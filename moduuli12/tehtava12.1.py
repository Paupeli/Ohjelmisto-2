import requests

def fetch_random_joke():
    url = "https://api.chucknorris.io/jokes/random"

    response = requests.get(url)

    if response.status_code == 200:
        joke_data = response.json()
        joke = joke_data['value']
        print(joke)

    else:
        print("Failed to fetch a joke. Please try again.")

fetch_random_joke()