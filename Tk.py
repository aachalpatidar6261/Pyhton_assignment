# Tkinter is python in-built modele.
# database table - Python-tops > emp(table)
from tkinter import *
import mysql.connector
import tkinter.messagebox as msg

def create_con():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Python_tops"
    )

# print(create_con) # successfully run

def insert():
    if e_name.get()==" " or e_dept.get()==" " or e_salary.get()==" ":
        msg.showinfo("insert status","All fields are mandatory.!")
    else:
        conn=create_con()
        cursor=conn.cursor()
        query="insert into emp(name,dept,salary) values(%s,%s,%s)"
        arg = (e_name.get(),e_dept.get(),e_salary.get())
        cursor.execute(query,arg)
        conn.commit()  # The commit() method is used to make sure the changes made to the database are consistent(continue).
        conn.close()
        e_name.delete(0,"end")
        e_dept.delete(0,"end")
        e_salary.delete(0,"end")
        msg.showinfo(",","Insert Data Successfully..!")

def search():
    if e_id.get()=="":
        msg.showinfo("Search Status","ID is mandatory.!")
    else:
        conn=create_con()
        cursor=conn.cursor()
        query="select * from emp where id=%s"
        arg=(e_id.get(),)   # we gave single argument so is mandatory to add "," in last.
        cursor.execute(query,arg)
        row=cursor.fetchall()
        #print(row)
        if row:
            for i in row:
                e_name.insert(0,i[1])
                e_dept.insert(0,i[2])
                e_salary.insert(0,i[3])
        else:
            msg.showinfo("Search Status","ID Not Found")

        conn.close()


def update():
    if e_id.get()=="" or e_name.get()=="" or e_dept.get()=="" or e_salary.get()=="":
        msg.showinfo("Update Status","All Fields Are Mandatory")
    else:
        conn=create_con()
        cursor=conn.cursor()
        query="update emp set name=%s, dept=%s, salary=%s where id=%s" # the id,name,salary,dept come from database table.
        arg=(e_name.get(),e_dept.get(),e_salary.get(),e_id.get())
        cursor.execute(query,arg)
        conn.commit()
        conn.close()
        #e_id.delete(0,"end")
        e_name.delete(0,"end")
        e_dept.delete(0,"end")
        e_salary.delete(0,"end")
        e_id.delete(0,"end")
        msg.showinfo(",","Updated Are Successfully")


def Delete():
    if e_id.get()=="":
        msg.showinfo("Delete Status","ID is Mandatory")
    else:
        conn=create_con()
        cursor=conn.cursor()
        query="Delete from emp where id=%s"
        arg=(e_id.get(),)
        cursor.execute(query,arg)
        conn.commit()
        conn.close()
        e_id.delete(0,"end")
        e_name.delete(0,"end")
        e_dept.delete(0,"end")
        e_salary.delete(0,"end")
        msg.showinfo(",","Data DELETE Successfully")


root=Tk()
root.title("Desktop Application")
root.geometry("300x390")
root.resizable(width=False,height=False)

l_id=Label(root,text="ID",font=("Algerian",15))
l_id.place(x=50,y=50)

l_name=Label(root,text="NAME",font=("Algerian",15))
l_name.place(x=50,y=100)

l_dept=Label(root,text="Depart.",font=("Algerian",15))
l_dept.place(x=50,y=150)

l_salary=Label(root,text="Salary",font=("Algerian",15))
l_salary.place(x=50,y=200)

e_id=Entry(root)
e_id.place(x=150,y=50)

e_name=Entry(root)
e_name.place(x=150,y=100)

e_dept=Entry(root)
e_dept.place(x=150,y=150)

e_salary=Entry(root)
e_salary.place(x=150,y=200)

insert = Button(root,text="INSERT",font=("algerian",15),bg="Teal",fg="black",command=insert)
insert.place(x=50,y=250)

search = Button(root,text="SEARCH",font=("algerian",15),bg="Teal",fg="black",command=search)
search.place(x=160,y=250)

update = Button(root,text="UPDATE",font=("algerian",15),bg="Teal",fg="black",command=update)
update.place(x=50,y=300)

delete = Button(root,text="DELETE",font=("algerian",15),bg="Teal",fg="black",command=Delete)
delete.place(x=160,y=300)


root.mainloop()  # convert code in exe file by installing - 'pip install pyinstaller' on cmd.