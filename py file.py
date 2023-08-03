import requests


#first step
#install module
# pip install geopy
# pip install timezonefinder
# pip install requests
# pip install pytz
# pip install pil

from tkinter import *
import tkinter as tk

from geopy import location
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
import json
from PIL import Image, ImageTk
from configparser import ConfigParser

root=Tk()

root.title("Weather App")
root.geometry("910x500+300+300")
root.config(bg="#57adff")

def getWeather():
    city=Textfield.get()
    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city)

    obj=TimezoneFinder()
    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
    timezone.config(text=result)

    long_lat.config(text=f"{round(location.latitude,1)}°N,{round(location.longitude,1)}°E")

    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)

    api="https://api.openweathermap.org/data/2.5/weather?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&appid=a4561c0dcefe3ee7cde7a700bcf41fe8"
    # api = "https://api.openweathermap.org/data/3.0/onecall?lat=" + str(location.latitude) + "&lon=" + str(location.longitude)+"&appid=996572df5d5aa0672f4f26dd15f9227b"

    json_data=requests.get(api).json()

    temp=json_data['main']['temp']
    humidity=json_data['main']['humidity']
    pressure=json_data['main']['pressure']
    wind=json_data['wind']['speed']
    description=json_data['weather'][0]['description']

    # temp = json_data["current"]["temp"]
    # humidity = json_data['current']['humidity']
    # pressure = json_data['current']['pressure']
    # wind = json_data['current']['wind_speed']
    # description = json_data['current']['weather'][0]['description']

    print(temp)
    print(humidity)
    print(pressure)
    print(wind)
    print(description)

    t.config(text=(temp,"K"))
    h.config(text=(humidity,"%"))
    p.config(text=(pressure,"hPa"))
    w.config(text=(wind,"m/s"))
    d.config(text=description)

    #days
    first=datetime.now()
    day1.config(text=first.strftime("%A"))

    second=first + timedelta(days=1)
    day2.config(text=second.strftime("%A"))

    third = first + timedelta(days=2)
    day3.config(text=third.strftime("%A"))

    fourth = first + timedelta(days=3)
    day4.config(text=fourth.strftime("%A"))

    fifth = first + timedelta(days=4)
    day5.config(text=fifth.strftime("%A"))

    sixth = first + timedelta(days=5)
    day6.config(text=sixth.strftime("%A"))

    seventh = first + timedelta(days=6)
    day7.config(text=seventh.strftime("%A"))


#add the icon
imageicon=PhotoImage(file="weather.png")
root.iconphoto(False,imageicon)

#add the blue rectangle
Blue=PhotoImage(file="rect.png")
Label(image=Blue,background="#57adff").place(x=-2,y=5)

#add labels
Label1=Label(root,text="Temperature",font=("Helvetica",10),fg="white",background="darkblue")
Label1.place(x=40, y=30)


Label2=Label(root,text="Humidity",font=("Helvetica",10),fg="white",background="darkblue")
Label2.place(x=40, y=60)

Label3=Label(root,text="Pressure",font=("Helvetica",10),fg="white",background="darkblue")
Label3.place(x=40, y=90)

Label4=Label(root,text="Wind speed",font=("Helvetica",10),fg="white",background="darkblue")
Label4.place(x=40, y=120)

Label5=Label(root,text="Description",font=("Helvetica",10),fg="white",background="darkblue")
Label5.place(x=40, y=150)


#create searchbox

# SearchImage=PhotoImage(file="search1.png")
# Label(image=SearchImage,background="#57adff").place(x=400,y=30)

Searchbar=PhotoImage(file="searchbar1.png")
Label(image=Searchbar,background="#57adff").place(x=350,y=-60)

Searchbutton=PhotoImage(file="searchbutton.png")
button=Button(image=Searchbutton,cursor="hand2",background="#57adff",command=getWeather).place(x=600,y=74)


Sunimage=PhotoImage(file="sun1.png")
Label(image=Sunimage,background="#57adff").place(x=400,y=10)

#textfield for searchbar
Textfield=Entry(root,justify='center',width=13,font=("poppins",20,"bold"),bg="blue",border=0,fg="white")
Textfield.place(x=400,y=75)
Textfield.focus()


#actual clock
clock=Label(root,font=("Helventica",30,"bold"),fg='white',bg='#57adff')
clock.place(x=700,y=80)

#timezone
timezone=Label(root,font=("Helventica",15),fg='white',bg='#57adff')
timezone.place(x=500,y=10)

long_lat=Label(root,font=("Helventica",15),fg='white',bg='#57adff')
long_lat.place(x=500,y=40)


frame=Frame(root,width=910,height=250,bg="darkblue")
frame.pack(side=BOTTOM)


secondbox=PhotoImage(file="R1.png")
box=PhotoImage(file="R.png")

t=Label(root,font=("Helventica",15),fg='white',bg='#57adff')
t.place(x=170,y=30)

h=Label(root,font=("Helventica",15),fg='white',bg='#57adff')
h.place(x=170,y=60)

p=Label(root,font=("Helventica",15),fg='white',bg='#57adff')
p.place(x=170,y=90)

w=Label(root,font=("Helventica",15),fg='white',bg='#57adff')
w.place(x=170,y=120)

d=Label(root,font=("Helventica",15),fg='white',bg='#57adff')
d.place(x=170,y=150)





#first cell

firstframe=Frame(root, width=220,height=115, bg='white')
firstframe.place(x=59,y=290)


#second cell
secondframe=Frame(root, width=68,height=130, bg='white')
secondframe.place(x=317,y=284)

#third cell
thirdframe=Frame(root, width=68,height=130, bg='white')
thirdframe.place(x=417,y=284)
#fourth cell
fourthframe=Frame(root, width=68,height=130, bg='white')
fourthframe.place(x=517,y=284)

#fifth cell
fifthframe=Frame(root, width=68,height=130, bg='white')
fifthframe.place(x=617,y=284)
#sixth cell
sixthframe=Frame(root, width=68,height=130, bg='white')
sixthframe.place(x=717,y=284)

#seventh cell
seventhframe=Frame(root, width=68,height=130, bg='white')
seventhframe.place(x=817,y=284)

#days
day1=Label(firstframe, font="arial 20", bg='white',fg='darkblue')
day1.place(x=50,y=8)

day2=Label(secondframe, font="arial 9", bg='white',fg='darkblue')
day2.place(x=0,y=23)

day3=Label(thirdframe, font="arial 9", bg='white',fg='darkblue')
day3.place(x=0,y=23)

day4=Label(fourthframe, font="arial 9", bg='white',fg='darkblue')
day4.place(x=0,y=23)

day5=Label(fifthframe, font="arial 9", bg='white',fg='darkblue')
day5.place(x=0,y=23)

day6=Label(sixthframe, font="arial 9", bg='white',fg='darkblue')
day6.place(x=0,y=23)

day7=Label(seventhframe, font="arial 9", bg='white',fg='darkblue')
day7.place(x=0,y=23)


# Label(frame,image=firstbox,bg="white").place(x=700,y=700)
Label(frame,image=secondbox,bg="darkblue").place(x=20,y=10)
Label(frame,image=box,bg="darkblue").place(x=300,y=10)
Label(frame,image=box,bg="darkblue").place(x=400,y=10)
Label(frame,image=box,bg="darkblue").place(x=500,y=10)
Label(frame,image=box,bg="darkblue").place(x=600,y=10)
Label(frame,image=box,bg="darkblue").place(x=700,y=10)
Label(frame,image=box,bg="darkblue").place(x=800,y=10)

mainloop()