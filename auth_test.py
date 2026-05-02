import requests

url = "http://20.207.122.201/evaluation-service/auth"

data = {
    "email": "km7158@srmist.edu.in",
    "name": "KavinSaran MR",
    "rollNo": "RA2311003020243",
    "accessCode": "QkbpxH",
    "clientID": "d6e12366-2047-4ffe-8bef-d1338981501d",
    "clientSecret": "gKraDhtrUbQBZdPT"
}
res = requests.post(url, json=data)
print(res.json())