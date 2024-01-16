import tkinter as tk

# Top level window
frame = tk.Tk()
frame.title("PLAYER NAME")
frame.geometry('250x70')


# Function for getting Input
# from textbox and printing it
# at label widget

def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    print(inp)
inputtxt = tk.Text(frame,height=1,width=23)
inputtxt.pack()
printButton = tk.Button(frame,text = "ENTER",command = printInput)
printButton.pack()

frame.mainloop()