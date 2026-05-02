import requests
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
BASE_URL = "http://20.207.122.201/evaluation-service"


def log(stack, level, package, message):
    url = f"{BASE_URL}/logs"

    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }

    payload = {
        "stack": stack.lower(),
        "level": level.lower(),
        "package": package.lower(),
        "message": message
    }

    try:
        requests.post(url, json=payload, headers=headers)
    except Exception as e:
        print("Logging failed:", e)


def log_wrapper(func):
    def wrapper(*args, **kwargs):
        log("backend", "info", "controller", f"{func.__name__} called")
        return func(*args, **kwargs)
    return wrapper