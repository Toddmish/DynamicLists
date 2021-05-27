from tkinter import *
try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 

except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here

window=Tk()
# add widgets here

window.title('Hello Python')
window.geometry("300x200+10+20")
window.mainloop()