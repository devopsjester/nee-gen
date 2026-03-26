"""
Arrr! This here module handles all location-related matters, ye landlubber!
We use free APIs to find yer whereabouts without needin' a treasure map (or API key).
"""

import requests


def get_location_from_zip(zipcode):
    """
    Arrr! Look up city and state for a given zip code using zippopotam.us.
    Returns (city, state, error) — error be None if all went smooth, like calm seas.
    """
    url = f"https://api.zippopotam.us/us/{zipcode}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 404:
            return (
                None,
                None,
                f"Blimey! Zip code '{zipcode}' not found in these waters.",
            )
        response.raise_for_status()
        data = response.json()
        city = data["places"][0]["place name"]
        state = data["places"][0]["state"]
        return city, state, None
    except requests.RequestException as e:
        return None, None, f"Shiver me timbers! Failed to look up zip code: {e}"
    except (KeyError, IndexError) as e:
        return None, None, f"Davy Jones stole the response data: {e}"


def get_current_location():
    """
    Arrr! Determine the current location by IP geolocation using ip-api.com.
    Returns (city, state, zipcode, error) — error be None if the seas be calm.
    """
    url = "http://ip-api.com/json/"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        if data.get("status") == "fail":
            return (
                None,
                None,
                None,
                "Failed to determine current location from IP address.",
            )
        city = data.get("city")
        state = data.get("regionName")
        zipcode = data.get("zip")
        return city, state, zipcode, None
    except requests.RequestException as e:
        return (
            None,
            None,
            None,
            f"Shiver me timbers! Failed to fetch current location: {e}",
        )
    except (KeyError, ValueError) as e:
        return None, None, None, f"Davy Jones stole the response data: {e}"
