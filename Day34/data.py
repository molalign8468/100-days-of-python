import requests

parameter = {
    "amount":10,
    "category":18,
    "type":"boolean"
}

API_URL = "https://opentdb.com/api.php"

data = requests.get(url=API_URL,params=parameter)
data.raise_for_status()
question_data = data.json()["results"]
