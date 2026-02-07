import tkinter as tk
import requests

API_KEY = "7cde33f33df790fcc336d08759d421e6"

def get_weather():
    city = entry_city.get()
    if city == "":
        result.config(text="Please enter a city")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        result.config(text="City not found")
        return

    temp = data["main"]["temp"]
    feels = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]
    condition = data["weather"][0]["description"]

    result.config(
        text=f"City: {city}\n"
             f"Temperature: {temp} °C\n"
             f"Feels Like: {feels} °C\n"
             f"Humidity: {humidity}%\n"
             f"Wind Speed: {wind} m/s\n"
             f"Condition: {condition}"
    )

def get_forecast():
    city = entry_city.get()
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    data = requests.get(url).json()

    if data.get("cod") != "200":
        forecast_label.config(text="Forecast not available")
        return

    forecast_text = "Next Hours Forecast:\n"
    for i in range(0, 8, 2):  # next few hours
        time = data["list"][i]["dt_txt"]
        temp = data["list"][i]["main"]["temp"]
        desc = data["list"][i]["weather"][0]["description"]
        forecast_text += f"{time} → {temp}°C, {desc}\n"

    forecast_label.config(text=forecast_text)

root = tk.Tk()
root.title("Advanced Weather Application")
root.geometry("400x500")

tk.Label(root, text="Advanced Weather App", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Enter City Name").pack()
entry_city = tk.Entry(root)
entry_city.pack(pady=5)

tk.Button(root, text="Get Current Weather", command=get_weather).pack(pady=5)
tk.Button(root, text="Get Forecast", command=get_forecast).pack(pady=5)

result = tk.Label(root, text="", justify="left")
result.pack(pady=10)

forecast_label = tk.Label(root, text="", justify="left")
forecast_label.pack(pady=10)

root.mainloop()
