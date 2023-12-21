import requests

# https://opentdb.com/api.php?amount=10&type=boolean
parameters = {
    "amount": 10,
    "type": "boolean"
}

# endpoint is the url before ?
response = requests.get('https://opentdb.com/api.php', params=parameters)

# raise exception if there are any errors
response.raise_for_status()

# converts response data in json format
data = response.json()
# print(data["results"])

question_data = data["results"]
