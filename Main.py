from tkinter import*
window=Tk()
window.title()
window.geometry("100x100")

def hande_press(event):
    '''print key associated with press'''
    print(event.char)
window.bind("<Key>",hande_press)

def handle_cliclk(event):
    print("Button is clicked")
button=Button(text="click me")
button.pack()
button.bind("<Button-1>",handle_cliclk)


window.mainloop()