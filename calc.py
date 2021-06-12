from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("400x400")
e = Entry(root, width=60, border=3)
e.grid(row=0, column=0, columnspan=5, padx=10, pady=10)


def buttonclick(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def buttonclear():
    return e.delete(0, END)


def buttonadd():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)


def buttonequal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))

def buttonsub():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)


def buttonmulti():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)


def buttondivide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)


button1 = Button(root, text="1", padx=40, pady=20, command=lambda: buttonclick(1)).grid(row=3, column=0)
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: buttonclick(2)).grid(row=3, column=1)
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: buttonclick(3)).grid(row=3, column=2)
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: buttonclick(4)).grid(row=2, column=0)
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: buttonclick(5)).grid(row=2, column=1)
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: buttonclick(6)).grid(row=2, column=2)
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: buttonclick(7)).grid(row=1, column=0)
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: buttonclick(8)).grid(row=1, column=1)
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: buttonclick(9)).grid(row=1, column=2)
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: buttonclick(0)).grid(row=4, column=0)
button_add = Button(root, text="+", padx=40, pady=20, command=buttonadd).grid(row=4, column=3)
button_equal = Button(root, text="=", padx=40, pady=20, command=buttonequal).grid(row=4, column=2)
button_clear = Button(root, text="C", padx=40, pady=20, command=lambda: buttonclear()).grid(row=4, column=1)
button_sub = Button(root, text="-", padx=40, pady=20, command=buttonsub).grid(row=2, column=3)
button_multi = Button(root, text="*", padx=40, pady=20, command=buttonmulti).grid(row=1, column=3)
button_divide = Button(root, text="/", padx=40, pady=20, command=buttondivide).grid(row=3, column=3)
root.mainloop()
