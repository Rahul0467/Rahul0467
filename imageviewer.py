from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("image")
root.iconbitmap("C:/Users/rahul/PycharmProjects/pythonProject/Guillendesign-Variations-3-Default-Icon.ico")
image = ImageTk.PhotoImage(Image.open("C:/Users/rahul/PycharmProjects/pythonProject/lbx spade poly/1.png"))
image1 = ImageTk.PhotoImage(Image.open("C:/Users/rahul/PycharmProjects/pythonProject/lbx spade poly/2.png"))
image2 = ImageTk.PhotoImage(Image.open("C:/Users/rahul/PycharmProjects/pythonProject/lbx spade poly/3.png"))
image_list = [image, image1, image2]
label = Label(image=image)
label.grid(row=0, column=0, columnspan=3)
status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E).grid(row=2, column=0,
                                                                                                    columnspan=3,
                                                                                                    sticky=W + E)


def right(n):
    global label
    global left_button
    global right_button
    global status

    label.grid_forget()
    label = Label(image=image_list[n - 1])
    label.grid(row=0, column=0, columnspan=3)
    right_button = Button(root, text=">>", command=lambda: right(n + 1))
    left_button = Button(root, text="<<", command=lambda: left(n - 1))
    if n == 3:
        right_button = Button(root, text=">>", state=DISABLED)
    right_button.grid(row=1, column=2)
    left_button.grid(row=1, column=0)
    label.grid(row=0, column=0, columnspan=3)

    status = Label(root, text="Image " + str(n) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E).grid(
        row=2, column=0,
        columnspan=3,
        sticky=W + E)


def left(n):
    global label
    global left_button
    global right_button
    global status
    label.grid_forget()
    label = Label(image=image_list[n - 1])
    label.grid(row=0, column=0, columnspan=3)
    right_button = Button(root, text=">>", command=lambda: right(n + 1))
    left_button = Button(root, text="<<", command=lambda: left(n - 1))
    if n == 1:
        left_button = Button(root, text="<<", state=DISABLED)
    right_button.grid(row=1, column=2)
    left_button.grid(row=1, column=0)
    label.grid(row=0, column=0, columnspan=3)

    status = Label(root, text="Image " + str(n) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E).grid(
        row=2, column=0,
        columnspan=3,
        sticky=W + E)


left_button = Button(root, text="<<", command=left, state=DISABLED).grid(row=1, column=0)
button_exit = Button(root, text="EXIT", command=root.quit).grid(row=1, column=1)
right_button = Button(root, text=">>", command=lambda: right(2)).grid(row=1, column=2, pady=10)
root.mainloop()
