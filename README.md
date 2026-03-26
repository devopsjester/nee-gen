# copilot-agent-weather-demo

A command-line weather application built with Python and Click. Check your current weather or look up conditions by zip code — no API key required!

## Requirements

- Python 3.7+

## Installation

1. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Install the `weather` CLI command:

   ```bash
   pip install -e .
   ```

## Usage

### `where-is`

Display the city and state for a zip code, or your current location.

```bash
# Look up a zip code
weather where-is --zipcode 90210

# Use your current location (determined by IP)
weather where-is
```

**Example output:**

```
90210 is in Beverly Hills, California.
Your current location is Austin, Texas.
```

### `current`

Display the current temperature (°F) and weather conditions.

```bash
# Get weather for a zip code
weather current --zipcode 10001

# Get weather for your current location
weather current
```

**Example output:**

```
It is currently 68ºF, and Partly cloudy in New York City, New York.
```

## APIs Used

- **[ip-api.com](http://ip-api.com)** — Free IP geolocation, no key required.
- **[zippopotam.us](https://api.zippopotam.us)** — Free zip code lookup, no key required.
- **[wttr.in](https://wttr.in)** — Free weather data, no key required.
