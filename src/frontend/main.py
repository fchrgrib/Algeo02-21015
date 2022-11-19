from tkinter import *

# Initialization --------------------------------------

window = Tk()
# icon here
window.configure(bg="white")
window.geometry("1040x720")
window.resizable(False, False)
window.title("GeoFace")

# Variables --------------------------------------

# Components --------------------------------------

# 1. Canvas
canvas = Canvas(
    window,
    bg = "#fff",
    height = 720,
    width = 1080,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x=0,y=0)

# 2. Background
background_img = PhotoImage(file = f"img/main-background.png")
background = canvas.create_image(
    540.0, 360.0,
    image = background_img
)

window.mainloop()