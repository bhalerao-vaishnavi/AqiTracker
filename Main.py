import tkinter as tk
from tkinter import *
root = tk.Tk()



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


button1 = tk.Button(root,text='AQI',fg='blue',font=('times new roman',18),width=
8, command=nextPage)
button1.place(x = 150 , y= 200 , width=200 , height=60)



button2 = tk.Button(root,text='WEATHER',fg='blue',font=('times new roman',18),width=8, command=prevPage)
button2.place(x = 350 , y= 200 , width=200 , height=60)




root.mainloop()