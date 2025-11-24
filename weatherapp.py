import requests


API_KEY = "39619fa462c0aec313bbff57ef5bd1ac"             
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"          
    }
    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        if data["cod"] != 200:
            return f"Error: {data['message']}"
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "description": data["weather"][0]["description"].title()
        }
        return weather
    except requests.exceptions.RequestException:
        return "Network Error!"
def show_weather():
    city = input("Enter City Name: ")
    result = get_weather(city)
    if isinstance(result, dict):
        print("\n📍 Weather in", result["city"])
        print("🌡 Temperature:", result["temperature"], "°C")
        print("💧 Humidity:", result["humidity"], "%")
        print("💨 Wind Speed:", result["wind_speed"], "m/s")
        print("🌥 Condition:", result["description"])
    else:
        print(result)
show_weather()
