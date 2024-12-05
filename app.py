import os
from flask import Flask, render_template, request, jsonify
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the Google API Key from the environment variable
google_api_key = os.getenv("GOOGLE_API_KEY")

if not google_api_key:
    raise ValueError("Google API key not found. Please set GOOGLE_API_KEY in your .env file.")

# Read the website text (knowledge base) with 'utf-8' encoding to handle any special characters
with open('pdf_text.txt', 'r', encoding='utf-8') as file:
    prompt = file.read()

# Define the assistant's template
hotel_assistant_template = prompt + """
You are the hotel manager of Vivanta New Delhi, Dwarka, named "Mr. Vivanta". 
Your expertise is in providing information and advice about anything related to Vivanta New Delhi, Dwarka. 
You are polite and professional in all interactions.

Rules:
1. If the question is about Vivanta New Delhi, Dwarka, provide accurate information.
2. If the question is a greeting (e.g., "Hello", "Hi", "Thank you"), respond warmly and politely, such as "Hello! How can I assist you with Vivanta New Delhi, Dwarka today?" or "You're welcome! Feel free to ask more about Vivanta New Delhi, Dwarka."
3. For any other queries outside this scope, respond with, "I'm sorry, I didn't quite get that. Could you please rephrase or ask something about the hotel?"

Question: {question} 
Answer: 
"""

# Initialize the Gemini model with the prompt template
hotel_assistant_prompt_template = PromptTemplate(
    input_variables=["question"],
    template=hotel_assistant_template
)

# Initialize the Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    api_key=google_api_key,
    temperature=0  # Set temperature to 0 for deterministic responses
)

# Create a chain combining the template and the model
llm_chain = hotel_assistant_prompt_template | llm

def query_llm(question):
    """
    Query the Gemini model with the formatted question.
    """
    # Trim leading/trailing spaces and normalize input
    question = question.strip().lower()
    
    # Handle standalone greetings and thank-you messages
    greetings = ["hello", "hi", "hey"]
    thank_you_phrases = ["thank you", "thanks"]
    
    if question in greetings:
        return "Hello! How can I assist you with Vivanta New Delhi, Dwarka today?"
    if any(thank_phrase in question for thank_phrase in thank_you_phrases):
        return "You're welcome! Feel free to ask more about Vivanta New Delhi, Dwarka."
    
    # Query the LLM for valid hotel-related questions
    response = llm_chain.invoke({'question': question})
    return response.content.strip()


# Flask app for the chatbot
app = Flask(__name__)

@app.route("/")
def index():
    """
    Render the main chatbot interface.
    """
    return render_template("index.html")

@app.route("/chatbot", methods=["POST"])
def chatbot():
    """
    Handle chatbot queries from the user.
    """
    data = request.get_json()
    question = data["question"]
    response = query_llm(question)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)