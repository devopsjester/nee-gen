"""
Arrr! This be the main CLI module for the weather app, ye scallywag!
Hoist the sails and check the weather before ye set out to sea!
"""

import sys

import click

from weather.api import get_current_weather
from weather.location import get_current_location, get_location_from_zip


@click.group()
def cli():
    """Arrr! A weather CLI app — know thy skies before ye sail!"""


@cli.command("where-is")
@click.option("--zipcode", default=None, help="Zip code to look up.")
def where_is(zipcode):
    """Display the city and state for a zip code or your current location."""
    if zipcode:
        # Arrr! Look up the city and state for the given zip code!
        city, state, error = get_location_from_zip(zipcode)
        if error:
            click.echo(f"Error: {error}", err=True)
            sys.exit(1)
        click.echo(f"{zipcode} is in {city}, {state}.")
    else:
        # Arrr! No zip code given — find where the cap'n currently is!
        city, state, _zipcode, error = get_current_location()
        if error:
            click.echo(f"Error: {error}", err=True)
            sys.exit(1)
        click.echo(f"Your current location is {city}, {state}.")


@cli.command("current")
@click.option("--zipcode", default=None, help="Zip code to get weather for.")
def current(zipcode):
    """Display the current temperature and weather conditions for a location."""
    if zipcode:
        # Arrr! Use the provided zip code to fetch the weather!
        location = zipcode
    else:
        # Arrr! No zip code — determine the cap'n's location by IP!
        city_loc, state_loc, zip_loc, error = get_current_location()
        if error:
            click.echo(f"Error: {error}", err=True)
            sys.exit(1)
        # Prefer city+state for a more accurate weather lookup, fallback to zip
        if city_loc and state_loc:
            location = f"{city_loc}+{state_loc}"
        elif zip_loc:
            location = zip_loc
        else:
            click.echo("Error: Could not determine your current location.", err=True)
            sys.exit(1)

    temp_f, weather_desc, city, state, error = get_current_weather(location)
    if error:
        click.echo(f"Error: {error}", err=True)
        sys.exit(1)
    click.echo(f"It is currently {temp_f}ºF, and {weather_desc} in {city}, {state}.")
