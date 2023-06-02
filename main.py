import tkinter
from tkinter import *
import customtkinter
import requests
from PIL import Image, ImageTk

# System
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

# Api
api_key = '30d4741c779ba94c470ca1f63045390a'

# Functions
def function():
    user_input = input1.get()
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

    if weather_data.json()['cod'] == '404':
        label2.configure(text='No City Found, try again')
    else:
        weather = weather_data.json()['weather'][0]['main']
        temp = round(weather_data.json()['main']['temp'])
        celsius = (temp - 32) * 5/9

        label2.configure(text=f"The weather in {user_input} is: {weather}")
        label3.configure(text=f"The temperature in {user_input} is: {celsius:.2f}ºC")  # Format the temperature



#images_function
        if weather == "Clouds":
            label4.configure(image=imgcloud, width=500, height=90)
        elif weather == "Rain":
            label4.configure(image=imgrain, width=500, height=90)
        elif weather == "Clear":
            label4.configure(image=imgclear, width=500, height=90)
            
# App
app = customtkinter.CTk()
app.geometry("450x480")
app.title("Weather Checker")
app.iconbitmap('fav.ico')

# Images
imgcloud = ImageTk.PhotoImage(Image.open("clouds.png"))
imgclear = ImageTk.PhotoImage(Image.open("clear.png"))
imgrain = ImageTk.PhotoImage(Image.open("rain.png"))
imgdefault = ImageTk.PhotoImage(Image.open("default.png"))
label4 = Label(image=imgdefault, width=5, height=9)
label4.pack()


# Widgets
frame = customtkinter.CTkFrame(app)
frame.pack(padx=20, pady=20, expand=True)

label = customtkinter.CTkLabel(frame, text="Weather Checker", text_color="white", font=('Arial', 19), width=300, height=80)
label.pack(padx=20, pady=20)

input1 = customtkinter.CTkEntry(frame, placeholder_text="Enter the city")
input1.pack(padx=20, pady=3)

btn = customtkinter.CTkButton(frame, text="Check", command=function)
btn.pack(padx=20, pady=3)

label2 = customtkinter.CTkLabel(frame, text="Weather", text_color="white", font=('Arial', 19), width=300, height=80)
label2.pack(padx=20, pady=3)

label3 = customtkinter.CTkLabel(frame, text="Temp", text_color="white", font=('Arial', 19), width=300, height=80)
label3.pack(padx=20, pady=3)

# Run the app
app.mainloop()
