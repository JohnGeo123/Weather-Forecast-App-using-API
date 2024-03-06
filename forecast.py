import requests

def get_weather_forecast(city):
    api_key = "YOUR_API_KEY"  # Replace "YOUR_API_KEY" with your actual API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data["cod"] == 200:
            weather_description = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            
            print(f"Weather forecast for {city}:")
            print(f"Description: {weather_description}")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s")
        else:
            print("Error: Unable to fetch weather data.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather_forecast(city)
