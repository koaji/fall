import tkinter
from tkinter import ttk

# thread
import threading
import time

cuiroot = tkinter.Tk()
cuiroot.title(u"fall")
cuiroot.geometry("350x400+100+50")

canvas = tkinter.Canvas(cuiroot, bg="white", height=300, width=300)


global pos
pos = [0, 0]

def refresh():
    canvas.delete("block")
    canvas.create_rectangle(pos[0], pos[1], 100 + pos[0], 30 + pos[1], fill="red", tag="block")
    canvas.pack()

def command_up():
    pos[1] = pos[1] - 10
    refresh()

def command_down():
    pos[1] = pos[1] + 10
    refresh()

def command_right():
    pos[0] = pos[0] + 10
    refresh()

def command_left():
    pos[0] = pos[0] - 10
    refresh()

if __name__ == "__main__":
    #th = threading.Thread(target=refresh)
    #th.start()
    
    up_btn = ttk.Button(cuiroot, text="UP", command=command_up)
    up_btn.place(x=100, y=350)
    down_btn = ttk.Button(cuiroot, text="DOWN", command=command_down)
    down_btn.place(x=100, y=380)
    left_btn = ttk.Button(cuiroot, text="LEFT", command=command_left)
    left_btn.place(x=0, y=350)
    right_btn = ttk.Button(cuiroot, text="RIGHT", command=command_right)
    right_btn.place(x=200,y=350)
    refresh()
    cuiroot.mainloop()

