import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    city = city_name.get()
    if city == "":
        messagebox.showerror("Error", "Please enter a city name")
        return

    api_key = "867344988d3af197d3891d76d4263dd3"  # Replace with your OpenWeatherMap API key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(base_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        messagebox.showerror("Error", "Failed to retrieve weather data")
        return

    weather_data = response.json()
    weather_description = weather_data["weather"][0]["description"]
    temperature = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    wind_speed = weather_data["wind"]["speed"]

    weather_result = f"Weather in {city}:\n"
    weather_result += f"Description: {weather_description}\n"
    weather_result += f"Temperature: {temperature}°C\n"
    weather_result += f"Humidity: {humidity}%\n"
    weather_result += f"Wind Speed: {wind_speed} m/s"

    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, weather_result)

root = tk.Tk()
root.title("Weather App")

city_name = tk.StringVar()
city_label = tk.Label(root, text="Enter City Name:")
city_label.pack()
city_entry = tk.Entry(root, textvariable=city_name)
city_entry.pack()

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack()

result_text = tk.Text(root, height=10, width=40)
result_text.pack()

root.mainloop()
