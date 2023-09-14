import mysql.connector as connectr
from tkinter import *                 
from tkinter import ttk               
import tkinter.messagebox
from os import system, name 
from PIL import ImageTk, Image



"""These messegeboxs display the messege written in the quotes.There are two arguments in the paranthesis
1. The first one shoes the heading of the messagebox.
2. The second one will show the message displayed by the messagebox"""


def notfound():         
    nf=tkinter.messagebox.showerror("Not found","Student not found")

def validentries():         
    nf=tkinter.messagebox.showerror("Invalid","All Entries Must be Valid!!")

"""def notvalidroll():         
    nf=tkinter.messagebox.showerror("Invalid","Invalid Roll Number")

def notvalidphn():         
    nf=tkinter.messagebox.showerror("Invalid","Invalid Phone Number")

def notvalidname():
     nf=tkinter.messagebox.showerror("Invalid","Invalid Student Name")

def notvalidfahtername():
    nf=tkinter.messagebox.showerror("Invalid","Invalid Father Name")
     
def notvalidrolphn():
    nf=tkinter.messagebox.showerror("Invalid","Invalid Phone and Roll Number")"""

def notshow():              
    ns=tkinter.messagebox.showwarning("Error","No Record to show")

def notdel():
    ns=tkinter.messagebox.showwarning("Error","No Record to Delete")

def exist():
    ex=tkinter.messagebox.showinfo("Exist","Student already exist")
    
def rolserch():
    cls=tkinter.messagebox.showerror("Entry","Enter the Roll no to search by Roll no")

def namserch():
    cls=tkinter.messagebox.showerror("Entry","Enter the Name to search by Name")

def clserch():
    cls=tkinter.messagebox.showerror("Entry","Enter the Class to search by Class")

def delroll():
    cls=tkinter.messagebox.showerror("Entry","Enter the Roll Number to Delete")

def detroll():
    cls=tkinter.messagebox.showerror("Entry","Enter the Roll Number to Show Details")
    
def enter():
    en=tkinter.messagebox.showerror("Entries","Enter all the information")
    
def Exit():
    Exit=tkinter.messagebox.askyesno("Student Management System","Confirm Do You Want To Exit")
    if Exit>0:
        root.destroy()
        return


def clear():                        #clears the output screen
    global t1
    Exit=tkinter.messagebox.askyesno("Student Management System","Do You Want To Clear The Screen")
    if Exit>0:
        t1.grid_forget()
        t1=Text(root,width=115,height=20)       #This will again create an empty grid as soon as the  output grid is destroyed
        t1.grid(row=10,column=1)
        e1.delete (0, last=len(student_name.get()))
        e2.delete (0, last=len(roll_no.get()))
        e3.current(0)
        e4.delete (0, last=len(phone.get()))
        e5.delete (0, last=len(father.get()))
        e6.delete (0, last=len(address.get()))
        return t1

def grd():
    global t1
    t1=Text(root,width=115,height=20)       #This will again create an empty grid as soon as the  output grid is destroyed
    t1.grid(row=10,column=1)
    return t1
        
def succesfull1():
    s1=tkinter.messagebox.showinfo("Done","Student Added Successfully")

def succesfull2():
    s1=tkinter.messagebox.showinfo("Done","Student Deleted Successfully")

def succesfull3():
    s1=tkinter.messagebox.showinfo("Done","Information Updated Successfully")



def create_window():                #creats a window
    window = tk.Toplevel(root)

   
def connection():                   #connects the program with database
    conn=connectr.connect(host="localhost",user="root", passwd="root", database="lucky")
    if conn.is_connected():
        print()
    else:
        print("cannot connect to the database")
    return conn

def chk():                          #searches for a specified rollnumber in the database 
    conn=connection()
    cur=conn.cursor()               #this statement will set a cursor to wrok on the database same as the file handling
    cur.execute("select ROLL_NO from STUDENTS WHERE ROLL_NO=%s",(str(roll_no.get()),))
    data=cur.fetchall()
    conn.close()
    return data

def chk2():                         #checks if the database is empty
    conn=connection()
    cur=conn.cursor()
    cur.execute("select s.ROLL_NO from STUDENTS s")
    data=cur.fetchall()
    conn.close()
    return data

"""def validate(rollNo, phoneNo, name, father):
    if  rollNo.isdigit() or phoneNo.isdigit() or name.isalpha() or father.isalpha() :
        if not(phoneNo.isdigit()):
            notvalidphn()
            return 1
        elif not(rollNo.isdigit()) :
            notvalidroll()
            return 1
        elif not(name.isalpha()) :
            notvalidname()
            return 1
        elif not(father.isalpha()) :
            notvalidfahtername()
            return 1
    else:
        notvalidrolphn()
        return 1"""

def validate(rollNo, phoneNo, name, father):
    if  not(rollNo.isdigit() and phoneNo.isdigit() and name.isalpha() and father.isalpha()) :
        validentries()
        return 1
    
def verifier():                     #a verifier function to ensure all the details are entered
    a=b=c=d=e=f=0
    if not student_name.get():
        t1.insert(END,"<>Student name is required<>\n")
        a=1
    if not roll_no.get():
        t1.insert(END,"<>Roll no is required<>\n")
        b=1
    if not Class.get():
        t1.insert(END,"<>Class is required<>\n")
        c=1
    if not phone.get():
        t1.insert(END,"<>Phone number is requrired<>\n")
        d=1
    if not father.get():
        t1.insert(END,"<>Father name is required<>\n")
        e=1
    if not address.get():
        t1.insert(END,"<>Address is Required<>\n")
        f=1   
    if a==1 or b==1 or c==1 or d==1 or e==1 or f==1:
        enter()
        return 1
    else:
        return 0

def comentry():
    conn=connection()
    cur=conn.cursor()
    cur.execute("select * from STUDENTS WHERE ROLL_NO=%s",(roll_no.get(),))
    data=cur.fetchall()
    conn.close()
    lst=["","1","2","3","4","5","6","7","8","9","10","11-Science","11-Commerce","12-Science","12-Commerce"]
    for i in data:
        for j in lst:
            if i[2]==j:
                c=lst.index(j)
    return c
                    

def values():
    a=chk2()
    #e7=Entry(root,textvariable=Class)
    #e7.place(x=110,y=64)

    if not a:
        t1.insert(END,"No Record To Show!!!\n")
        notshow()
    else :
        if roll_no.get():
            conn=connection()
            cur=conn.cursor()
            cur.execute("select * from STUDENTS WHERE ROLL_NO=%s",(roll_no.get(),))
            data=cur.fetchall()
            conn.close()
            b=comentry()
            for i in data:
                str(i)
                e1.insert(END,i[0])
                e3.current(b)
                e4.insert(END,i[3])
                e5.insert(END,i[4])
                e6.insert(END,i[5])
            b4=Button(root,text="UPDATE INFO",command=update_student,width=20)
            b4.grid(row=12,column=0)
        else:
            detroll()
            
def add_student():                  #to add details of new student in the database
    grd()
    ret=verifier()
    if chk():
        t1.insert(END,"<>Roll number Already Exist<>\n")
        exist()
    elif ret==0:
        conn=connection()
        cur=conn.cursor()
        a=validate(roll_no.get(), phone.get(), student_name.get(), father.get())
        if not a:
            cur.execute("CREATE TABLE IF NOT EXISTS STUDENTS(NAME TEXT,ROLL_NO TEXT ,Class TEXT,PHONE_NO VARCHAR(20),father_name TEXT,ADDRESS TEXT)")
            cur.execute("insert into STUDENTS values(%s,%s,%s,%s,%s,%s)",(student_name.get(),roll_no.get(),Class.get(),phone.get(),father.get(),address.get()))
            conn.commit()
            conn.close()
            succesfull1()
            t1.insert(END,"ADDED SUCCESSFULLY\n")


def view_student():                 #fetches details  of all students in the database
    grd()
    a=chk2()
    if not a:
        t1.insert(END,"No Record To Show!!!\n")
        notshow()
    else :
        conn=connection()
        cur=conn.cursor()
        cur.execute("select * from STUDENTS")
        data=cur.fetchall()
        conn.close()
        t1.insert(END,"Name\t\t\t Roll NO\t\t  Class\t\t  Phone NO\t\t  Father Name\t\t\t   Address\n")
        for i in data:
            str(i)
            t1.insert(END,"\n")
            out=i[0]+"\t\t\t "+str(i[1])+"\t\t  "+i[2]+"\t\t  "+str(i[3])+"\t\t   "+i[4]+"\t\t\t    "+i[5]+"\n"
            t1.insert(END,out)


def delete_student():               #to delete the details of any student just by entering the roll number
    grd()
    a=chk2()
    if not a:
        t1.insert(END,"No Record To Delete!!!\n")
        notdel()
    else:
        if roll_no.get():
            conn=connection()
            cur=conn.cursor()
            cur.execute("DELETE FROM STUDENTS WHERE ROLL_NO=%s",(str(roll_no.get()),))
            conn.commit()
            conn.close()
            succesfull2()
            t1.insert(END,"SUCCESSFULLY DELETED THE USER\n")
        else:
            delroll()


def update_student():               #to update the info about any student in the database  IMPORTANT:-ALL THE DETAILS OF THE STUDENT MUST BE ENTERED
    grd()
    ret=verifier()
    if ret==0:
        conn=connection()
        cur=conn.cursor()
        cur.execute("UPDATE STUDENTS SET NAME=%s,ROLL_NO=%s,Class=%s,PHONE_NO=%s,father_name=%s,ADDRESS=%s where ROLL_NO=%s",(student_name.get(),str(roll_no.get()),Class.get(),str(phone.get()),father.get(),address.get(),str(roll_no.get())))
        conn.commit()
        conn.close()
        succesfull3()
        t1.insert(END,"UPDATED SUCCESSFULLY\n")
        b4=Button(root,text="DETAILS",command=values,width=20)
        b4.grid(row=12,column=0)
                             


def search():                                                   #to search the deatils of any student by roll number
    grd()
    if not roll_no.get():
        rolserch()
    else:
        conn=connection()
        cur=conn.cursor()
        cur.execute("select * from STUDENTS WHERE ROLL_NO=%s",(roll_no.get(),))
        data=cur.fetchall()
        if data:
            t1.insert(END,"Name\t\t\t Roll NO\t\t  Class\t\t  Phone NO\t\t  Father Name\t\t\t   Address\n")#to search the details of all the students by a common name
            for i in data:
                str(i)
                t1.insert(END,"\n")
                out=i[0]+"\t\t\t "+str(i[1])+"\t\t  "+i[2]+"\t\t  "+str(i[3])+"\t\t   "+i[4]+"\t\t\t    "+i[5]+"\n"
                t1.insert(END,out)
        else:
            t1.insert(END,"Not Found")
            notfound()
        conn.close()


def namesearch():
    grd()
    if not student_name.get():
        namserch()
    else:
        conn=connection()
        cur=conn.cursor()
        cur.execute("select * from STUDENTS WHERE NAME=%s",(student_name.get(),))
        data=cur.fetchall()
        if data:
            t1.insert(END,"Name\t\t\t Roll NO\t\t  Class\t\t  Phone NO\t\t  Father Name\t\t\t   Address\n")
            for i in data:
                str(i)
                t1.insert(END,"\n")
                out=i[0]+"\t\t\t "+str(i[1])+"\t\t  "+i[2]+"\t\t  "+str(i[3])+"\t\t   "+i[4]+"\t\t\t    "+i[5]+"\n"
                t1.insert(END,out)
        else:
            t1.insert(END,"Not Found")
            notfound()
        conn.close()

def scbclss():                                          #a function to search by Class                     
    grd()
    if not Class.get():
        clserch()
    else:
        conn=connection()
        cur=conn.cursor()
        cur.execute("select * from STUDENTS WHERE Class=%s",(Class.get(),))
        data=cur.fetchall()
        if data:
            t1.insert(END,"Name\t\t\t Roll NO\t\t  Class\t\t Phone NO\t\t  Father Name\t\t\t   Address\n")
            for i in data:
                str(i)
                t1.insert(END,"\n")
                out=i[0]+"\t\t\t "+str(i[1])+"\t\t  "+i[2]+"\t\t "+str(i[3])+"\t\t   "+i[4]+"\t\t\t    "+i[5]+"\n"
                t1.insert(END,out)
        else:
            t1.insert(END,"Not Found")
            notfound()
        conn.close()


if __name__=="__main__":
    root=Tk()
    root.title("Birla Shiksha Kendra")
    root.configure(bg="lightsteelblue")
    Tops = Text(root,width=115,height=20, bd=4,bg='white')   #This the the frame just below the output grid to cover the background when the grid will be destroyed.
    Tops.grid(row=10,column=1)                                  
    canvas1 = Canvas(root, width = 220, height = 320)               #This is to obtain the image on it 
    img1 = ImageTk.PhotoImage(Image.open("C:\\Users\\Chirayu Maru\\Desktop\\bsk_250x320.jpg"))
    canvas1.grid(row=10,column=0)
    canvas1.create_image(0, 0, anchor= NW, image=img1)
    
    img2 = ImageTk.PhotoImage(Image.open("C:\\Users\\Chirayu Maru\\Desktop\\bsk_250x320.jpg"))
    canvas2 = Canvas(root, width = 220, height = 320)
    canvas2.grid(row=10,column=2)
    canvas2.create_image(0, 0, anchor=NW, image=img2)
        
#These are the variables which will be used to obtain the input from the user

    student_name=StringVar()
    roll_no=StringVar()
    Class=StringVar()
    phone=StringVar()
    father=StringVar()
    address=StringVar()
    
#These are the labels of the input as the user need to know what information he need to enter in the input.

    label1=Label(root,text="Student name:",bg="white")
    label1.place(x=0,y=4)

    label2=Label(root,text="Roll no:",bg="white")
    label2.place(x=0,y=34)

    label3=Label(root,text="Class:",bg="white")
    label3.place(x=0,y=64)

    label4=Label(root,text="Phone Number:",bg="white")
    label4.place(x=0,y=94)

    label5=Label(root,text="Father Name:",bg="white")
    label5.place(x=0,y=124)

    label6=Label(root,text="Address:",bg="white")
    label6.place(x=0,y=154)

#These are to take the input from the user or this the place where the user will give the input
#The textvariable argument used here gives the name of the variable in which the value is going.

    e1=Entry(root,textvariable=student_name)
    e1.place(x=95,y=4)

    e2=Entry(root,textvariable=roll_no)
    e2.place(x=95,y=34)

    e3=Entry(root,textvariable=Class)
    e3.place(x=95,y=64)
    e3=ttk.Combobox(root, state='readonly',textvariable = Class, width=17)
    e3['value']=('',"1","2","3","4","5","6","7","8","9","10","11-Science","11-Commerce","12-Science","12-Commerce")
    e3.current(0)
    e3.place(x=95,y=64)

    e4=Entry(root,textvariable=phone)
    e4.place(x=95,y=94)
    
    e5=Entry(root,textvariable=father)
    e5.place(x=95,y=124)

    e6=Entry(root,textvariable=address)
    e6.place(x=95,y=154)
    
    t1=Text(root,width=115,height=20)                    #This is the grid used to show the output
    t1.grid(row=10,column=1)
   

    b1=Button(root,text="ADD STUDENT",command=add_student,width=20)
    b1.grid(row=11,column=0)

    b2=Button(root,text="VIEW ALL STUDENTS",command=view_student,width=20)
    b2.grid(row=11,column=1)

    b3=Button(root,text="DELETE STUDENT",command=delete_student,width=20)
    b3.grid(row=11,column=2)

    b4=Button(root,text="DETAILS",command=values,width=20)
    b4.grid(row=12,column=0)
                                                                                    #These are the buttons used to perform the specified task in the argument named command.
    b5=Button(root,text="SEARCH ROLL NO",command=search,width=20)               #The command argument contains the name of the function defined above for the tasks.
    b5.grid(row=12,column=1)

    b6=Button(root,text="CLEAR",command=clear,width=20)
    b6.grid(row=13,column=2)
    
    b7=Button(root,text="CLOSE",command=Exit,width=60)
    b7.grid(row=13,column=1)

    b8=Button(root,text="SEARCH NAME",command=namesearch,width=20)
    b8.grid(row=12,column=2)

    b8=Button(root,text="SEARCH BY CLASS",command=scbclss,width=20)
    b8.grid(row=13,column=0)
    

    root.mainloop()
