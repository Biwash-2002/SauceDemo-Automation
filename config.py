import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
STANDARD_USERNAME = os.getenv("STANDARD_USERNAME")
STANDARD_PASSWORD = os.getenv("STANDARD_PASSWORD")