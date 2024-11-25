from tkinter import *
from opencage.geocoder import OpenCageGeocode

def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        #results = geocoder.geocode(city)
        results = geocoder.geocode(city, language='ru')

        if results:
            lat = round(results[0]['geometry']['lat'], 2)
            lng = round(results[0]['geometry']['lng'], 2)
            country = results[0]['components']['country']
            region = results[0]['components']['state']
            return f"Широта: {lat}, Долгота: {lng}\nСтрана: {country}\nРегион: {region}"
        else:
            return "Город не найден"
    except Exception as e:
        return f"Ошибка: {e}"

def show_coordinates(event=None):
    city = entry.get()
    coordinates = get_coordinates(city, key)
    label.config(text=coordinates)

# Интерфейс
window = Tk()
window.title("Поиск координат города")

key = '97c595bec990457d975c12c16a4ec4a7'

# Элементы интерфейса
entry = Entry()
entry.pack()
entry.bind("<Return>", show_coordinates)

button = Button(text="Поиск", command=show_coordinates)
button.pack()

label = Label(text="Введите город и нажмите Поиск")
label.pack()

# Запуск приложения
window.mainloop()

