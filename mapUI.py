
import tkintermapview
import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

# create tkinter window
root_tk = tk.Tk()
root_tk.geometry(f"{800}x{600}")
root_tk.title("MAP view")

# create map widget
map_widget = tkintermapview.TkinterMapView(root_tk, width=800, height=600, corner_radius=0)
map_widget.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

map_widget.set_zoom(15)
# set current widget position by address

marker_1 = map_widget.set_address("Belthangadi, karnataka, india", marker=True)

# print(marker_1.position, marker_1.text)  # get position and text
# path_1 = map_widget.set_path([marker_1.position,(13.9903521, 75.2825052),(14.9903521, 75.2825052) ])



root_tk.mainloop()