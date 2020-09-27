import Tkinter
import tkMessageBox

top = Tkinter.Tk()
num = 1

def helloCallBack():
	tkMessageBox.showinfo( "Calculator", num)

B = Tkinter.Button(top, text ="Add", command = helloCallBack)

B.pack()
top.mainloop()