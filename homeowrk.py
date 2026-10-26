from tkinter import*
from tkinter import messagebox

root=Tk()
root.title("Exam Scanner")
root.geometry("200x200")

def msg():
    messagebox.showwarning("ALERT","THERE IS PROBLEM SIR PT2 IS INCOMING AND WE DONT HAVE ENOUGH FUEL TO AIRSTRIKE THE SCHOOL SO WE NEED TO STUDY THERE I S NO CHOICE LEFT WE NEED TO SURRENDER!!")

button=Button(root,text="Scan for Virus",command=msg)
button.place(x=40,y=80)

root.mainloop()