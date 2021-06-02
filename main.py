from tkinter import *
import tkinter.messagebox as tkMessageBox
import mysql.connector
from mysql.connector import Error

root = Tk()
# UPPER TITLE
root.title(" COVID19 Vaccine Booking ")
width = 640
height = 480
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2)-(width/2)
y = (screen_height/2)-(height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)


#DATABASE NAME=covid

def database():
    global conn, cursor
    conn = mysql.connector.connect(
        host="localhost", user="root", password="", database="covid")

    cursor = conn.cursor()

# register function inside which all logic is there

def register():
    database()  #DATABASE IS CALLED
    if Name.get() == "" or Age.get() == "" or Gender.get() == "" or Phone.get() == "" or Email.get() == "" or City.get() == "":
        result.config(text="Please Fill the required fields",
                      fg="orange", font=("Comic Sans", 10))  # EMPTY INPUT
    else:
        cursor.execute("INSERT INTO `Registrations` (name,age,gender,phone,email,city) VALUES (%s,%s,%s,%s,%s,%s) ", (str(Name.get()), str(Age.get()), str(Gender.get()), str(Phone.get()), str(Email.get()), str(City.get())))
        conn.commit() #SUCCESSFUL INPUT

        result.config(text="Successfully Created!",
                      fg="green", font=("Comic Sans", 10))
        Name.delete(0, 'end')
        Age.delete(0,'end')
        Gender.delete(0,'end')
        Phone.delete(0,'end')
        Email.delete(0,'end')
        City.delete(0,'end')

        cursor.close()
        conn.close()

def shift_screen():
    root.destroy()
    import admin


#title styling

TitleFrame = Frame(root, height=150, width=640, bd=1, relief=SOLID)
TitleFrame.pack(side=TOP)
RegisterFrame = Frame(root)  #frame=div tag 
RegisterFrame.pack(side=TOP, pady=20) #

# title at top

#labels

labelTitle = Label(TitleFrame, text="COVID-19 Vaccine Registration",
                   bd=1, width=640, font=("Comic Sans", 14),bg='yellow')
labelTitle.pack()

labelName = Label(RegisterFrame, text="Name:", font=("Comic Sans", 12), bd=18)
labelName.grid(row=1)

labelAge = Label(RegisterFrame, text="Age:", font=("Comic Sans", 12), bd=18)
labelAge.grid(row=2)

labelGender = Label(RegisterFrame, text="Gender:", font=("Comic Sans", 12), bd=18)
labelGender.grid(row=3)

labelPhone = Label(RegisterFrame, text="Phone:", font=("Comic Sans", 12), bd=18)
labelPhone.grid(row=4)

labelEmail = Label(RegisterFrame, text="Email:", font=("Comic Sans", 12), bd=18)
labelEmail.grid(row=5)

labelCity = Label(RegisterFrame, text="City:", font=("Comic Sans", 12), bd=18)
labelCity.grid(row=6)

result = Label(RegisterFrame, text="")
result.grid(row=7, columnspan=2)

#input of lables

Name = Entry(RegisterFrame, textvariable="NAME", font=("Comic Sans", 12), width=30)
Name.grid(row=1, column=1)

Age = Entry(RegisterFrame, textvariable="AGE", font=("Comic Sans", 12), width=30)
Age.grid(row=2, column=1)

Gender = Entry(RegisterFrame, textvariable="GENDER", font=("Comic Sans", 12), width=30)
Gender.grid(row=3, column=1)

Phone = Entry(RegisterFrame, textvariable="PHONE", font=("Comic Sans", 12), width=30)
Phone.grid(row=4, column=1)

Email = Entry(RegisterFrame, textvariable="EMAIL", font=("Comic Sans", 12), width=30)
Email.grid(row=5, column=1)

City = Entry(RegisterFrame, textvariable="CITY", font=("Comic Sans", 12), width=30)
City.grid(row=6, column=1)


btn = Button(RegisterFrame, text="Register", font=("Comic Sans", 12), command=register)
btn.grid(row=8, columnspan=2)


#top menu

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Show Data", command=shift_screen)
filemenu.add_command(label="Exit")
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)


#imp function (otherwise it will run in loop)
if __name__ == '__main__':
    root.mainloop()
