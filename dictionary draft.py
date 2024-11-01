# Import the requests library for making API calls
import requests

# Prints a welcome message
print("Welcome to The Free Lexicon")

# Define a function for the dictionary word search process
def dict():
    try:
        # API request setup
        request_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
        word_request = input("Please enter text: ")
        word_input = request_url + word_request
        
        # Get data from the Web API
        response = requests.get(word_input)
        # Check for a successful response (status code 200)
        if response.status_code == 200:
            # Convert the JSON data object into a Python-friendly format
            data = response.json()
            for entry in data:
                # Access part of speech from entry
                for meaning in entry["meanings"]:
                     # Print a separator line
                    print("------------")
                    # Print the part of speech
                    print("Part of Speech:", meaning["partOfSpeech"])
                    # Access definitions from entry
                    for definition in meaning["definitions"]:
                        # Print the definition(s)
                        print("- Definition:", definition["definition"])
                         # Print a separator line
                        print("------------")
        else:
            # For non-200 status code responses, convert the JSON error object into a Python-friendly format
            error_data = response.json()
            # Get the status code and print it
            print("Error:", response.status_code)
            # Get the error title fom the error data and print it
            print("Sorry,", error_data["title"])
             # Print a separator line
            print("------------")
            
    except Exception as error:
        # Handle other potential API request errors
        print("Sorry, there was a problem processing this request")
        print(error)

# A loop for running the "dict()" function ten times.
for i in range(10):
    dict()

            

