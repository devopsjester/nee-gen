"""
Arrr! This here module fetches weather data from the high seas of the internet!
We use wttr.in — a free API that needs no registration or treasure (API key).
"""

import requests


def get_current_weather(location):
    """
    Arrr! Fetch current weather from wttr.in for the given location.
    Location can be a zip code, city name, or 'city+state' string.
    Returns (temp_f, weather_desc, city, state, error).
    Error be None if the winds be favourable.
    """
    url = f"https://wttr.in/{location}?format=j1"
    try:
        response = requests.get(
            url,
            timeout=10,
            headers={"User-Agent": "weather-cli/1.0"},
        )
        response.raise_for_status()
        data = response.json()
        current = data["current_condition"][0]
        temp_f = current["temp_F"]
        weather_desc = current["weatherDesc"][0]["value"]
        nearest = data["nearest_area"][0]
        city = nearest["areaName"][0]["value"]
        state = nearest["region"][0]["value"]
        return temp_f, weather_desc, city, state, None
    except requests.RequestException as e:
        return (
            None,
            None,
            None,
            None,
            f"Shiver me timbers! Failed to fetch weather: {e}",
        )
    except (KeyError, IndexError, ValueError) as e:
        return None, None, None, None, f"Davy Jones garbled the weather data: {e}"
