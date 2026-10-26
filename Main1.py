from tkinter import*
from tkinter import messagebox

root=Tk()
root.title("Virus Scanner")
root.geometry("200x200")

def msg():
    messagebox.showwarning("ALERT","THERE IS TROJON HORSE VIRUS IN YOUR COMPUTER PLS THROW YOUR LAPTOP AWAY BECAUSE THE HORSE WILL COME OUT AND KICK YOU!!!")

button=Button(root,text="Scan for Virus",command=msg)
button.place(x=40,y=80)

root.mainloop()