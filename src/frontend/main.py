from tkinter import *

# Initialization --------------------------------------

window = Tk()
# icon here
window.configure(bg="white")
window.geometry("1080x720")
window.resizable(False, False)
window.title("GeoFace")

# Variables --------------------------------------

# Components --------------------------------------

# 1. Canvas
canvas = Canvas(
    window,
    bg = "#f5f6f8",
    height = 720,
    width = 1080,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x=0,y=0)

# 2. Background
# background_img = PhotoImage(file = f"img/main-background.png")
background = canvas.create_image(
    540.0, 360.0,
    image = "img/main-background.png"
)

window.mainloop()