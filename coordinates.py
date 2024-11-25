from cProfile import label
from tkinter import Entry, Label, Button
from Задания.холст import window
from test import geocoder, query, results

from tkinter import Tk
from opencage.geocoder import OpenCageGeocode

def get_coords(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        query=city
        results = geocoder.geocode(query)
        if results:
            lat=round(results[0]['geometry']['lat'],3)
            lng=round(results[0]['geometry']['lng'],3)
            return lat,lng
        else:
            print('Данные не найдены')
    except Exception as err:
        print(f'Неизвестная ошибка {err}')


def show_coords(event=None):
    city=entry.get()
    coordinates = get_coords(city, key)
    label.config(text=coordinates)


key='65465465465'

window=Tk()
window.title('Поиск координат города')

entry=Entry()
entry.pack()
entry.bind('Return', show_coords)
entry.focus_set()

but=Button(text='Поиск', command=show_coords)
but.pack()

label=Label(text='Введите город и нажмите кнопку для поиска')
label.pack()

window.mainloop()


