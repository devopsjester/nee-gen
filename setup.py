# Arrr! This here setup.py registers the weather command, ye landlubber!
from setuptools import find_packages, setup

setup(
    name="weather",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "click",
        "requests",
    ],
    entry_points={
        "console_scripts": [
            # Arrr! This maps the 'weather' command to our CLI, matey!
            "weather=weather.cli:cli",
        ],
    },
)
