import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# GitHub Token
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
