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

def shift_screen():
    root.destroy()
    import main

#title styling


TitleFrame = Frame(root, height=100, width=640, bd=1, relief=SOLID)
TitleFrame.pack(side=TOP)
RegisterFrame = Frame(root)
RegisterFrame.pack(side=TOP, pady=20)
DataFrame=Frame(root)
DataFrame.pack(side=TOP,pady=20)


labelTitle = Label(TitleFrame, text="COVID-19 Vaccine Registration Data",font=("Comic Sans",18),bg='yellow', bd=1, width=640)
labelTitle.pack()


database()


def search():
    for k in DataFrame.winfo_children():
        k.destroy()

    search_city=str(City.get())
    cursor.execute("SELECT * FROM `Registrations` WHERE city='"+ search_city+"'")


    data = cursor.fetchall()
    print(data)
    i = 2
    for display in data:
        for j in range(len(display)):
            a = Entry(DataFrame, width=15, fg='blue')
            a.grid(row=i, column=j)
            a.insert(END, display[j])
        i = i+1


labelName = Label(RegisterFrame, text="City:", bd=18, font=("Comic Sans", 16))
labelName.grid(row=1)

City = Entry(RegisterFrame, textvariable="CITY",
             width=30, font=("Comic Sans", 14))
City.grid(row=1, column=1)

btn = Button(RegisterFrame, text="Search",font=("Comic Sans", 14), command=search)
btn.grid(row=1, column=2)




#top menu

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Register",command=shift_screen)
filemenu.add_command(label="Exit")
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)



#imp function (otherwise it will run in loop)
if __name__ == '__main__':
    root.mainloop()
'''
CREATE TABLE FORM(form_id int(10),form_area char(25),form_type char(25));

INSERT INTO FORM VALUES(100,'East','Registration'); 
INSERT INTO FORM VALUES(200,'West','Registration');
INSERT INTO FORM VALUES(300,'North','Registration',);
INSERT INTO FORM VALUES(400,'South','Registration');

alter table FORM add primary key(form_area);
SELECT *FROM FORM;

GRANT UPDATE ON form_id.FORM TO Admin1;
GRANT ALTER ON form_id.FORM TO User;

REVOKE UPDATE ON  FROM User;
REVOKE CREATE,ALTER ON FROM FROM User;




CREATE TABLE Registration(Name char(30),Age int(10),Gender char(15),Phone int(20),Email varchar(20),City char(30));
INSERT INTO Registration VALUES('Unnati',20,'F',8949632148,'unnati19@gmail.com','Surat');

 alter table Registrations add primary key(City);
SELECT * FROM Registrations;



CREATE TABLE City_search(City_id int(5),foreign key (City) references Registrations(City),foreign key (form_area) references FORM(form_area));
INSERT INTO City_search VALUES(1,'Surat')
SELECT * FROM City_search;
'''
