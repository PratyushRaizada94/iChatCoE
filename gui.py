from tkinter import *

from tkinter import messagebox

def on_closing():

    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        GUI.destroy()

def Enter_Hit(event):

    utter=input_user.get()
    message.config(state=NORMAL,fg="Blue")
    message.insert(INSERT,"User: "+utter+"\n")

   #Handshake starts here

    if (utter=="hi" or utter=="hello"):
        reply="Hello"
        message.insert(INSERT,"Bot: "+reply+"\n")
        input_value.set("")
        message.config(state=DISABLED)
    else:
        reply="Sorry, I did not understand what you just said."
        message.insert(INSERT,"Bot: "+reply+"\n")
        input_value.set("")
        message.config(state=DISABLED)                                                                                                          

if __name__ == "__main__":
    GUI=Tk()
    GUI.title("Infosys Chatbot")
    input_value=StringVar()
    scrollbar = Scrollbar(GUI)
    scrollbar.pack(side=RIGHT, fill=Y)
    label1=Label(GUI,text="Welcome to Infosys Chatbot!",fg="Red")
    label1.pack(side=TOP,fill=X)
    message=Text(GUI)
    message.pack()
    message.config(state=DISABLED,yscrollcommand=scrollbar.set)
    scrollbar.config(command=message.yview)
    input_user=Entry(GUI,text=input_value)
    user_label=Label(GUI,text="Enter message here:",fg="Red")
    user_label.pack(fill=X)
    input_user.pack(fill=X)
    input_user.bind("<Return>", Enter_Hit)
    GUI.protocol("WM_DELETE_WINDOW", on_closing)
    GUI.mainloop()