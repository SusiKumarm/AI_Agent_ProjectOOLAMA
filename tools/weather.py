import requests

def get_weather():

    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=13.0827"
        "&longitude=80.2707"
        "&current_weather=true"
    )

    response = requests.get(url)

    return response.json()["current_weather"]