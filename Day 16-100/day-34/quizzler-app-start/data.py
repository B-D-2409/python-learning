import requests

parametars = {
    "amount": 10,
    "type": "boolean"
}
response = requests.get(url="https://opentdb.com/api.php?amount=10&category=21&difficulty=medium&type=boolean", params=parametars)
response.raise_for_status()
data = response.json()
question_data = data["results"]
print(question_data)

