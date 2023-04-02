import requests
from dotenv import load_dotenv
import os

load_dotenv()

headers = {
    "x-app-id": os.getenv("NUTRIONIX_APP_ID"),
    "x-app-key": os.getenv("NUTRIONIX_API_KEY"),
    "x-remote-user-id": "0",
}


