import requests
import time
from useful import Loader, ClearScreen

Api = "d9bee5753a36850aecb14c4e4f78b338"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={Api}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return (
            f"City: {data['name']}\n"
            f"Temperature: {data['main']['temp']} °C\n"
            f"Description: {data['weather'][0]['description'].capitalize()}\n"
            f"Humidity: {data['main']['humidity']}%\n"
            f"Wind Speed: {data['wind']['speed']} m/s"
        )
    else:
        return "Error: City not found or API request failed."

while True:
    enter = input("Enter City Name: ")
    ClearScreen.clear()
    Loader.loading("Fetching weather data")
    time.sleep(1)
    ClearScreen.clear()
    print(get_weather(enter))
    ask = input("Do You want to check another city? (yes/no): ").lower().strip()
    ClearScreen.clear()
    if ask.lower() == 'no':
        Loader.loading("Goodbye")
        break
    elif ask.lower() != 'yes':
        print("Invalid input\n\n")
        Loader.loading("Exiting")
    else:
      continue
