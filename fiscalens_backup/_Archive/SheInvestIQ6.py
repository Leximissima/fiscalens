import requests
import google.generativeai as genai 
import os
from io import BytesIO
from dotenv import load_dotenv


# Load environment variables from .env file and configure the API
load_dotenv()
api_key = os.getenv("API_KEY")
if not api_key:
    raise EnvironmentError("API key not found. Ensure it's set in the .env file.")

genai.configure(api_key=api_key)

##user_prompt = "Please summarize this doc."


# Load system prompt from file
try:
    with open("SystemPrompt.txt", "r") as file:
        system_prompt = file.read()
except FileNotFoundError:
    raise FileNotFoundError("SystemPrompt.txt not found. Ensure the file is in the same directory.")

# Load user prompt from file
try:
    with open("UserPrompt.txt", "r") as file:
        user_prompt = file.read()
except FileNotFoundError:
    raise FileNotFoundError("UserPrompt.txt not found. Ensure the file is in the same directory.")


# Initialize the generative model
model_name='gemini-1.5-flash'
model = genai.GenerativeModel(
    model_name=model_name,
    system_instruction=system_prompt,
)

# User Prompt and URL of PDF
PDF_path='https://ir.tesla.com/_flysystem/s3/sec/000162828024002390/tsla-20231231-gen.pdf'


# Step 1: Download the PDF content from the URL
def fetch_pdf_from_url(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return BytesIO(response.content)
    

# Step 2: Upload the PDF to Gemini
def upload_pdf_to_Gemini(pdf_file):
    # Use the BytesIO object for uploading with the correct MIME type
    upload_response = genai.upload_file(pdf_file, mime_type="application/pdf")
    model_response = model.generate_content([user_prompt, upload_response])
    return model_response.text

# Start SheInvestIQ
if __name__ == "__main__":
    try:
        pdf_file = fetch_pdf_from_url(PDF_path)
        response = upload_pdf_to_Gemini(pdf_file)
        print("I am SheInvestIQ. Here is the summary of the financial statement. \n", response)
    except Exception as e:
        print("Error:", e)
