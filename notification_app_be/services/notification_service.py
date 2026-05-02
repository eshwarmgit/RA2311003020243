import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "http://20.207.122.201/evaluation-service"
TOKEN = os.getenv("TOKEN")

# Priority mapping
PRIORITY_MAP = {
    "email": 3,
    "sms": 2,
    "push": 1
}


def fetch_notifications():
    try:
        headers = {
            "Authorization": f"Bearer {TOKEN}"
        }

        response = requests.get(
            f"{BASE_URL}/notifications",
            headers=headers,
            timeout=5
        )

        # Debug (can remove later)
        print("Status:", response.status_code)

        if response.status_code != 200:
            print("Error Response:", response.text)
            return {"notifications": []}
        print(response.json())
        return response.json()
        

    except Exception as e:
        print("Fetch error:", e)
        return {"notifications": []}



def process_notifications(data):
    try:
        notifications = data.get("notifications", [])

        # Safe sorting
        sorted_notifications = sorted(
            notifications,
            key=lambda x: (
                PRIORITY_MAP.get(x.get("type", ""), 0),
                x.get("timestamp", "")
            ),
            reverse=True
        )

        return sorted_notifications[:5]

    except Exception as e:
        print("Processing error:", e)
        return []