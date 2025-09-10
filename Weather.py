import requests

def get_weather(city_name, api_key):
    """Fetch weather data for a given city using OpenWeatherMap API"""
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # use 'imperial' for Fahrenheit
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise error for bad responses (4xx, 5xx)
        data = response.json()

        # Extract useful info
        city = data["name"]
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"\n Weather in {city}:")
        print(f" Temperature: {temp}°C")
        print(f" Condition: {weather}")
        print(f" Humidity: {humidity}%")
        print(f" Wind Speed: {wind_speed} m/s")

    except requests.exceptions.RequestException as e:
        print("⚠ Error fetching data:", e)
    except KeyError:
        print("⚠ Invalid city name or API response")

if __name__ == "_main_":
    api_key = "31a745caf0ba574639273c13e63507c3"  # 🔑 Replace with your OpenWeatherMap API key
    city = input("Enter city name: ")
    get_weather(city, api_key)