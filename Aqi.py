from configparser import ConfigParser
from turtle import width
import requests
import tkinter as tk

root = tk.Tk()



root.title("AQI Tracker")
root.geometry("700x700")
root.configure(bg='light blue') 

def get_aqi(world):
    city = textbox1.get()
    key='37f96394ffe8b6cca1110af3d8270604c711c688'
    url='http://api.waqi.info/feed/' + city + '/?token='
    main_url = url + key  # Main URL
    r = requests.get(main_url)  # Accessing the URL
    data = r.json()['data']  # Fetching data in variable
    aqi = data['aqi']  # Air quality Index

    air_label['text'] = aqi

textbox1 = tk.Entry(root,font=('times new roman',20),width=40)
textbox1.place(x = 200 , y=90 , width=300 , height=60)

button1 = tk.Button(root,text='AQI',fg='blue',font=('times new roman',18),width=8,command=lambda: get_aqi(textbox1.get()))
button1.place(x = 150 , y= 200 , width=200 , height=60)

air_label=tk.Label(root,text="",font=('times new roman',18),width=40)
air_label.place(x = 200 , y= 300 , width=150 , height=50)


root.mainloop()