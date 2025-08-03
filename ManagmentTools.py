from tkinter import *
from tkinter.messagebox import *
from PIL import Image,ImageTk
from tkinter import ttk
import mysql
import mysql.connector
import datetime
import time
# Database Setup
Main=Tk()
Main.title("Managment Tools")
Main.geometry("1520x750+0+0")
Main.resizable(width=False,height=False)
Main.config(bg="sky Blue")
Main.iconbitmap("./ManagmentToolsImages/ManagmentTools1.ico")
MainBg = PhotoImage(file = "./ManagmentToolsImages/ManagmentTools2.png") 
ImgLabel = Label(Main, image = MainBg) 
ImgLabel.place(x=0,y=0) 
HeadLabel=Label(Main,text="Managment Tools",bg="sky blue",fg="black",font=("Arial Black",50,"bold"),bd=10,relief="ridge")
HeadLabel.place(x=0,y=0,height=110,width=1525)

StudentIdVal=StringVar()
StudentNameVal=StringVar()
StudentCourseVal=StringVar()
StudentRollVal=IntVar()
StudentEmailVal=StringVar()
StudentFeesVal=IntVar()

ProfessorIdVal=StringVar()
ProfessorNameVal=StringVar()
ProfessorCourseVal=StringVar()
ProfessorClassVal=IntVar()
ProfessorEmailVal=StringVar()
ProfessorSalaryVal=IntVar()

DoctorIdVal=StringVar()
DoctorNameVal=StringVar()
DoctorSpecialistVal=StringVar()
DoctorEmailVal=StringVar()
DoctorSalaryVal=IntVar()

def addStd():
    cur.execute("Create Database If Not Exists ManagmentTools")
    cur.execute("use ManagmentTools")
    cur.execute("create table if not exists Student(StdId varchar(20) primary key,StdName varchar(20),StdCourse varchar(20),StdRoll int,StdEmail varchar(20),StdFees int)")
    db.commit()
    print("Data Base And Student Table Both Are Maked")
    id=StudentIdVal.get()
    name=StudentNameVal.get()
    course=StudentCourseVal.get()
    roll=StudentRollVal.get()
    email=StudentEmailVal.get()
    fees=StudentFeesVal.get()
    if(id and name and course and roll and email and fees):
        cur.execute("insert into student(StdId,StdName,StdCourse,StdRoll,StdEmail,StdFees) values('{}','{}','{}',{},'{}',{})".format(id,name,course,roll,email,fees))
        db.commit()
        print("Student Data Inserted Successfully")
        showinfo("Info","Student Data Inserted Successfully")
    else:
        showwarning("Warning","Fill All Fields")

def addPrf():
    cur.execute("Create Database If Not Exists ManagmentTools")
    cur.execute("use ManagmentTools")
    cur.execute("create table if not exists Professor(PrfId varchar(20) primary key,PrfName varchar(20),PrfCourse varchar(20),PrfClasses int,PrfEmail varchar(20),PrfSalary int)")
    db.commit()
    print("Data Base And Professor Table Both Are Maked")
    id=ProfessorIdVal.get()
    name=ProfessorNameVal.get()
    course=ProfessorCourseVal.get()
    classes=ProfessorClassVal.get()
    email=ProfessorEmailVal.get()
    salary=ProfessorSalaryVal.get()
    if(id and name and course and classes and email and salary):
        cur.execute("insert into Professor(PrfId,PrfName,PrfCourse,PrfClasses,PrfEmail,PrfSalary) values('{}','{}','{}',{},'{}',{})".format(id,name,course,classes,email,salary))
        db.commit()
        print("Professor Data Inserted Successfully")
        showinfo("Info","Professor Data Inserted Successfully")
    else:
        showwarning("Warning","Fill All Fields")

def addstudentdetails():
    AddStudentDetails=Toplevel()
    AddStudentDetails.resizable(height=False,width=False)
    AddStudentDetails.geometry("500x650+100+30")
    AddStudentDetails.config(bg="sky blue")
    AddStudentDetails.iconbitmap("./ManagmentToolsImages/CollegeIcon.ico")
    AddStudentLabelDetails=Label(AddStudentDetails,text="Give Student Details Carefully: ",font=("Calibri",20),fg="red",bg="sky blue")
    AddStudentLabelDetails.place(x=50,y=20,height=30,width=400)
    IdLabel=Label(AddStudentDetails,text="Id: ",font=("Calibri",20),bg="sky blue",
    fg="green")
    IdLabel.place(x=20,y=100,height=30,width=100)
    IdEntry=Entry(AddStudentDetails,font=("Happy School",20),fg="black",textvariable=StudentIdVal)
    IdEntry.place(x=170,y=100,height=30,width=300)
    NameLabel=Label(AddStudentDetails,text="Name: ",font=("Calibri",20),bg="sky blue",fg="green")
    NameLabel.place(x=20,y=150,height=30,width=100)
    NameEntry=Entry(AddStudentDetails,font=("Happy School",20),fg="black",textvariable=StudentNameVal)
    NameEntry.place(x=170,y=150,height=30,width=300)
    CourseChckLabel=Label(AddStudentDetails,text="Course: ",font=("Calibri",20),bg="sky blue",fg="green")
    CourseChckLabel.place(x=20,y=200,height=30,width=100)
    CourseChck=ttk.Combobox(AddStudentDetails,values=['BCA','BBA','MCA','MBA','MCA Int.','MBA Int.'],font=("Calibri",20),textvariable=StudentCourseVal)
    CourseChck.place(x=170,y=200,height=30,width=300)
    RollLabel=Label(AddStudentDetails,text="Roll: ",font=("Calibri",20),bg="sky blue",
    fg="green")
    RollLabel.place(x=20,y=250,height=30,width=100)
    RollEntry=Entry(AddStudentDetails,font=("Happy School",20),fg="black",textvariable=StudentRollVal)
    RollEntry.place(x=170,y=250,height=30,width=300)
    EmailLabel=Label(AddStudentDetails,text="Email: ",font=("Calibri",20),bg="sky blue",
    fg="green")
    EmailLabel.place(x=20,y=300,height=30,width=100)
    EmailEntry=Entry(AddStudentDetails,font=("Happy School",20),fg="black",textvariable=StudentEmailVal)
    EmailEntry.place(x=170,y=300,height=30,width=300)
    FeesLabel=Label(AddStudentDetails,text="Fees: ",font=("Calibri",20),bg="sky blue",
    fg="green")
    FeesLabel.place(x=20,y=350,height=30,width=100)
    FeesEntry=Entry(AddStudentDetails,font=("Happy School",20),fg="black",textvariable=StudentFeesVal)
    FeesEntry.place(x=170,y=350,height=30,width=300)
    AddStudentDetailsButton=Button(AddStudentDetails,text="Add",
    font=("Calibri",30),bg="blue",fg="white",command=addStd)
    AddStudentDetailsButton.place(x=180,y=450,height=40,width=150) 

def addprofessordetails():
    AddProfessorDetails=Toplevel()
    AddProfessorDetails.resizable(height=False,width=False)
    AddProfessorDetails.geometry("500x650+100+30")
    AddProfessorDetails.config(bg="sky blue")
    AddProfessorDetails.iconbitmap("./ManagmentToolsImages/CollegeIcon.ico")
    AddProfessorLabelDetails=Label(AddProfessorDetails,text="Give Student Details Carefully: ",font=("Calibri",20),fg="red",bg="sky blue")
    AddProfessorLabelDetails.place(x=50,y=20,height=30,width=400)
    IdLabel=Label(AddProfessorDetails,text="Id: ",font=("Calibri",20),bg="sky blue",
    fg="green")
    IdLabel.place(x=20,y=100,height=30,width=100)
    IdEntry=Entry(AddProfessorDetails,font=("Happy School",20),fg="black",textvariable=ProfessorIdVal)
    IdEntry.place(x=170,y=100,height=30,width=300)
    NameLabel=Label(AddProfessorDetails,text="Name: ",font=("Calibri",20),bg="sky blue",fg="green")
    NameLabel.place(x=20,y=150,height=30,width=100)
    NameEntry=Entry(AddProfessorDetails,font=("Happy School",20),fg="black",textvariable=ProfessorNameVal)
    NameEntry.place(x=170,y=150,height=30,width=300)
    CourseChckLabel=Label(AddProfessorDetails,text="Course: ",font=("Calibri",20),bg="sky blue",fg="green")
    CourseChckLabel.place(x=20,y=200,height=30,width=100)
    CourseChck=ttk.Combobox(AddProfessorDetails,values=['BCA','BBA','MCA','MBA','MCA Int.','MBA Int.'],font=("Calibri",20),textvariable=ProfessorCourseVal)
    CourseChck.place(x=170,y=200,height=30,width=300)
    ClassesLabel=Label(AddProfessorDetails,text="Classes: ",font=("Calibri",20),bg="sky blue",
    fg="green")
    ClassesLabel.place(x=20,y=250,height=30,width=100)
    ClassesEntry=Entry(AddProfessorDetails,font=("Happy School",20),fg="black",textvariable=ProfessorClassVal)
    ClassesEntry.place(x=170,y=250,height=30,width=300)
    EmailLabel=Label(AddProfessorDetails,text="Email: ",font=("Calibri",20),bg="sky blue",
    fg="green")
    EmailLabel.place(x=20,y=300,height=30,width=100)
    EmailEntry=Entry(AddProfessorDetails,font=("Happy School",20),fg="black",textvariable=ProfessorEmailVal)
    EmailEntry.place(x=170,y=300,height=30,width=300)
    SalaryLabel=Label(AddProfessorDetails,text="Salary: ",font=("Calibri",20),bg="sky blue",
    fg="green")
    SalaryLabel.place(x=20,y=350,height=30,width=100)
    SalaryEntry=Entry(AddProfessorDetails,font=("Happy School",20),fg="black",textvariable=ProfessorSalaryVal)
    SalaryEntry.place(x=170,y=350,height=30,width=300)
    AddProfessorDetailsButton=Button(AddProfessorDetails,text="Add",
    font=("Calibri",30),bg="blue",fg="white",command=addPrf)
    AddProfessorDetailsButton.place(x=180,y=450,height=40,width=150) 

def updStd():
    id=StudentIdVal.get()
    cur.execute("use managmenttools")
    cur.execute("select * from student where StdId='{}'".format(id))
    data=cur.fetchone()
    print(data)
    if(data!=None):
        print(data[0])
        name=StudentNameVal.get()
        course=StudentCourseVal.get()
        roll=StudentRollVal.get()
        email=StudentEmailVal.get()
        fees=StudentFeesVal.get()
        if(id and name and course and roll and email and fees):
            cur.execute("update student set StdName='{}',StdCourse='{}',StdRoll={},StdEmail='{}',StdFees={} where StdId='{}'".format(name,course,roll,email,fees,id))
            db.commit()
            print("Student Data Updated Successfully")
            showinfo("Info","Student Data Updated Successfully")
    else:
        showwarning("Warning","Sorry !\nStudent Id Not Present")

def updPrf():
    id=ProfessorIdVal.get()
    cur.execute("use managmenttools")
    cur.execute("select * from professor where PrfId='{}'".format(id))
    data=cur.fetchone()
    print(data)
    if(data!=None):
        print(data[0])
        name=ProfessorNameVal.get()
        course=ProfessorCourseVal.get()
        classes=ProfessorClassVal.get()
        email=ProfessorEmailVal.get()
        salary=ProfessorSalaryVal.get()
        if(id and name and course and classes and email and salary):
            cur.execute("update Professor set PrfName='{}',PrfCourse='{}',PrfClasses={},PrfEmail='{}',PrfSalary={} where PrfId='{}'".format(name,course,classes,email,salary,id))
            db.commit()
            print("Professor Data Updated Successfully")
            showinfo("Info","Professor Data Updated Successfully")
    else:
        showwarning("Warning","Sorry !\nProfessor Id Not Present")

def updatestudentdetails():
    showinfo("Info","All Updation Done With Student ID")
    UpdateStudentDetails=Toplevel()
    UpdateStudentDetails.resizable(height=False,width=False)
    UpdateStudentDetails.geometry("500x650+100+30")
    UpdateStudentDetails.config(bg="sky blue")
    UpdateStudentDetails.iconbitmap("./ManagmentToolsImages/CollegeIcon.ico")
    UpdateStudentLabelDetails=Label(UpdateStudentDetails,text="Update Student Details Carefully: ",font=("Calibri",20),fg="red",bg="sky blue")
    UpdateStudentLabelDetails.place(x=50,y=20,height=30,width=400)
    IdLabel=Label(UpdateStudentDetails,text="Id: ",font=("Calibri",20),bg="sky blue",
    fg="green")
    IdLabel.place(x=20,y=100,height=30,width=100)
    IdEntry=Entry(UpdateStudentDetails,font=("Happy School",20),fg="black",textvariable=StudentIdVal)
    IdEntry.place(x=170,y=100,height=30,width=300)
    NameLabel=Label(UpdateStudentDetails,text="Name: ",font=("Calibri",20),bg="sky blue",fg="green")
    NameLabel.place(x=20,y=150,height=30,width=100)
    NameEntry=Entry(UpdateStudentDetails,font=("Happy School",20),fg="black",textvariable=StudentNameVal)
    NameEntry.place(x=170,y=150,height=30,width=300)
    CourseChckLabel=Label(UpdateStudentDetails,text="Course: ",font=("Calibri",20),bg="sky blue",fg="green")
    CourseChckLabel.place(x=20,y=200,height=30,width=100)
    CourseChck=ttk.Combobox(UpdateStudentDetails,values=['BCA','BBA','MCA','MBA','MCA Int.','MBA Int.'],font=("Calibri",20),textvariable=StudentCourseVal)
    CourseChck.place(x=170,y=200,height=30,width=300)
    RollLabel=Label(UpdateStudentDetails,text="Roll: ",font=("Calibri",20),bg="sky blue",
    fg="green")
    RollLabel.place(x=20,y=250,height=30,width=100)
    RollEntry=Entry(UpdateStudentDetails,font=("Happy School",20),fg="black",textvariable=StudentRollVal)
    RollEntry.place(x=170,y=250,height=30,width=300)
    EmailLabel=Label(UpdateStudentDetails,text="Email: ",font=("Calibri",20),bg="sky blue",
    fg="green")
    EmailLabel.place(x=20,y=300,height=30,width=100)
    EmailEntry=Entry(UpdateStudentDetails,font=("Happy School",20),fg="black",textvariable=StudentEmailVal)
    EmailEntry.place(x=170,y=300,height=30,width=300)
    FeesLabel=Label(UpdateStudentDetails,text="Fees: ",font=("Calibri",20),bg="sky blue",
    fg="green")
    FeesLabel.place(x=20,y=350,height=30,width=100)
    FeesEntry=Entry(UpdateStudentDetails,font=("Happy School",20),fg="black",textvariable=StudentFeesVal)
    FeesEntry.place(x=170,y=350,height=30,width=300)
    UpdateStudentDetailsButton=Button(UpdateStudentDetails,text="Update",
    font=("Calibri",30),bg="blue",fg="white",command=updStd)
    UpdateStudentDetailsButton.place(x=180,y=450,height=40,width=150) 

def updateprofessordetails():
    showinfo("Info","All Updation Done With Professor ID")
    UpdateProfessorDetails=Toplevel()
    UpdateProfessorDetails.resizable(height=False,width=False)
    UpdateProfessorDetails.geometry("500x650+100+30")
    UpdateProfessorDetails.config(bg="sky blue")
    UpdateProfessorDetails.iconbitmap("./ManagmentToolsImages/CollegeIcon.ico")
    UpdateProfessorLabelDetails=Label(UpdateProfessorDetails,text="Give Student Details Carefully: ",font=("Calibri",20),fg="red",bg="sky blue")
    UpdateProfessorLabelDetails.place(x=50,y=20,height=30,width=400)
    IdLabel=Label(UpdateProfessorDetails,text="Id: ",font=("Calibri",20),bg="sky blue",
    fg="green")
    IdLabel.place(x=20,y=100,height=30,width=100)
    IdEntry=Entry(UpdateProfessorDetails,font=("Happy School",20),fg="black",textvariable=ProfessorIdVal)
    IdEntry.place(x=170,y=100,height=30,width=300)
    NameLabel=Label(UpdateProfessorDetails,text="Name: ",font=("Calibri",20),bg="sky blue",fg="green")
    NameLabel.place(x=20,y=150,height=30,width=100)
    NameEntry=Entry(UpdateProfessorDetails,font=("Happy School",20),fg="black",textvariable=ProfessorNameVal)
    NameEntry.place(x=170,y=150,height=30,width=300)
    CourseChckLabel=Label(UpdateProfessorDetails,text="Course: ",font=("Calibri",20),bg="sky blue",fg="green")
    CourseChckLabel.place(x=20,y=200,height=30,width=100)
    CourseChck=ttk.Combobox(UpdateProfessorDetails,values=['BCA','BBA','MCA','MBA','MCA Int.','MBA Int.'],font=("Calibri",20),textvariable=ProfessorCourseVal)
    CourseChck.place(x=170,y=200,height=30,width=300)
    ClassesLabel=Label(UpdateProfessorDetails,text="Classes: ",font=("Calibri",20),bg="sky blue",
    fg="green")
    ClassesLabel.place(x=20,y=250,height=30,width=100)
    ClassesEntry=Entry(UpdateProfessorDetails,font=("Happy School",20),fg="black",textvariable=ProfessorClassVal)
    ClassesEntry.place(x=170,y=250,height=30,width=300)
    EmailLabel=Label(UpdateProfessorDetails,text="Email: ",font=("Calibri",20),bg="sky blue",
    fg="green")
    EmailLabel.place(x=20,y=300,height=30,width=100)
    EmailEntry=Entry(UpdateProfessorDetails,font=("Happy School",20),fg="black",textvariable=ProfessorEmailVal)
    EmailEntry.place(x=170,y=300,height=30,width=300)
    SalaryLabel=Label(UpdateProfessorDetails,text="Salary: ",font=("Calibri",20),bg="sky blue",
    fg="green")
    SalaryLabel.place(x=20,y=350,height=30,width=100)
    SalaryEntry=Entry(UpdateProfessorDetails,font=("Happy School",20),fg="black",textvariable=ProfessorSalaryVal)
    SalaryEntry.place(x=170,y=350,height=30,width=300)
    UpdateProfessorDetailsButton=Button(UpdateProfessorDetails,text="Update",
    font=("Calibri",30),bg="blue",fg="white",command=updPrf)
    UpdateProfessorDetailsButton.place(x=180,y=450,height=40,width=150) 

def addstudent():
    AddStudent=Toplevel()
    AddStudent.resizable(height=False,width=False)
    AddStudent.geometry("1020x550+100+100")
    AddStudent.config(bg="sky blue")
    AddStudent.iconbitmap("./ManagmentToolsImages/CollegeIcon.ico")
    AddStudentLabel=Label(AddStudent,text="Choose An Option To Add: ",font=("Calibri",20),fg="red",bg="sky blue")
    AddStudentLabel.place(x=50,y=100,height=30,width=400)
    AddStudentButton=Button(AddStudent,text="1. Student",bg="blue",fg="white",font=("Calibri",30,"bold"),command=addstudentdetails)
    AddStudentButton.place(x=200,y=200,height=50,width=250)
    AddProfessorButton=Button(AddStudent,text="2. Professor",bg="blue",fg="white",font=("Calibri",30,"bold"),command=addprofessordetails)
    AddProfessorButton.place(x=200,y=350,height=50,width=250)

def updatestudent():
    UpdateStudent=Toplevel()
    UpdateStudent.resizable(height=False,width=False)
    UpdateStudent.geometry("1020x550+100+100")
    UpdateStudent.config(bg="sky blue")
    UpdateStudent.iconbitmap("./ManagmentToolsImages/CollegeIcon.ico")
    UpdateStudentLabel=Label(UpdateStudent,text="Choose An Option To Update: ",font=("Calibri",20),fg="red",bg="sky blue")
    UpdateStudentLabel.place(x=50,y=100,height=30,width=400)
    UpdateStudentButton=Button(UpdateStudent,text="1. Student",bg="blue",fg="white",font=("Calibri",30,"bold"),command=updatestudentdetails)
    UpdateStudentButton.place(x=200,y=200,height=50,width=250)
    UpdateProfessorButton=Button(UpdateStudent,text="2. Professor",bg="blue",fg="white",font=("Calibri",30,"bold"),command=updateprofessordetails)
    UpdateProfessorButton.place(x=200,y=350,height=50,width=250)

def srchprf():
    id=ProfessorIdVal.get()
    cur.execute("use managmenttools")
    cur.execute("select * from professor where PrfId='{}'".format(id))
    data=cur.fetchone()
    print(data)
    if(data!=None):
        showinfo("Info","Professor Id Found\nProfessor Id: "+data[0]+"\nProfessor Name: "+data[1]+"\nProfessor Course: "+data[2]+"\nProfessor Classes: "+str(data[3])+"\nProfessor Email: "+data[4]+"\nProfessor Salary: "+str(data[5]))
    else:
        showwarning("Warning","Sorry !\nProfessor Id Not Found")
    pass

def srchstd():
    id=StudentIdVal.get()
    cur.execute("use managmenttools")
    cur.execute("select * from student where StdId='{}'".format(id))
    data=cur.fetchone()
    print(data)
    if(data!=None):
        showinfo("Info","Student Id Found\nStudent Id: "+data[0]+"\nStudent Name: "+data[1]+"\nStudent Course: "+data[2]+"\nStudent Roll: "+str(data[3])+"\nStudent Email: "+data[4]+"\nStudent Fees Paid: "+str(data[5]))
    else:
        showwarning("Warning","Sorry !\nStudent Id Not Found")

def rmvstd():
    id=StudentIdVal.get()
    cur.execute("use managmenttools")
    cur.execute("select * from student where StdId='{}'".format(id))
    data=cur.fetchone()
    print(data)
    if(data!=None):
         cur.execute("delete from student where StdId='{}'".format(id))
         db.commit()
         showinfo("Info","Student Id Found And Deleted")
    else:
        showwarning("Warning","Sorry !\nStudent Id Not Found")

def rmvprf():
    id=ProfessorIdVal.get()
    cur.execute("use managmenttools")
    cur.execute("select * from professor where PrfId='{}'".format(id))
    data=cur.fetchone()
    print(data)
    if(data!=None):
         cur.execute("delete from professor where PrfId='{}'".format(id))
         db.commit()
         showinfo("Info","Professor Id Found And Deleted")
    else:
        showwarning("Warning","Sorry !\nProfessor Id Not Found")

def searchstudentdetails():
    showinfo("Info","All Searching Done With Student ID")
    SearchStudentDetails=Toplevel()
    SearchStudentDetails.resizable(height=False,width=False)
    SearchStudentDetails.geometry("500x650+100+30")
    SearchStudentDetails.config(bg="sky blue")
    SearchStudentDetails.iconbitmap("./ManagmentToolsImages/CollegeIcon.ico")
    SearchStudentLabelDetails=Label(SearchStudentDetails,text="Give Student Id: ",font=("Calibri",20),fg="red",bg="sky blue")
    SearchStudentLabelDetails.place(x=50,y=20,height=30,width=400)
    IdLabel=Label(SearchStudentDetails,text="Id: ",font=("Calibri",20),bg="sky blue",
    fg="green")
    IdLabel.place(x=20,y=100,height=30,width=100)
    IdEntry=Entry(SearchStudentDetails,font=("Happy School",20),fg="black",textvariable=StudentIdVal)
    IdEntry.place(x=170,y=100,height=30,width=300)
    SearchStudentDetailsButton=Button(SearchStudentDetails,text="Search",
    font=("Calibri",30),bg="blue",fg="white",command=srchstd)
    SearchStudentDetailsButton.place(x=180,y=200,height=40,width=150)

def searchprofessordetails():
    showinfo("Info","All Updation Done With Professor ID")
    SearchProfessorDetails=Toplevel()
    SearchProfessorDetails.resizable(height=False,width=False)
    SearchProfessorDetails.geometry("500x650+100+30")
    SearchProfessorDetails.config(bg="sky blue")
    SearchProfessorDetails.iconbitmap("./ManagmentToolsImages/CollegeIcon.ico")
    SearchProfessorLabelDetails=Label(SearchProfessorDetails,text="Give Professor Id : ",font=("Calibri",20),fg="red",bg="sky blue")
    SearchProfessorLabelDetails.place(x=50,y=20,height=30,width=400)
    IdLabel=Label(SearchProfessorDetails,text="Id: ",font=("Calibri",20),bg="sky blue",
    fg="green")
    IdLabel.place(x=20,y=100,height=30,width=100)
    IdEntry=Entry(SearchProfessorDetails,font=("Happy School",20),fg="black",textvariable=ProfessorIdVal)
    IdEntry.place(x=170,y=100,height=30,width=300)
    SearchProfessorDetailsButton=Button(SearchProfessorDetails,text="Search",
    font=("Calibri",30),bg="blue",fg="white",command=srchprf)
    SearchProfessorDetailsButton.place(x=180,y=200,height=40,width=150)

def removestudentdetails():
    showinfo("Info","All Removing Done With Student ID")
    RemoveStudentDetails=Toplevel()
    RemoveStudentDetails.resizable(height=False,width=False)
    RemoveStudentDetails.geometry("500x650+100+30")
    RemoveStudentDetails.config(bg="sky blue")
    RemoveStudentDetails.iconbitmap("./ManagmentToolsImages/CollegeIcon.ico")
    RemoveStudentLabelDetails=Label(RemoveStudentDetails,text="Give Student Id: ",font=("Calibri",20),fg="red",bg="sky blue")
    RemoveStudentLabelDetails.place(x=50,y=20,height=30,width=400)
    IdLabel=Label(RemoveStudentDetails,text="Id: ",font=("Calibri",20),bg="sky blue",
    fg="green")
    IdLabel.place(x=20,y=100,height=30,width=100)
    IdEntry=Entry(RemoveStudentDetails,font=("Happy School",20),fg="black",textvariable=StudentIdVal)
    IdEntry.place(x=170,y=100,height=30,width=300)
    RemoveStudentDetailsButton=Button(RemoveStudentDetails,text="Remove",
    font=("Calibri",30),bg="blue",fg="white",command=rmvstd)
    RemoveStudentDetailsButton.place(x=180,y=200,height=40,width=150)

def removeprofessordetails(): 
    showinfo("Info","All Removing Done With Professor ID")
    RemoveProfessorDetails=Toplevel()
    RemoveProfessorDetails.resizable(height=False,width=False)
    RemoveProfessorDetails.geometry("500x650+100+30")
    RemoveProfessorDetails.config(bg="sky blue")
    RemoveProfessorDetails.iconbitmap("./ManagmentToolsImages/CollegeIcon.ico")
    RemoveProfessorLabelDetails=Label(RemoveProfessorDetails,text="Give Professor Id: ",font=("Calibri",20),fg="red",bg="sky blue")
    RemoveProfessorLabelDetails.place(x=50,y=20,height=30,width=400)
    IdLabel=Label(RemoveProfessorDetails,text="Id: ",font=("Calibri",20),bg="sky blue",
    fg="green")
    IdLabel.place(x=20,y=100,height=30,width=100)
    IdEntry=Entry(RemoveProfessorDetails,font=("Happy School",20),fg="black",textvariable=ProfessorIdVal)
    IdEntry.place(x=170,y=100,height=30,width=300)
    RemoveProfessorDetailsButton=Button(RemoveProfessorDetails,text="Remove",
    font=("Calibri",30),bg="blue",fg="white",command=rmvprf)
    RemoveProfessorDetailsButton.place(x=180,y=200,height=40,width=150)

def srchcollege():
    SearchStudent=Toplevel()
    SearchStudent.resizable(height=False,width=False)
    SearchStudent.geometry("1020x550+100+100")
    SearchStudent.config(bg="sky blue")
    SearchStudent.iconbitmap("./ManagmentToolsImages/CollegeIcon.ico")
    SearchStudentLabel=Label(SearchStudent,text="Choose An Option To Search: ",font=("Calibri",20),fg="red",bg="sky blue")
    SearchStudentLabel.place(x=50,y=100,height=30,width=400)
    SearchStudentButton=Button(SearchStudent,text="1. Student",bg="blue",fg="white",font=("Calibri",30,"bold"),command=searchstudentdetails)
    SearchStudentButton.place(x=200,y=200,height=50,width=250)
    SearchProfessorButton=Button(SearchStudent,text="2. Professor",bg="blue",fg="white",font=("Calibri",30,"bold"),command=searchprofessordetails)
    SearchProfessorButton.place(x=200,y=350,height=50,width=250)
    
def rmvcollege ():
    Removetudent=Toplevel()
    Removetudent.resizable(height=False,width=False)
    Removetudent.geometry("1020x550+100+100")
    Removetudent.config(bg="sky blue")
    Removetudent.iconbitmap("./ManagmentToolsImages/CollegeIcon.ico")
    RemovetudentLabel=Label(Removetudent,text="Choose An Option To Remove: ",font=("Calibri",20),fg="red",bg="sky blue")
    RemovetudentLabel.place(x=50,y=100,height=30,width=400)
    RemovetudentButton=Button(Removetudent,text="1. Student",bg="blue",fg="white",font=("Calibri",30,"bold"),command=removestudentdetails)
    RemovetudentButton.place(x=200,y=200,height=50,width=250)
    RemoveProfessorButton=Button(Removetudent,text="2. Professor",bg="blue",fg="white",font=("Calibri",30,"bold"),command=removeprofessordetails)
    RemoveProfessorButton.place(x=200,y=350,height=50,width=250)

def college():
    College=Toplevel()
    College.resizable(height=False,width=False)
    College.geometry("1520x750+0+0")
    College.config(bg="sky blue")
    College.iconbitmap("./ManagmentToolsImages/CollegeIcon.ico")
    CollegeHead=Label(College,text="Student Managment System",bg="sky blue",
               font=("Calibri",50,"bold"),bd=10,relief="groove",fg="blue")
    CollegeHead.place(x=0,y=0,height=100,width=1520)
    CollegeAddBtn=Button(College,text="Add",font=("Happy School",30,"bold"),bg="blue",bd=5,fg="white",command=addstudent)
    CollegeAddBtn.place(x=200,y=200,height=50,width=230)
    CollegeUpdateBtn=Button(College,text="Update",font=("Happy School",30,"bold"),bg="blue",bd=5,fg="white",command=updatestudent)
    CollegeUpdateBtn.place(x=200,y=300,height=50,width=230)
    CollegeRemoveBtn=Button(College,text="Remove",font=("Happy School",30,"bold"),bg="blue",bd=5,fg="white",command=rmvcollege)
    CollegeRemoveBtn.place(x=200,y=400,height=50,width=230)
    CollegeSearchBtn=Button(College,text="Search",font=("Happy School",30,"bold"),bg="blue",bd=5,fg="white",command=srchcollege)
    CollegeSearchBtn.place(x=200,y=500,height=50,width=230)

def addDoc():
    cur.execute("use managmenttools")
    cur.execute("create table if not exists Doctor(DocId varchar(20),DocName varchar(20),DocSpe varchar(20),DocEmail varchar(20),DocSal int ,DocJoinDate Date,DocJoinTime varchar(20))")
    db.commit()
    print("Doctor Table Created")
    id=DoctorIdVal.get()
    name=DoctorNameVal.get()
    specialist=DoctorSpecialistVal.get()
    email=DoctorEmailVal.get()
    salary=DoctorSalaryVal.get()
    if(id and name and specialist and email and salary):
        cur.execute("insert into doctor (DocId,DocName,DocSpe,DocEmail,DocSal,DocJoinDate,DocJoinTime) values('{}','{}','{}','{}',{},'{}','{}')".format(id,name,specialist,email,salary,datetime.datetime.now(),time.strftime("%H:%M:%S", time.localtime())))
        db.commit()
        print("Doctor Data Inserted Successfully")
        showinfo("Info","Data Inserted Successfully")
    else:
        showwarning("Warning","First Fill All Fields")

def adddoctordetails():
    AddDoctorDetails=Toplevel()
    AddDoctorDetails.resizable(height=False,width=False)
    AddDoctorDetails.geometry("500x650+100+30")
    AddDoctorDetails.config(bg="sky blue")
    AddDoctorDetails.iconbitmap("./ManagmentToolsImages/CollegeIcon.ico")
    AddDoctorLabelDetails=Label(AddDoctorDetails,text="Give Doctor Details Carefully: ",font=("Calibri",20),fg="red",bg="sky blue")
    AddDoctorLabelDetails.place(x=50,y=20,height=30,width=400)
    IdLabel=Label(AddDoctorDetails,text="Id: ",font=("Calibri",20),bg="sky blue",
    fg="green")
    IdLabel.place(x=20,y=100,height=30,width=100)
    IdEntry=Entry(AddDoctorDetails,font=("Happy School",20),fg="black",textvariable=DoctorIdVal)
    IdEntry.place(x=170,y=100,height=30,width=300)
    NameLabel=Label(AddDoctorDetails,text="Name: ",font=("Calibri",20),bg="sky blue",fg="green")
    NameLabel.place(x=20,y=150,height=30,width=100)
    NameEntry=Entry(AddDoctorDetails,font=("Happy School",20),fg="black",textvariable=DoctorNameVal)
    NameEntry.place(x=170,y=150,height=30,width=300)
    SpecailistLabel=Label(AddDoctorDetails,text="Specailist: ",font=("Calibri",20),bg="sky blue",fg="green")
    SpecailistLabel.place(x=20,y=200,height=30,width=100)
    SpecailistChck=ttk.Combobox(AddDoctorDetails,values=['BCA','BBA','MCA','MBA','MCA Int.','MBA Int.'],font=("Calibri",20),textvariable=DoctorSpecialistVal)
    SpecailistChck.place(x=170,y=200,height=30,width=300)
    EmailLabel=Label(AddDoctorDetails,text="Email: ",font=("Calibri",20),bg="sky blue",
    fg="green")
    EmailLabel.place(x=20,y=250,height=30,width=100)
    EmailEntry=Entry(AddDoctorDetails,font=("Happy School",20),fg="black",textvariable=DoctorEmailVal)
    EmailEntry.place(x=170,y=250,height=30,width=300)
    SalaryLabel=Label(AddDoctorDetails,text="Salary: ",font=("Calibri",20),bg="sky blue",
    fg="green")
    SalaryLabel.place(x=20,y=300,height=30,width=100)
    SalaryEntry=Entry(AddDoctorDetails,font=("Happy School",20),fg="black",textvariable=DoctorSalaryVal)
    SalaryEntry.place(x=170,y=300,height=30,width=300)
    AddDoctorDetailsButton=Button(AddDoctorDetails,text="Add",
    font=("Calibri",30),bg="blue",fg="white",command=addDoc)
    AddDoctorDetailsButton.place(x=180,y=450,height=40,width=150) 

def addpatientdetails():
    pass

def addhospital():
    AddHospital=Toplevel()
    AddHospital.resizable(height=False,width=False)
    AddHospital.geometry("1020x550+100+100")
    AddHospital.config(bg="sky blue")
    AddHospital.iconbitmap("./ManagmentToolsImages/CollegeIcon.ico")
    AddHospitalLabel=Label(AddHospital,text="Choose An Option To Add: ",font=("Calibri",20),fg="red",bg="sky blue")
    AddHospitalLabel.place(x=50,y=100,height=30,width=400)
    AddDoctorButton=Button(AddHospital,text="1. Doctor",bg="blue",fg="white",font=("Calibri",30,"bold"),command=adddoctordetails)
    AddDoctorButton.place(x=200,y=200,height=50,width=250)
    AddPatientButton=Button(AddHospital,text="2. Patient",bg="blue",fg="white",font=("Calibri",30,"bold"),command=addpatientdetails)
    AddPatientButton.place(x=200,y=350,height=50,width=250)

def hospital():
    Hospital=Toplevel()
    Hospital.resizable(height=False,width=False)
    Hospital.geometry("1520x750+0+0")
    Hospital.config(bg="sky blue")
    Hospital.iconbitmap("./ManagmentToolsImages/CollegeIcon.ico")
    HospitalHead=Label(Hospital,text="Hospital Managment System",bg="sky blue",
               font=("Calibri",50,"bold"),bd=10,relief="groove",fg="blue")
    HospitalHead.place(x=0,y=0,height=100,width=1520)
    HospitalAddBtn=Button(Hospital,text="Add",font=("Happy School",30,"bold"),bg="blue",bd=5,fg="white",command=addhospital)
    HospitalAddBtn.place(x=200,y=200,height=50,width=230)
    HospitalUpdateBtn=Button(Hospital,text="Update",font=("Happy School",30,"bold"),bg="blue",bd=5,fg="white")
    HospitalUpdateBtn.place(x=200,y=300,height=50,width=230)
    HospitalRemoveBtn=Button(Hospital,text="Remove",font=("Happy School",30,"bold"),bg="blue",bd=5,fg="white")
    HospitalRemoveBtn.place(x=200,y=400,height=50,width=230)
    HospitalSearchBtn=Button(Hospital,text="Search",font=("Happy School",30,"bold"),bg="blue",bd=5,fg="white")
    HospitalSearchBtn.place(x=200,y=500,height=50,width=230)

def library():
    Library=Toplevel()
    Library.resizable(height=False,width=False)
    Library.geometry("1520x750+0+0")
    Library.config(bg="sky blue")
    Library.iconbitmap("./ManagmentToolsImages/CollegeIcon.ico")
    LibraryHead=Label(Library,text="Library Managment System",bg="sky blue",
               font=("Calibri",50,"bold"),bd=10,relief="groove",fg="blue")
    LibraryHead.place(x=0,y=0,height=100,width=1520)
    LibraryAddBtn=Button(Library,text="Add",font=("Happy School",30,"bold"),bg="blue",bd=5,fg="white")
    LibraryAddBtn.place(x=200,y=200,height=50,width=230)
    LibraryUpdateBtn=Button(Library,text="Update",font=("Happy School",30,"bold"),bg="blue",bd=5,fg="white")
    LibraryUpdateBtn.place(x=200,y=300,height=50,width=230)
    LibraryRemoveBtn=Button(Library,text="Remove",font=("Happy School",30,"bold"),bg="blue",bd=5,fg="white")
    LibraryRemoveBtn.place(x=200,y=400,height=50,width=230)
    LibrarySearchBtn=Button(Library,text="Search",font=("Happy School",30,"bold"),bg="blue",bd=5,fg="white")
    LibrarySearchBtn.place(x=200,y=500,height=50,width=230)

def pharmacy():
    Pharmacy=Toplevel()
    Pharmacy.resizable(height=False,width=False)
    Pharmacy.geometry("1520x750+0+0")
    Pharmacy.config(bg="sky blue")
    Pharmacy.iconbitmap("./ManagmentToolsImages/CollegeIcon.ico")
    PharmacyHead=Label(Pharmacy,text="Pharmacy Managment System",bg="sky blue",
               font=("Calibri",50,"bold"),bd=10,relief="groove",fg="blue")
    PharmacyHead.place(x=0,y=0,height=100,width=1520)
    PharmacyAddBtn=Button(Pharmacy,text="Add",font=("Happy School",30,"bold"),bg="blue",bd=5,fg="white")
    PharmacyAddBtn.place(x=200,y=200,height=50,width=230)
    PharmacyUpdateBtn=Button(Pharmacy,text="Update",font=("Happy School",30,"bold"),bg="blue",bd=5,fg="white")
    PharmacyUpdateBtn.place(x=200,y=300,height=50,width=230)
    PharmacyRemoveBtn=Button(Pharmacy,text="Remove",font=("Happy School",30,"bold"),bg="blue",bd=5,fg="white")
    PharmacyRemoveBtn.place(x=200,y=400,height=50,width=230)
    PharmacySearchBtn=Button(Pharmacy,text="Search",font=("Happy School",30,"bold"),bg="blue",bd=5,fg="white")
    PharmacySearchBtn.place(x=200,y=500,height=50,width=230)

def traffic():
    Traffic=Toplevel()
    Traffic.resizable(height=False,width=False)
    Traffic.geometry("1520x750+0+0")
    Traffic.config(bg="sky blue")
    Traffic.iconbitmap("./ManagmentToolsImages/CollegeIcon.ico")
    TraffiHead=Label(Traffic,text="Traffic Managment System",bg="sky blue",
               font=("Calibri",50,"bold"),bd=10,relief="groove",fg="blue")
    TraffiHead.place(x=0,y=0,height=100,width=1520)
    TrafficAddBtn=Button(Traffic,text="Add",font=("Happy School",30,"bold"),bg="blue",bd=5,fg="white")
    TrafficAddBtn.place(x=200,y=200,height=50,width=230)
    TrafficUpdateBtn=Button(Traffic,text="Update",font=("Happy School",30,"bold"),bg="blue",bd=5,fg="white")
    TrafficUpdateBtn.place(x=200,y=300,height=50,width=230)
    TrafficRemoveBtn=Button(Traffic,text="Remove",font=("Happy School",30,"bold"),bg="blue",bd=5,fg="white")
    TrafficRemoveBtn.place(x=200,y=400,height=50,width=230)
    TrafficSearchBtn=Button(Traffic,text="Search",font=("Happy School",30,"bold"),bg="blue",bd=5,fg="white")
    TrafficSearchBtn.place(x=200,y=500,height=50,width=230)

FirstFrame=LabelFrame(Main,bg="sky blue")
FirstFrame.place(x=50,y=150,height=200,width=200)
FirstImage = Image.open("./ManagmentToolsImages/College.png") 
First_resize_image = FirstImage.resize((250,290))
FirstImage = ImageTk.PhotoImage(First_resize_image)
FirstLabel=Label(FirstFrame,image=FirstImage)
FirstLabel.place(x=0,y=0,height=150,width=200)
FirstButton=Button(FirstFrame,bg="blue",text="College",font=("Calibri",30,"bold"),fg="white",command=college)
FirstButton.place(x=0,y=150,height=45,width=195)

SecondFrame=LabelFrame(Main,bg="sky blue")
SecondFrame.place(x=340,y=150,height=200,width=200)
SecondImage = Image.open("./ManagmentToolsImages/Hospital.png") 
Second_resize_image = SecondImage.resize((220,250))
SecondImage = ImageTk.PhotoImage(Second_resize_image)
SecondLabel=Label(SecondFrame,image=SecondImage)
SecondLabel.place(x=0,y=0,height=150,width=200)
SecondButton=Button(SecondFrame,bg="blue",text="Hospital",font=("Calibri",30,"bold"),fg="white",command=hospital)
SecondButton.place(x=0,y=150,height=45,width=195)

ThirdFrame=LabelFrame(Main,bg="sky blue")
ThirdFrame.place(x=640,y=150,height=200,width=200)
ThirdImage = Image.open("./ManagmentToolsImages/Library.png") 
Third_resize_image = ThirdImage.resize((250,170))
ThirdImage = ImageTk.PhotoImage(Third_resize_image)
ThirdLabel=Label(ThirdFrame,image=ThirdImage)
ThirdLabel.place(x=0,y=0,height=150,width=200)
ThirdButton=Button(ThirdFrame,bg="blue",text="Library",font=("Calibri",30,"bold"),fg="white",command=library)
ThirdButton.place(x=0,y=150,height=45,width=195)

FourthFrame=LabelFrame(Main,bg="sky blue")
FourthFrame.place(x=950,y=150,height=200,width=200)
FourthImage = Image.open("./ManagmentToolsImages/Pharmacy.png") 
Fourth_resize_image = FourthImage.resize((230,250))
FourthImage = ImageTk.PhotoImage(Fourth_resize_image)
FourthLabel=Label(FourthFrame,image=FourthImage)
FourthLabel.place(x=0,y=0,height=150,width=200)
FourthButton=Button(FourthFrame,bg="blue",text="Pharmacy",font=("Calibri",30,"bold"),fg="white",command=pharmacy)
FourthButton.place(x=0,y=150,height=45,width=195)

FifthFrame=LabelFrame(Main,bg="sky blue")
FifthFrame.place(x=1250,y=150,height=200,width=200)
FifthImage = Image.open("./ManagmentToolsImages/Traffic.jpg") 
Fifth_resize_image = FifthImage.resize((300,200))
FifthImage = ImageTk.PhotoImage(Fifth_resize_image)
FifthLabel=Label(FifthFrame,image=FifthImage)
FifthLabel.place(x=0,y=0,height=150,width=200)
FifthButton=Button(FifthFrame,bg="blue",text="Traffic",font=("Calibri",30,"bold"),fg="white",command=traffic)
FifthButton.place(x=0,y=150,height=45,width=195)


Main.mainloop()
