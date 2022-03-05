from configparser import ConfigParser
from tkinter.font import BOLD
from turtle import width
import requests
import tkinter as tk

root = tk.Tk()



root.title("AQI Tracker")
root.geometry("700x700")
root.configure(bg='light blue') 



def get_aqi(city):
    try:
        city = textbox1.get()
        key='37f96394ffe8b6cca1110af3d8270604c711c688'
        url='http://api.waqi.info/feed/' + city + '/?token='
        main_url = url + key  # Main URL
        r = requests.get(main_url)  # Accessing the URL
        data = r.json()['data']  # Fetching data in variable
        aqi = data['aqi']  # Air quality Index    
        air_label['text'] = aqi
    except:
        hellow =tk.Label(root,text="Data not available sorry",fg ="black" ,font=('times new roman',18,BOLD),width=500)
        hellow.place(x = 300 , y= 500 , width=150 , height=50)

    if (aqi < 50):
        condition =tk.Label(root,text="Good",bg = "green" ,font=('times new roman',18,BOLD),width=40)
        condition.place(x = 300 , y= 500 , width=150 , height=50)

    elif(aqi > 50 and aqi < 100):
       
        condition =tk.Label(root,text="Moderate",bg = "yellow" ,font=('times new roman',18,BOLD),width=40)
        condition.place(x = 300 , y= 500 , width=150 , height=50)

    elif(aqi > 100 and aqi < 150):
        
        condition =tk.Label(root,text="Unhealthy for Sensitive Groups",bg = "orange" ,font=('times new roman',18,BOLD),width=40)
        condition.place(x = 300 , y= 500 , width=150 , height=50)

    elif(aqi > 150 and aqi < 200):
        
        condition =tk.Label(root,text="Unhealthy",bg = "red" ,font=('times new roman',18,BOLD),width=40)
        condition.place(x = 300 , y= 500 , width=150 , height=50)
    
    elif(aqi > 200 and aqi < 300):
        
        condition =tk.Label(root,text="Very Unhealthy",bg = "purple" ,font=('times new roman',18,BOLD),width=40)
        condition.place(x = 300 , y= 500 , width=150 , height=50)

    else:
        condition =tk.Label(root,text="Hazardous",bg = "crimson" ,font=('times new roman',18,BOLD),width=40)
        condition.place(x = 300 , y= 500 , width=150 , height=50)

textbox1 = tk.Entry(root,font=('times new roman',20),width=40)
textbox1.place(x = 200 , y=90 , width=300 , height=60)

button1 = tk.Button(root,text='AQI',fg='blue',font=('times new roman',18),width=8,command=lambda: get_aqi(textbox1.get()))
button1.place(x = 150 , y= 200 , width=200 , height=60)

air_label=tk.Label(root,text="",font=('times new roman',18),width=40)
air_label.place(x = 200 , y= 300 , width=150 , height=50)

root.mainloop()