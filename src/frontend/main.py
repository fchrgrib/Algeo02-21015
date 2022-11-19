import os
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showerror

# Initialization --------------------------------------

window = Tk()
# icon here
window.configure(bg="white")
window.geometry("1040x720")
window.resizable(False, False)
window.title("GeoFace")

# Variables --------------------------------------

DATASET = StringVar() # dev note: Ini input Dataset-nya. Cara akses stringnya DATASET.get()
DATASET.set("")

DATASET_PLACEHOLDER = StringVar()
DATASET_PLACEHOLDER.set("No data chosen")

YOUR_IMAGE = StringVar() # dev note: Ini input Test Image-nya. Cara akses stringnya DATASET.get()
YOUR_IMAGE.set("")

YOUR_IMAGE_PLACEHOLDER = StringVar()
YOUR_IMAGE_PLACEHOLDER.set("No file chosen")

RESULT_STR = StringVar()
RESULT_STR.set("0% Similar")

# Function --------------------------------------     

def openFolder():
    DATASET_STR = filedialog.askdirectory(
        initialdir="..\\..\\",
        title = "Choose data set",
    )
    if DATASET_STR:
        DATASET.set(DATASET_STR)
        DATASET_PLACEHOLDER.set(os.path.basename(DATASET_STR))

def openFile():
    YOUR_IMAGE_STR = filedialog.askopenfilename(
        initialdir="..\\..\\",
        title = "Choose file",
        filetypes = (("png files", "*.png"),
        ("jpg files", "*.jpg"),
        ("all files", "*.*"))
    )
    if YOUR_IMAGE_STR:
        YOUR_IMAGE.set(YOUR_IMAGE_STR)
        YOUR_IMAGE_PLACEHOLDER.set(os.path.basename(YOUR_IMAGE_STR))

def calculateFace():
    if (DATASET.get() != "") & (YOUR_IMAGE.get() != ""):
        # dev note: Fungsi backend taro di sini
        print("Calculating face")
        print(DATASET.get())
        print(YOUR_IMAGE.get())
        # sampai sini
    else:
        showerror(title="Error", message="Data set and Image are invalid")

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
background_img = PhotoImage(file = f"src/frontend/img/main-background.png")
background = canvas.create_image(
    540.0, 360.0,
    image = background_img
)

# 3. Buttons
button1_img = PhotoImage(file = f"src/frontend/img/button1.png")
button1_entry = Button(
    image = button1_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = openFolder,
    relief = "flat"
)
button1_entry.place(
    x = 76, y = 270,
    width = 115,
    height = 40
)

button2_img = PhotoImage(file = f"src/frontend/img/button2.png")
button2_entry = Button(
    image = button2_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = openFile,
    relief = "flat"
)
button2_entry.place(
    x = 76, y = 375,
    width = 100,
    height = 40
)

button3_img = PhotoImage(file = f"src/frontend/img/search.png")
button3_entry = Button(
    image = button3_img,
    borderwidth = 0,
    highlightthickness = 0,
    command = calculateFace,
    relief = "flat"
)
button3_entry.place(
    x = 76, y = 475,
    width = 210,
    height = 35
)

# 4. Labels
label1_label = Label(
    canvas,
    textvariable = DATASET_PLACEHOLDER,
    font = ("Poppins", 11),
    fg = "#8B8B8B",
    borderwidth = 0,
    background = "#fff",
    highlightthickness= 0,
    anchor = "w",
    padx = 10
)
label1_label.place(
    x = 190, y = 270,
    width = 190,
    height = 40,
)

label2_label = Label(
    canvas,
    textvariable = YOUR_IMAGE_PLACEHOLDER,
    font = ("Poppins", 11),
    fg = "#8B8B8B",
    borderwidth = 0,
    background = "#fff",
    highlightthickness= 0,
    anchor = "w",
    padx = 10
)
label2_label.place(
    x = 180, y = 375,
    width = 190,
    height = 40,
)

result_label = Label(
    canvas,
    textvariable= RESULT_STR,
    font = ("Poppins", 14, "bold"),
    fg = "#86FFA8",
    borderwidth = 0,
    background = "#fff",
    highlightthickness= 0,
    anchor = "w",
    padx = 10
)

result_label.place(
    x = 68, y = 555,
    width = 190,
    height = 40,
)

window.mainloop()