import tkinter as tk
import os

# Main
root = tk.Tk()


def calc_add():
    # get() : Gets the value from text box in the string format
    result = eval(a_text.get()) + eval(b_text.get())

    ans.configure(text="Answer : "+a_text.get() + "+" +
                  b_text.get() + " = " + str(result))


def clear_btn():
    a_text.delete(first=0, last=100)
    b_text.delete(first=0, last=100)
    a_text.focus()
    ans.configure(text="")


# Canvas
canvas = tk.Canvas(root, height=600, width=400, bg="#AC1818")
canvas.pack()

# frame : Frame()
frame = tk.Frame(root, bg="#5C839D")
frame.place(relwidth=0.8, relheight=0.8, rely=0.1, relx=0.1)

# Label()
lbl_heading = tk.Label(
    frame, text="ADDITION OF TWO NUMBERS", bg="#5C839D", fg="Black")
lbl_heading.place(x=90, y=20)

# label 1 : Enter the value of a:

lbl_a = tk.Label(frame, text="Enter the value of a", bg="#5C839D", fg="Black")
lbl_a.place(x=20, y=80)

# Label 2 : Enter the value of a:
lbl_b = tk.Label(frame, text="Enter the value of b", bg="#5C839D", fg="Black")
lbl_b.place(x=20, y=120)

# Text Box : Entry()
a_text = tk.Entry(frame, width=20, bd=1)
a_text.place(x=170, y=80)

# Text Box : Entry()
b_text = tk.Entry(frame, width=20, bd=1)
b_text.place(x=170, y=120)

# Button : Button()
cal_btn = tk.Button(frame, text="ADD", padx=25,
                    pady=5, bg="#AC1818", fg="Black", command=calc_add)
cal_btn.place(x=60, y=170)

# Button : Button()
clr_btn = tk.Button(frame, text="CLEAR", padx=25,
                    pady=5, bg="#AC1818", fg="Black", command=clear_btn)
clr_btn.place(x=170, y=170)

# Answer()
ans = tk.Label(
    frame, text="", bg="#5C839D", fg="Black")
ans.place(x=90, y=220)

root.mainloop()
