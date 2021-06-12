from tkinter import *
import requests


def weather(root):
    c = city.get()
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + c + "&appid=5ecb7234173d904bb766af30b53b8433"
    json_data = requests.get(url).json()
    condition = json_data["weather"][0]["main"]
    temp = int(json_data["main"]["temp"] - 273.15)
    final_info = condition + "\n" + str(temp)
    label1.config(text=final_info)


root = Tk()
root.title("Weather App")
root.geometry("400x400")
f = ("poppins", 35, "bold")
t = ("poppins", 15, "bold")
city = Entry(root, justify="center", font=t)
city.pack(pady=20)
city.focus()
city.bind("<Return>", weather)

label1 = Label(root, font=t)
label1.pack()

root.mainloop()
