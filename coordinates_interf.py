



window=Tk()
window.title("Поиск координат города")

entry=Entry()
entry.pack()
entry.bind("<Return>", show_coords)
entry.focus_set()

but=Button(text="Поиск", command=show_coords)
but.pack()

label=Label(text="Введите город и нажмите кнопку для поиска")
label.pack()
