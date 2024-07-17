import requests
import json
from datetime import datetime, timedelta
import pytz

url = "https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=60.10&lon=9.58"

headers = {
    "User-Agent": "MyCustomUserAgent/1.0"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = json.loads(response.text)
    timeseries = data["properties"]["timeseries"]
    weather_dict = {}

    for data_point in timeseries:
        if len(weather_dict) != 3:
            time_utc = data_point["time"]
            time_utc_parsed = datetime.fromisoformat(time_utc[:-1])
            time_est = time_utc_parsed - timedelta(hours=4)
            time_est_str = time_est.strftime('%Y-%m-%dT%I:%M:%S %p')
            air_temp = data_point["data"]["instant"]["details"]["air_temperature"]
            humidity = data_point["data"]["instant"]["details"]["relative_humidity"]
            wind_speed = data_point["data"]["instant"]["details"]["wind_speed"]
            air_pressure = data_point["data"]["instant"]["details"]["air_pressure_at_sea_level"]
            summary = data_point["data"].get("next_1_hours", {}).get("summary", {}).get("symbol_code", None)
            precip_next_hour_details = data_point["data"].get("next_1_hours", {}).get("details", {})
            precip_next_hour = precip_next_hour_details.get("precipitation_amount", None)

            weather_dict[time_est_str] = (air_temp, humidity, wind_speed, air_pressure, summary, precip_next_hour)

    print(weather_dict)
else:
    print("Failed to fetch weather data:", response.status_code)
