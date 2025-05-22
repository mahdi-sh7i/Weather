# Weather App (PyQt5)

A simple desktop weather application built with Python and PyQt5. This app fetches and displays real-time weather data for any city using the OpenWeatherMap API. It features a modern, frameless, and transparent UI.

## Features

- Search weather by city name
- Displays
  - City
  - Temperature (°C)
  - Humidity
  - Weather condition
  - Description
  - Wind speed
- Shows condition-specific images
- Frameless, centered, and transparent window design

## Previwe

![3](https://github.com/user-attachments/assets/510ed336-023e-4763-89de-71a3153b3bdd)


## Prerequisites

- Python 3.x
- `PyQt5`
- `requests` library
- A `.ui` file named `weather.ui` in the same directory
- Weather condition images in
  - `homemahdiprojectmin-pic`
  - `homemahdiprojectbig-pic`

## Installation

1. Clone the repository or copy the project files.
2. Make sure `weather.ui` and required image folders exist.
3. Install dependencies

```bash
pip install PyQt5 requests
```

## Usage

Run the app

```bash
python weacher.py
```

1. Enter a city name in the text box.
2. Click the search button.
3. Weather data and images will appear.

## API

This application uses the [OpenWeatherMap API](httpsopenweathermap.orgapi).  
You need an API key (replace the default one in `weacher.py` with your own).

## Notes

- Ensure a stable internet connection.
- Replace image paths with your own if needed.
- API key should be kept secure for production use.
