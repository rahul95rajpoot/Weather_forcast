# import requests
# import urllib.parse

# city = input("Enter the city name: ")
# city_encoded = urllib.parse.quote(city)  # Encode the city name
# print("Display weather report for:", city)

# url = "https://wttr.in/{}".format(city_encoded)
# res = requests.get(url)
# print(res.text)


import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests

def get_weather():
    city = city_entry.get()
    api_key = '9bda61a3871b3559569f96f4f0578624'  # Replace with your actual API key
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()

    if data['cod'] == '200':
        forecasts = data['list']
        result_tree.delete(*result_tree.get_children())  # Clear the previous content

        for i, forecast in enumerate(forecasts):
            timestamp = forecast['dt']
            forecast_time = forecast['dt_txt']
            temperature = forecast['main']['temp']
            weather_description = forecast['weather'][0]['description']

            # Determine row color based on odd/even index
            row_color = "lightblue" if i % 2 == 0 else "lightcyan"

            result_tree.insert("", "end", values=(forecast_time, weather_description, f"{temperature}°C"), tags=("row", f"row{i}"))
            result_tree.tag_configure(f"row{i}", background=row_color)

    else:
        result_tree.delete(*result_tree.get_children())  # Clear the previous content
        result_tree.insert("", "end", values=("Error", data['message'], ""), tags=("error",))
        result_tree.tag_configure("error", background="pink")

# Create the main window
root = tk.Tk()
root.title("Weather Forecasting by Rahul Rajpoot")

# Set window background image
background_image = Image.open("weatherfore_cast/sky.jpeg")  # Replace with your image file
background_image = background_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
background_photo = ImageTk.PhotoImage(background_image)

background_label = tk.Label(root, image=background_photo)
background_label.image = background_photo
background_label.place(relwidth=1, relheight=1)

# Create GUI elements
city_label = tk.Label(root, text="Enter city name:", bg="white", font=("Helvetica", 12))
city_label.pack(pady=(10, 0))

city_entry = tk.Entry(root, font=("Helvetica", 12))
city_entry.pack(pady=5)

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather, bg="#4CAF50", fg="white", font=("Helvetica", 12))
get_weather_button.pack(pady=10)

# Create a Treeview widget for displaying the result
result_tree = ttk.Treeview(root, columns=("Date/Time", "Description", "Temperature"), show="headings")
result_tree.heading("Date/Time", text="Date/Time")
result_tree.heading("Description", text="Description")
result_tree.heading("Temperature", text="Temperature")
result_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()


