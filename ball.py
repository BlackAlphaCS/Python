from tkinter import *
import random
import time


root = Tk()

root.title("Stopwatch")

label1 = Label(root, width=5, font=("Ubuntu", 100), text="00:00")
label1.grid(row=0, columnspan=2)

btn1 = Button(root, text="Start", font=("Ubuntu", 30), command=start_sw)
btn2 = Button(root, text="Stop!", font=("Ubuntu", 30), command=stop_sw)
btn3 = Button(root, text="Continue", font=("Ubuntu", 30), command=continue_sw)
btn4 = Button(root, text="Reset", font=("Ubuntu", 30), command=reset_sw)

btn1.grid(row=1,columnspan=2,sticky="ew")

root.mainloop()
