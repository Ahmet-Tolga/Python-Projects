from tkinter import *
import json,requests
def bul():
    url="https://api.openweathermap.org/data/2.5/weather?q="
    name=enter.get()
    url+=name
    url+="&appid=890acf67d71ed8d3b1692e6937ce9bb0&lang=tr&units=metric"
    a=requests.get(url).json()["name"]
    sehir["text"]=a
    b=requests.get(url).json()["weather"]
    for i in b:
        b=i["description"]
    hava["text"]=b
    c=requests.get(url).json()["main"]
    c=str(c["temp"])
    c+=" "+"Derece"
    derece["text"]=c
app=Tk()
app.geometry("350x400")
app.title("weather forecast")
label=Label(app,justify="center",font="40px",text="Bölge ismi Girin:")
label.pack(ipady=10)
enter=Entry(app,justify="center",font="40px")
enter.pack(fill="both",ipady=10,padx=10,pady=5)
btn=Button(app,justify="center",text="Bul",bg="light green",font="20px",width=4,command=bul)
btn.pack(ipady=10)
sehir=Label(app,justify="center",font="300px")
sehir.pack(ipady=20)
hava=Label(app,justify="center",font="40px")
hava.pack(ipady=10)
derece=Label(app,justify="center",font="200px")
derece.pack(ipady=40)
app.mainloop()
