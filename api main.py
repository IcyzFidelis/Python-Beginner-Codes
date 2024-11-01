import requests

request_url = "https://official-joke-api.appspot.com/random_ten"

# Get data from the Web API
response = requests.get(request_url)

# Convert the JSON data object into a Python-friendly format
data = response.json()

# Go through each item in the list of data
for joke in data:
  print(joke["setup"])
  print(joke["punchline"])
  print("---------")
