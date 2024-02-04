import requests
import json

def get_city_data():
    while True:
        name = input("Name of the city: ")
        api_url = f'https://api.api-ninjas.com/v1/city?name={name}'
        response = requests.get(api_url, headers={'X-Api-Key': 'YOUR-API-KEY'}) #here must be your api_key
        if response.status_code == requests.codes.ok:
            try:
                data = response.json()
                if data:
                    return data[0]
                else:
                    print("There is no city with this name, or something went wrong. Try again.")
            except json.decoder.JSONDecodeError:
                print("Error decoding JSON content. Try again.")
        else:
            print(f"Request failed with status code: {response.status_code}. Try again.")

def kelvin_to_celsius(kelvin):
    return round(kelvin - 273.15, 2)

def get_weather_data(lat, lon, appid):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {'lat': lat, 'lon': lon, 'appid': appid}
    response = requests.get(url, params=params).json()
    return response['main']['temp']


city_data = get_city_data()
lat, lon = city_data['latitude'], city_data['longitude']
appid = 'YOUR_API_KEY for  OpenWeatherMap'

temperature = get_weather_data(lat, lon, appid)

print(f"\nTemperature in {city_data['name'].upper()} is about: {kelvin_to_celsius(temperature)} ℃")
