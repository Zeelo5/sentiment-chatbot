import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_default_secret_key')
    # OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'your_openai_api_key')
    # SUGGESTIONS_API_KEY = os.getenv('SUGGESTIONS_API_KEY', 'your_suggestions_api_key')
 
