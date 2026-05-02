import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "http://20.207.122.201/evaluation-service"
TOKEN = os.getenv("TOKEN")


def get_headers():
    return {
        "Authorization": f"Bearer {TOKEN}"
    }


def fetch_depots():
    try:
        res = requests.get(f"{BASE_URL}/depots", headers=get_headers(), timeout=5)
        print("Depot Status:", res.status_code)

        if res.status_code != 200:
            print("Depot Error:", res.text)
            return []

        return res.json().get("depots", [])

    except Exception as e:
        print("Depot Fetch Error:", e)
        return []


def fetch_vehicles():
    try:
        res = requests.get(f"{BASE_URL}/vehicles", headers=get_headers(), timeout=5)
        print("Vehicle Status:", res.status_code)

        if res.status_code != 200:
            print("Vehicle Error:", res.text)
            return []

        return res.json().get("vehicles", [])

    except Exception as e:
        print("Vehicle Fetch Error:", e)
        return []


def assign_vehicles(vehicles, depots):
    result = []

    try:
        # Sort vehicles by Duration (largest first)
        vehicles.sort(key=lambda x: x.get("Duration", 0), reverse=True)

        for v in vehicles:
            v_hours = v.get("Duration", 0)

            for d in depots:
                d_hours = d.get("MechanicHours", 0)

                if d_hours >= v_hours:
                    result.append({
                        "taskId": v.get("TaskID"),
                        "depotId": d.get("ID")
                    })

                    # reduce available hours
                    d["MechanicHours"] -= v_hours
                    break

        return result

    except Exception as e:
        print("ASSIGN ERROR:", e)
        return []