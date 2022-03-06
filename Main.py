import tkinter as tk
import datetime as dt
from tkinter import *
root = tk.Tk()

x = dt.datetime.now()

print(x.strftime("%A"))

root.title("AQI Tracker")
root.geometry("700x700")
root.configure(bg='light blue') 

img = PhotoImage(file="landscape.png")
label = Label(
    root,
    image=img
)
label.place(x=0, y=0)

def nextPage():
    root.destroy()
    import Aqi

def prevPage():
    root.destroy()
    import WeatherApp_withicons

button1 = tk.Button(root,text='AQI',fg='black',font=('times new roman',18),width=8, command=nextPage)
button1.place(x = 100 , y= 250 , width=200 , height=60)

button2 = tk.Button(root,text='WEATHER',fg='black',font=('times new roman',18),width=8, command=prevPage)
button2.place(x = 400 , y= 250 , width=200 , height=60)

date = tk.Label(root,text=f"{x:%d : %B : %Y : %A    : %X}"   ,fg = "black",bg="light blue", font=('times new roman',18),width=60)
date.place(x = 0 , y= 5 )
root.mainloop()