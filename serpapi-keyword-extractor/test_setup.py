import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Test API key loading
api_key = os.getenv('SERPAPI_KEY')
if api_key:
    print("✅ API key loaded successfully")
    print(f"API key starts with: {api_key[:10]}...")
else:
    print("❌ API key not found. Check your .env file")

# Test imports
try:
    import requests
    import nltk
    print("✅ All dependencies imported successfully")
except ImportError as e:
    print(f"❌ Import error: {e}")