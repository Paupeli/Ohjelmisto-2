import requests

def get_weather(municipality, api_key):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={municipality}&appid={api_key}'

    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()

        condition = weather_data ['weather'][0]['description']
        temperature_kelvin  = weather_data ['main']['temp']

        temperature_celsius = temperature_kelvin - 273.15

        print(f"Weather condition: {condition}")
        print(f"Temperature: {temperature_celsius: .2f}°C")

    else:
        print("Failed to fetch the data. Please check the city name or API key.")

def main():
    municipality = input("Enter the name of the municipality: ")
    api_key = input("Enter your OpenWeather API key: ")

    get_weather(municipality,api_key)

main()