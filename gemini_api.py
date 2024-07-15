import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')

# Configure Google Generative AI
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("Write a story about a AI and magic")
print(response.text)