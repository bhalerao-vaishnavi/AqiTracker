import tkinter as tk

root = tk.Tk()



root.title("AQI Tracker")
root.geometry("700x700")
root.configure(bg='light blue') 



button1 = tk.Button(root,text='AQI',fg='blue',font=('times new roman',18),width=8)
button1.place(x = 150 , y= 200 , width=200 , height=60)

button2 = tk.Button(root,text='WEATHER',fg='blue',font=('times new roman',18),width=8)
button2.place(x = 350 , y= 200 , width=200 , height=60)




root.mainloop()