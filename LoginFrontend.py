# <---- Importing Libraries ---->
from configparser import ConfigParser
from pathlib import path

import customtkinter as ctk
import matplotlib.pyplot
import pandas as pd
import pymysql as sql
import pyvips
from cryptography.fernet import Fernet
from customtkinter import filedialog
from pwinput import pwinput

# <--- Get Secret Keys from .env ---->

configure = ConfigParser()
print(
    configure.read("config.ini")
)  # reading the config to get a fernet key for encrypting and decrypting the passowords

key = Fernet.generate()
print(key)

fernet = Fernet(configure.get("secret files"))

# <--- Connection setup with mySQL ---->
connection = sql.connect(
    host="localhost", user="root", database="studentdatabase", password=""
)
cursor = connection.cursor()

# <---- setup tkinter app window ---->

app = ctk.CTk()
app.title("Student Management System")
app.geometry("500x400")
app.iconphoto()  # giving a customized icon to the window


# <---- functions starts from here ---->


# ==== login ====
def login():
    # prompts user to ask username and password
    username = input("Enter your Username: ")
    password = pwinput("Enter your password: ")
    # check if the username exists
    cursor.execute(f"select username from users where username='{username}';")
    res = cursor.fetchall()
    if len(res) != 0:
        # check if the password is correct
        cursor.execute(f"select password from users where username='{username}';")
        realpassword = fernet.decrypt(
            cursor.fetchall()[0].decode
        )  # decrypts the password
        if password == realpassword:  # checks the password is matching
            print("Welcome to Student Management system")
            # Now check the role
            cursor.execute(f"select role from users where username='{username}';")
            role = cursor.fetchall[0]
            # returning what role the user has in the database for a seperate dashboard and communicating with the dasboard for certain functions
            if role == "admin":
                return "admin"
            elif role == "teacher":
                return "Teacher"
            else:
                return "Student"
        else:
            print("The given password is incorrect. Please try again")
    else:
        print("Wrong User! Please try again")


# ==== register ====
def register():
    # prompts user to register
    username = input("Enter Username: ")
    password = fernet.encrypt(input("Enter Password:"))
    role = input("Enter your role: ")
    # check if user exists in the database
    cursor.execute(f"select * from users where username={username}")
    res = cursor.fetchall()
    if username not in res:
        cursor.execute(f"insert into users values ('{username}','{password}','{role}')")
        print("User registered sucessfully")
    else:
        # prompting the user that he/she
        print("User already exists! Please login")


# ==== forgot passowrd ====
def forgotpassword():
    print("Hello! This is the guide to change your lost/forgotten password")
    username = input("Enter username: ")
    # checks if the username is in the database or not
    cursor.execute(f"select * from users where username={username}")
    res = cursor.fetchall()
    if len(res) != 0:
        print("The user doesn't exist Please register")
    # if it is, then going forward to changing the password
    else:
        newpass = "Enter new password: "
        confirmpass = "Confirm the password"
        # checking the confirmation is true or not...
        if newpass == confirmpass:
            # encrypts the password and changes it to the database
            fernet.encrypt(newpass)
            cursor.execute(
                f"update table users set password='{newpass}' where username='{username}'"
            )
            connection.commit()
        else:
            print("The passwords doesn't match. Please try again")


# ==== show dashboard ====
def dashboard():
    pass


# ==== add class & subjects =====
def addclass():
    studentclass = int(input("Enter class to add"))
    # check if the class exists
    cursor.execute("Show tables")
    res = cursor.fetchall()
    if studentclass in res:
        print("The class already exists!")
    else:
        # default columns are set as Id, admissionId, Name, Class, Section, RollNo
        cursor.execute(
            f"create table {studentclass}(admissionId int, Name varchar(64), Class int, section varchar(2), rollno int)"
        )
        connection.commit()
        # prompts user how many subjects are there instead of defining it before itself
        amountOfsubjects = int(
            input(
                "Enter amount of subjects which are non optional or non choice based in this class: "
            )
        )
        optionalSubjects = int(
            input("Enter number of subjects which are optional or choice based: ")
        )
        for i in range(0, amountOfsubjects):
            # prompts user to name the subject until the loop ends
            subject = input("Enter Subject Name: ")
            cursor.execute(f"ALTER TABLE {studentclass} ADD {subject} int;")
            connection.commit()
        # stores optional subjects as a seperate column values. where people choose on of it
        # creating a blank list such that values are stored in that
        optionalSubjectlist = []
        for i in range(0, optionalSubjects):
            x = input("Enter How many choices are there(if optional, leave it to 1): ")

            secondlist = []
            # if its not an optional subject, instead a choice based subject the checker will have 2
            if x != 1:
                for i in range(0, x):
                    z = input(f"Enter Choice #{i+1}: ")
                    secondlist.append(z)
            else:
                z = input("Enter the optional subject: ")
                secondlist.append("none", i)
            # adding optional subjects as a list [["Math","Informatics Practices","Physical Education"]]
            optionalSubjectlist.append(secondlist)
            # clearing the list
            secondlist.clear()
        # now optional subjects have some values that we are going to append to the database as optional
        # for i in optionalSubjectlist:
        #    cursor.execute(f"alter table {studentclass} add column ")
        # putting this on hold as of now :))


# ==== add student ====
def addstudent():
    # for now, only the student details will be added and marks will be added later
    studentName = input("Enter Name of the Student: ")
    admissionNo = input("Enter Admission Number: ")
    studentClass = int(input("Enter Class Of the Student: "))
    rollNo = int(input("Enter RollNo "))
    # the rest, like marks and optional subjects will be added in the line as there will be a seperaate function called as addMarks for the teacher....
    # the class is going to be added by teacher


# ==== edit student ====
def editstudent():
    pass


# ==== delete student ====
def deletestudent():
    pass


# ==== promote student/class ====
def promote():
    pass


# ==== show students of certain class ====
def showstudents():
    # prompting class and section
    studentclass = int(input("Enter Class: "))
    studentsection = input("Enter Section: ")
    # naming the table same as class
    tablename = str(studentclass)
    table = pd.read_sql(f"select * from {tablename}")
    print(table)


# ==== show graphs ====
def showgraphs():
    pass


# ==== export to csv ====
def exportcsv():
    pass


# ==== export students id card ====
def exportidcard():
    pass


# <---- Add Elements ---->

# <---- Mainloop the App ---->
app.mainloop()
