from tkinter import *
from mysql import connector


ab=Tk()
ab.title("registraton form")
ab.geometry('500x500')
ab.configure(background="light pink")
label=Label(ab,text="REGISTRATION FORM",width=30,fg="black",bg="light pink",font="bold").place(x=100,y=60)

def database():
    conn=connector.connect(
        user='root',
        password='Sarb@2001#',
        host='127.0.0.1',
        port='3306',
        database='registration')
    mycursor=conn.cursor()
    mycursor.execute("insert into form1 values(%s,%s,%s,%s,%s,%s)",
        (entry1.get(),entry2.get(),entry3.get(),entry4.get(),c.get(),var.get()))
    
    conn.commit()
a=Label(ab,text="SR.NO.")
a.place(x=80,y=130)
entry1=Entry(ab)
entry1.place(x=200, y=130)
b=Label(ab,text="STUDENT NAME")
b.place(x=80,y=180)
entry2=Entry(ab)
entry2.place(x=200, y=180)
c=Label(ab,text="ROLL NO")
c.place(x=80,y=230)
entry3=Entry(ab)
entry3.place(x=200, y=230)
d=Label(ab,text="ADDRESS")
d.place(x=80,y=280)
entry4=Entry(ab)
entry4.place(x=200, y=280)
a=Label(ab,text="BRANCH")
a.place(x=80,y=330)
list_of_branches=["CSE","IT","ECE","ME","CIVIL"]
c=StringVar()
droplist=OptionMenu(ab,c,*list_of_branches)
droplist.config(width=20)
c.set("SELECT YOUR BRANCH")
droplist.place(x=200,y=330)
e=Label(ab,text="GENDER")
e.place(x=80, y=380)
var=IntVar()
Radiobutton(ab,text="Male",padx=5,variable=var,value=1).place(x=200,y=380)
Radiobutton(ab,text="Female",padx=20,variable=var,value=2).place(x=270,y=380)
b1=Button(ab,text="SUBMIT",fg="white",bg="black",width=20,command=database)
b1.place(x=180,y=430)
ab.mainloop()
