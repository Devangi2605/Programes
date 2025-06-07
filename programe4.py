'''
Build a Weather app using Python and Tkinter library and OpenWeatherMap API

'''
import tkinter as tk
from tkinter import ttk, messagebox
import requests
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.dates as mdates
import datetime

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Forecast App")
        self.root.geometry("1000x800")

        # API configuration
        self.api_key = "7a902715986376aac2ac960d16e2fd59"
        self.base_url = "http://api.openweathermap.org/data/2.5/forecast"
# To help from open weather map because of API
        # GUI Elements
        self.create_widgets()
        self.setup_plot_area()

    def create_widgets(self):
        # Input Frame
        input_frame = ttk.Frame(self.root)
        input_frame.pack(pady=10)

        self.city_entry = ttk.Entry(input_frame, width=30)
        self.city_entry.insert(0, "Enter City (e.g., London,uk)")
        self.city_entry.pack(side=tk.LEFT, padx=5)

        self.fetch_btn = ttk.Button(input_frame, text="Get Forecast", command=self.fetch_weather)
        self.fetch_btn.pack(side=tk.LEFT)

        # Weather Info Display
        self.weather_info = ttk.Label(self.root, font=('Helvetica', 14))
        self.weather_info.pack(pady=20)

    def setup_plot_area(self):
        # Plot Frame
        self.plot_frame = ttk.Frame(self.root)
        self.plot_frame.pack(fill=tk.BOTH, expand=True)

        # Matplotlib Figure
        self.fig = Figure(figsize=(8, 6), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def fetch_weather(self):
        try:
            city = self.city_entry.get()
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric'
            }
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            self.weather_data = response.json()
            self.display_current_weather()
            self.plot_forecast()
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Failed to fetch weather data: {str(e)}")

    def display_current_weather(self):
        current = self.weather_data['list'][0]
        main = current['main']
        weather = current['weather'][0]
        info_text = (
            f"Current Weather: {weather['description'].title()}\n"
            f"Temperature: {main['temp']}°C\n"
            f"Humidity: {main['humidity']}%\n"
            f"Wind: {current['wind']['speed']} m/s"
        )
        self.weather_info.config(text=info_text)

    def plot_forecast(self):
        self.ax.clear()

        # Extract forecast data
        dates = [entry['dt_txt'] for entry in self.weather_data['list']]
        temps = [entry['main']['temp'] for entry in self.weather_data['list']]

        # Convert string dates to datetime objects
        dates = [datetime.datetime.strptime(d, '%Y-%m-%d %H:%M:%S') for d in dates]

        # Plot formatting
        self.ax.plot(dates, temps, marker='o', linestyle='-')
        self.ax.xaxis.set_major_formatter(mdates.DateFormatter('%a %H:%M'))
        self.ax.set_title("5-Day Forecast")
        self.ax.set_ylabel("Temperature (°C)")
        self.fig.autofmt_xdate()
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()


