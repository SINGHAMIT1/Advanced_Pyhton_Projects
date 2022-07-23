# PIL library in Python which stands for Python Imaging Library
# Python framework for building GUI application (tkinter)

# creating an application to convert a PNG image to JPG

# importing necessary libraries
import tkinter as tk
from tkinter import filedialog
from PIL import Image

root = tk.Tk()
canvus1 = tk.Canvas(root, width=300, height=250, bg="azure3", relief="raised")
canvus1.pack()

label1 = tk.Label(root, text="Image Converter", bg="azure3")
label1.config(font=("helvetica", 20))
canvus1.create_window(150, 70, window=label1)


# import PNG file
def getPng():
    global im1
    import_file_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path)


# browse PNG
browse_png = tk.Button(text="Select PNG file", command=getPng, bg="royalblue",
                       fg="white",
                       font=("helvetica", 12, "bold"))
canvus1.create_window(150, 130, window=browse_png)


# convert function
def convert():
    global im1
    export_file_path = filedialog.asksaveasfilename(defaultextension=".jpg")
    im1.save(export_file_path)


# save
save_button = tk.Button(text="Convert PNG to JPG", command=convert, bg="royalblue",
                        fg="white",
                        font=("helvetica", 12, "bold"))
canvus1.create_window(150, 180, window=save_button)

root.mainloop()

