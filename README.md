# Hotel Assistant Chatbot - "ViviBot"

## **Project Overview**
"ViviBot" is a personalized chatbot designed to assist users with information about **Vivanta New Delhi, Dwarka**. This chatbot is powered by **LangChain** and **Google Generative AI (Gemini)**, hosted on a Flask web application, and deployed on Render.

The bot is named "Mr. Vivanta," reflecting its role as a virtual hotel manager, providing users with accurate, polite, and professional responses to their queries about the hotel.

---

## **Features**
- Provides information specific to **Vivanta New Delhi, Dwarka**, such as:
  - Location details
  - Hotel amenities and facilities
  - Check-in and check-out policies
  - Dining options
- Handles greetings warmly and professionally.
- Declines queries outside the scope of hotel-related information with a polite message.
- Hosted and accessible live online: [**ViviBot on Render**](https://personalchatbot.onrender.com).

---

## **Technologies Used**
- **Flask**: Backend framework for handling requests and rendering responses.
- **LangChain**: For creating a prompt template and integrating with the Google Generative AI model.
- **Google Generative AI (Gemini)**: Language model for generating accurate and context-aware responses.
- **dotenv**: For securely managing environment variables.
- **Docker**: For containerizing the application.
- **Render**: For deployment and hosting.

---

## **Setup Instructions**
### **1. Prerequisites**
- Python 3.8+
- Google API Key for the Generative AI model
- Docker installed (if running the app in a container)
- A `.env` file containing:

GOOGLE_API_KEY=your_google_api_key_here


### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3. Run Locally
- Place your hotel knowledge base in a file named pdf_text.txt in the root directory.
- Start the Flask app:
```bash
python app.py
```
- Open the app at http://localhost:5000/.

### Deployment on Render
The chatbot is deployed and live on Render. You can access it here:
https://personalchatbot.onrender.com

### File Structure
```bash
hotel-assistant-chatbot/
├── app.py                 # Main application code
├── pdf_text.txt           # Knowledge base for the chatbot
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html         # Frontend HTML template
├── .env                   # Environment variables (excluded from Git)
├── .gitignore             # Ignored files for version control
└── Dockerfile             # Docker configuration for deployment
```

### How to Interact with ViviBot
- Open the live link: https://personalchatbot.onrender.com.
- Ask any hotel-related questions, such as:
- "Where is your hotel?"
- "What facilities do you offer?"
- "What are the check-in and check-out times?"
- ViviBot will respond with accurate and professional answers!

### Future Enhancements
- Add multilingual support.
- Expand the knowledge base with more detailed information about hotel services and nearby attractions.
- Integrate voice commands for a more interactive experience.

### Author
- Developed by Dattatray Bodake. Contributions and feedback are welcome! 😊
