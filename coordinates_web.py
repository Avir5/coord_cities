from tkinter import Tk
from opencage.geocoder import OpenCageGeocode
import webbrowser

def get_coords(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        query=city
        results = geocoder.geocode(query)
        if results:
            lat=round(results[0]['geometry']['lat'],3)
            lng=round(results[0]['geometry']['lng'],3)

            osm=f'https://www.openstreetmap.org/?mlat={lat}&mlon={lng}'
            return {'coordinates':f'Широта:{lat}, Долгота:{lng}'}
        else:
            return {'coordinates':None, "map_url":None'}
    except Exception as err:
        print(f'Неизвестная ошибка {err}')


def show_coords(event=None):
    global map_url
    city=entry.get()
    result = get_coords(city, key)

    map_url=result['map_url']
    coordinates=result['coordinates']
    label.config(text=coordinates)


def show_map():
    if map_url:
        webbrowser.open(map_url)


key='97c595bec990457d975c12c16a4ec4a7'

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

label = Label(text='Открыть карту', command=show_map)
label.pack()

window.mainloop()

'''
def show_coords(event=None):
    global map_url
    city=entry.get()
    result = get_coords(city, key)

    map_url=result["map_url"]
    coordinates=result["coordinates"]
    label.config(text=coordinates)
'''