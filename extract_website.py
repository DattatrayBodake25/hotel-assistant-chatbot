import requests
from bs4 import BeautifulSoup

target_url = "https://www.vivantahotels.com/en-in/"

try:
    print(f"Fetching content from {target_url}")
    response = requests.get(target_url)

    if response.status_code == 200:
        print("Website content retrieved successfully!")
        soup = BeautifulSoup(response.content, 'html.parser')
        text = ""

        # Extract all paragraphs
        for paragraph in soup.find_all('p'):
            text += paragraph.get_text() + "\n"

        # Save text to a file
        output_file = "website_text.txt"
        with open(output_file, "w", encoding="utf-8") as text_file:
            text_file.write(text)

        print(f"Text extracted and saved to {output_file}")
    else:
        print(f"Error: Failed to retrieve website content. Status code: {response.status_code}")

except Exception as e:
    print(f"An error occurred: {e}")