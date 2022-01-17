import requests
import json

response_API = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
data_raw = response_API.text
question_data = json.loads(data_raw)