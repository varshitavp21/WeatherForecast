from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
from PIL import Image,ImageTk
import pytz
import json

root  = Tk()
root.title("Weather")
root.geometry("890x470+300+300")
root.resizable(False,False)

# bg = PhotoImage(file="images/1.png")
#
# # Show image using label
# label1 = Label(root, image=bg)
# label1.place(x=0, y=0)

root.configure(bg="#57adff")

def getWeather():
    city = textfield.get()

    getlocator = Nominatim(user_agent="geoapiExercise")
    location = getlocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    timezone.config(text=result)
    long_lat.config(text=f"{round(location.latitude,4)}°N,{round(location.longitude,4)}°E")

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)

    #weather
    api ="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=669073e0fee502f0d5c3814811cf7a4037"
    json_data = requests.get(api).json()

    if 'current' in json_data:
        # current
        temp = json_data['current']['temp']
        humidity = json_data['current']['humidity']
        pressure = json_data['current']['pressure']
        wind = json_data['current']['wind_speed']
        description = json_data['current']['weather'][0]['description']

        t.config(text=(temp, "°C"))
        h.config(text=(humidity, "%"))
        p.config(text=(pressure, "hPa"))
        w.config(text=(wind, "m/s"))
        d.config(text=description)

    else:
        # handle error here
        d.config(text="Error: Could not retrieve weather data.")



#icon
image_icon = PhotoImage(file="images/Images/logo.png")
root.iconphoto(False,image_icon)

Round_box = PhotoImage(file="images/Images/Rounded Rectangle 1.png")
Label(root,image=Round_box,bg="#57adff").place(x=30,y=110)

#label

label1 = Label(root,text="Temperature",font=('Helvetica',11),fg="white",bg="#203243")
label1.place(x=50,y=120)

label2 = Label(root,text="Humidity",font=('Helvetica',11),fg="white",bg="#203243")
label2.place(x=50,y=140)

label3 = Label(root,text="Pressure",font=('Helvetica',11),fg="white",bg="#203243")
label3.place(x=50,y=160)

label4 = Label(root,text="Wind Speed",font=('Helvetica',11),fg="white",bg="#203243")
label4.place(x=50,y=180)

label5 = Label(root,text="Description",font=('Helvetica',11),fg="white",bg="#203243")
label5.place(x=50,y=200)


##search box
Search_image = PhotoImage(file="images/Images/Rounded Rectangle 3.png")
myimage = Label(image=Search_image,bg="#57adff")
myimage.place(x=270,y=120)

wea_image = PhotoImage(file="images/Images/Layer 7.png")
weatherimage = Label(root,image=wea_image,bg="#203243")
weatherimage.place(x=290,y=127)

textfield = tk.Entry(root,justify='center',width=15,font=('poppins',25,'bold'),bg="#203243",border=0,fg="white")
textfield.place(x=370,y=130)
textfield.focus()

Search_icon = PhotoImage(file="images/Images/Layer 6.png")
myimage_icon = Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#203243",command=getWeather)
myimage_icon.place(x=645,y=125)


#frame box
frame = Frame(root,width=900,height=180,bg="#212120")
frame.pack(side=BOTTOM)

#bottom box
firstbox = PhotoImage(file="images/Images/Rounded Rectangle 2.png")
secondbox = PhotoImage(file="images/Images/Rounded Rectangle 2 copy.png")

Label(frame,image=firstbox,bg="#212120").place(x=30,y=20)
Label(frame,image=secondbox,bg="#212120").place(x=300,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=400,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=500,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=600,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=700,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=800,y=30)

#clock (here we will place time)
clock = Label(root,font=("Helvetica",30,'bold'),fg="white",bg="#57adff")
clock.place(x=30,y=20)

#timezone

timezone = Label(root,font=("Helvetica",20),fg="white",bg="#57adff")
timezone.place(x=700,y=20)

long_lat = Label(root,font=("Helvetica",10),fg="white",bg="#57adff")
long_lat.place(x=700,y=50)

#th
t = Label(root,font=("Helvetica",11),fg="white",bg="#203243")
t.place(x=150,y=120)

h = Label(root,font=("Helvetica",11),fg="white",bg="#203243")
h.place(x=150,y=140)

p = Label(root,font=("Helvetica",11),fg="white",bg="#203243")
p.place(x=150,y=160)

w = Label(root,font=("Helvetica",11),fg="white",bg="#203243")
w.place(x=150,y=180)

d = Label(root,font=("Helvetica",11),fg="white",bg="#203243")
d.place(x=150,y=200)










root.mainloop()



