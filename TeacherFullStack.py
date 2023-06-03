##
########! Connecting to the server !########
### ! <-- Connecting to the server and creating necessary tables -->

from time import sleep
import customtkinter as ctk
from tkinter import messagebox


window = ctk.CTk()
window.title("Student Management")
window.geometry("500x400")
window.resizable(False, False)
window.configure()

frame = ctk.CTkFrame(master=window)
dashboardFrame = ctk.CTkFrame(master=window)

frame.tkraise()


def TBackend():
    # ! <-- Globals for easier life -->
    global BetterInput, IsProperName, dataframe, series, IsProperStream, db, con, cur, IsProperFcore, IsProperLang2WOF, IsProperLang2WF, IsProperLang3, IsProperRollNum, sleep, plt, pwinput, system, open_new_tab

    # !  <-- Imports -->
    # ? OS --> For running terminal commands
    from os import system

    # ? Time --> For pausing the program
    from time import sleep

    # ? Web Browser --> For opening dataframe on browser
    from webbrowser import open_new_tab

    # ? Matplotlib --> for plotting a graph
    import matplotlib.pyplot as plt

    # ? Pandas --> for storing data
    from pandas import DataFrame as dataframe
    from pandas import Series as series

    # ? PWInputs --> for inputting passwords
    from pwinput import pwinput

    # ? PyMySQL --> for connecting to MySQL
    from pymysql import connect

    # ? Functions --> for better defaults
    from functions import (
        BetterInput,
        IsProperFcore,
        IsProperLang2WF,
        IsProperLang2WOF,
        IsProperLang3,
        IsProperName,
        IsProperRollNum,
        IsProperStream,
    )

    # ! <-- Connecting to MySQL -->
    db = "studentdatabase"
    con = connect(host="localhost", user="root", password="16computers", database="mysql")
    cur = con.cursor()

    # ! <-- Creating basic Databases and Tables -->
    cur.execute(f"create database if not exists {db}")
    cur.execute(
        f"create table if not exists {db}.teacherDB(user varchar(64) primary key, pass varchar(100))"
    )
    cur.execute(
        f"create table if not exists {db}.allstudents(AdmNum int primary key, name varchar(100), class int, section varchar(10))"
    )

    # ! <-- Creating class tables for MySQL -->
    # ** <-- CAT IS CATEGORY -->
    # ? Grade 1
    cur.execute(
        f"""CREATE TABLE if not exists {db}.catone(AdmNum int primary key, Name VARCHAR(50), Class INT, Section varchar(10), RollNumber INT, Lang2Name VARCHAR(50), English INT, Mathematics INT, Science INT, SocialSciences INT, Lang2 INT, Total INT, Average FLOAT)"""
    )

    # ? Grade 2 - Grade 4
    cur.execute(
        f"""CREATE TABLE if not exists {db}.cattwo(AdmNum int primary key, Name VARCHAR(50), Class INT, Section varchar(10), RollNumber INT, Lang2Name VARCHAR(50), English INT, Mathematics INT, Science INT, SocialSciences INT, Lang2 INT, Computers INT, Total INT, Average FLOAT)"""
    )

    # ? Grade 5 - Grade 8
    cur.execute(
        f"""CREATE TABLE if not exists {db}.catthree(AdmNum int primary key, Name VARCHAR(50), Class INT, Section varchar(10), RollNumber INT, Lang2Name VARCHAR(50), Lang3Name VARCHAR(50), English INT, Mathematics INT, Science INT, SocialSciences INT, Lang2 INT, Lang3 INT, Computers INT, Total INT, Average FLOAT)"""
    )

    # ? Grade 9-10
    cur.execute(
        f"""CREATE TABLE if not exists {db}.catfour(AdmNum int primary key, Name VARCHAR(50), Class INT, Section varchar(10), RollNumber INT, Lang2Name VARCHAR(50), English INT, Mathematics INT, Science INT, SocialSciences INT, Lang2 INT, Total INT, Average FLOAT)"""
    )

    # ? MPC
    cur.execute(
        f"""CREATE TABLE if not exists {db}.catfive(AdmNum int primary key, Name VARCHAR(50), Class INT, Section varchar(10), RollNumber INT, FcoreName VARCHAR(50), English INT, Mathematics INT, Physics INT, Chemistry INT, Fcore INT, Total INT, Average FLOAT)"""
    )

    # ? BiPC
    cur.execute(
        f"""CREATE TABLE if not exists {db}.catsix(AdmNum int primary key, Name VARCHAR(50), Class INT, Section varchar(10), RollNumber INT, FcoreName VARCHAR(50), English INT, Biology INT, Physics INT, Chemistry INT, Fcore INT, Total INT, Average FLOAT)"""
    )

    # ? Commerce
    cur.execute(
        f"""CREATE TABLE if not exists {db}.catseven(AdmNum int primary key, Name VARCHAR(50), Class INT, Section varchar(10), RollNumber INT, FcoreName VARCHAR(50), English INT, Accounts INT, BusinessStudies INT, Economics INT, Fcore INT, Total INT, Average FLOAT)"""
    )

    # ? Humanities
    cur.execute(
        f"""CREATE TABLE if not exists {db}.cateight(AdmNum int primary key, Name VARCHAR(50), Class INT, Section varchar(10), RollNumber INT, FcoreName VARCHAR(50), English INT, History INT, PoliticalSciences INT, Economics INT, Fcore INT, Total INT, Average FLOAT)"""
    )
    con.commit()


### ! <-- If Login is called -->
def LoginUser(User=None, Pass=None, errorlab=None):
    # ? Taking username incase not provided
    if User == None:
        User = input("Please enter the username: ")
    # ? Taking password incase not provided
    if Pass == None:
        Pass = pwinput("Please enter the Password: ")
    # ? Running the login systems
    cur.execute(f'select * from {db}.teacherDB where user="{User}"')
    userFetch = cur.fetchall()
    if len(userFetch) == 0:
        print("Username doesn't exist!")
        messagebox.showwarning('Error', "Username doesn't exist!")
    else:
        if userFetch[0][1] == Pass:
            print("Successful login!")
            dashboardFrame.tkraise()
            dashboardFrame.pack()
        else:
            print("Wrong Password")
            messagebox.showwarning('Error', "Wrong Password!")


### ! <-- If Change Password is called -->
def ChangePass(user: str, Pass: str):
    cur.execute(f'select * from {db}.teacherDB where user="{user}"')
    userFetch = cur.fetchall()[0]
    if len(userFetch) == 0:
        return "Username doesn't exist!"
    else:
        if userFetch[1] == Pass:
            newPass = input("Enter a new password: ")
            confPass = input("Confirm the password: ")
            if newPass == confPass:
                cur.execute(
                    f"update {db}.teacherDB set pass='{newPass}' where user='{userFetch[0]}'"
                )
                con.commit()
        else:
            return "Wrong password"
    print("The password has successfully been changed.")


########! Related to Login !########
### ! <-- If Signup is called -->
def RegisterUser(User=None, Pass=None):
    # ? Taking username incase not provided
    if User == None:
        User = input("Please enter the username: ")
    # ? Taking password incase not provided
    if Pass == None:
        Pass = pwinput("Please enter the Password: ")
    # ? Running the signup system
    cur.execute(f'select * from {db}.teacherDB where user="{User}"')
    userFetch = cur.fetchall()
    if len(userFetch) == 0:
        cur.execute(f'insert into {db}.teacherDB values("{User}", "{Pass}")')
        con.commit()
        print("Successfully created user.")
    else:
        print("This user already exists!")
        LoginUser(User, pwinput("Please enter the password for the user: "))
        print("Login Successful!")


username = ctk.CTkEntry(master=frame, placeholder_text="Enter Username")
username.pack(pady=10, padx=10)

password = ctk.CTkEntry(frame, show="*", placeholder_text="Enter Password")
password.pack(pady=10, padx=10)

login = ctk.CTkButton(
    master=frame,
    command=lambda: LoginUser(username.get(), password.get()),
    text="Login",
)
login.pack(pady=10, padx=10)

signup = ctk.CTkButton(
    master=frame,
    text="Sign Up",
    command=lambda: RegisterUser(username.get(), password.get()),
)
TBackend()
signup.pack(pady=10, padx=10)
frame.pack(pady=20, padx=60, fill="both", expand=True)
window.mainloop()



########! Related to student info !########
# ! <-- Adding students -->
def AddStudent():
    # ? Name
    Name = IsProperName(
        BetterInput("Enter student's name: ", filter="sentence", type=str)
    )
    # ? Admission Number
    AdmNum = BetterInput(f"Enter {Name}'s admission number: ", "+", int)
    while True:
        cur.execute(f"select name from {db}.allstudents where AdmNum={AdmNum}")
        admNumFetch = cur.fetchall()
        try:
            if len(admNumFetch) == 0:
                break
            else:
                raise ValueError
        except:
            print("This admission number already exists")
            AdmNum = BetterInput(f"Enter a valid admission number: ", "+", int)
    # ? Class
    Class = BetterInput(f"Enter {Name}'s class: ", "+", int)

    # ! Categorizing by classes
    if 1 <= Class <= 3:
        # ? Asking for 2nd language name without french
        Lang2Name = IsProperLang2WOF(
            BetterInput(
                f"Enter {Name}'s 2nd language (Hindi, Telugu): ", "sentence", str
            )
        )
    elif Class == 4:
        # ? Asking for 2nd language name with french
        Lang2Name = IsProperLang2WF(
            BetterInput(
                f"Enter {Name}'s 2nd language (Hindi, Telugu, French): ",
                "sentence",
                str,
            )
        )
    elif 5 <= Class <= 8:
        # ? Asking for 2nd language name with french
        Lang2Name = IsProperLang2WF(
            BetterInput(
                f"Enter {Name}'s 2nd language (Hindi, Telugu, French): ",
                "sentence",
                str,
            )
        )
        # ? Asking for 3rd language name
        Lang3Name = IsProperLang3(
            BetterInput(
                f"Enter {Name}'s 3rd language (Sanskrit, Hindi, Telugu, French): ",
                "sentence",
                str,
            ),
            Lang2Name,
        )
    elif 9 <= Class <= 10:
        # ? Asking for 2nd language name with french
        Lang2Name = IsProperLang2WF(
            BetterInput(
                f"Enter {Name}'s 2nd language (Hindi, Telugu, French): ",
                "sentence",
                str,
            )
        )
    elif Class in [11, 12]:
        # ! Categorizing by stream
        Stream = IsProperStream(
            BetterInput(
                f"Enter {Name}'s stream (mpc, bipc, cec, humanities): ", "sentence", str
            )
        )
        # ? Asking for 5th core name
        FcoreName = IsProperFcore(
            BetterInput(
                f"Enter {Name}'s Fcore (Mathematics, Psychology, Informatics Practices, Physical Education, Fine Arts): ",
                "sentence",
            ),
            Stream,
        )
    # ? Section
    Section = BetterInput(f"Enter {Name}'s section: ", "upper", str)
    # ? Roll Number
    RollNum = IsProperRollNum(BetterInput(f"Enter {Name}'s roll number: ", "+", int))
    # ? Inserting data into a main table
    cur.execute(
        f"insert into {db}.allstudents values({AdmNum}, '{Name}', {Class}, '{Section}')"
    )
    # ? Grade one
    if Class == 1:
        cur.execute(
            f"insert into {db}.catone(AdmNum, Name, Class, Section, RollNumber, Lang2Name) values({AdmNum}, '{Name}', {Class}, '{Section}', {RollNum}, '{Lang2Name}')"
        )
    # ? Grade 2 - 4
    elif 2 <= Class <= 4:
        cur.execute(
            f"insert into {db}.cattwo(AdmNum, Name, Class, Section, RollNumber, Lang2Name) values({AdmNum}, '{Name}', {Class}, '{Section}', {RollNum}, '{Lang2Name}')"
        )
    # ? Grade 5 - 8
    elif 5 <= Class <= 8:
        cur.execute(
            f"insert into {db}.catthree(AdmNum, Name, Class, Section, RollNumber, Lang2Name, Lang3Name) values({AdmNum}, '{Name}', {Class}, '{Section}', {RollNum}, '{Lang2Name}', '{Lang3Name}')"
        )
    # ? Grade 9 - 12
    elif 9 <= Class <= 10:
        cur.execute(
            f"insert into {db}.catfour(AdmNum, Name, Class, Section, RollNumber, Lang2Name) values({AdmNum}, '{Name}', {Class}, '{Section}', {RollNum}, '{Lang2Name}')"
        )
    elif 11 <= Class <= 12:
        # ? Math, Physics, Chemistry
        if Stream.lower() == "mpc":
            cur.execute(
                f"insert into {db}.catfive(AdmNum, Name, Class, Section, RollNumber, FcoreName) values({AdmNum}, '{Name}', {Class}, '{Section}', {RollNum}, '{FcoreName}')"
            )
        # ? Biology, Physics, Chemistry
        elif Stream.lower() == "bipc":
            cur.execute(
                f"insert into {db}.catsix(AdmNum, Name, Class, Section, RollNumber, FcoreName) values({AdmNum}, '{Name}', {Class}, '{Section}', {RollNum}, '{FcoreName}')"
            )
        # ? Commerce
        elif Stream.lower() == "cec":
            cur.execute(
                f"insert into {db}.catseven(AdmNum, Name, Class, Section, RollNumber, FcoreName) values({AdmNum}, '{Name}', {Class}, '{Section}', {RollNum}, '{FcoreName}')"
            )
        # ? Humanities
        elif Stream.lower() == "humanities":
            cur.execute(
                f"insert into {db}.cateight(AdmNum, Name, Class, Section, RollNumber, FcoreName) values({AdmNum}, '{Name}', {Class}, '{Section}', {RollNum}, '{FcoreName}')"
            )
    con.commit()
    print(f"{Name} has been successfully added.")


# ! <-- Editing student information -->
def EditStudent():
    # ? Admission Number
    AdmNum = BetterInput(f"Enter admission number of the student: ", "+", int)
    while True:
        cur.execute(f"select class from {db}.allstudents where AdmNum={AdmNum}")
        admNumFetch = cur.fetchall()
        try:
            if len(admNumFetch) == 0:
                raise ValueError
            else:
                break
        except:
            print("This admission number does not exist.")
            AdmNum = BetterInput(f"Enter a valid admission number: ", "+", int)
    # ? Name
    Name = IsProperName(
        BetterInput("Enter new student's name: ", filter="sentence", type=str)
    )

    # ? Old Class
    OldClass = admNumFetch[0][0]
    OldStream = None
    if OldClass in [11, 12]:
        # ? Mathematics, Physics, Chemistry
        cur.execute(f"select * from {db}.catfive where AdmNum={AdmNum}")
        streamFetch = cur.fetchall()
        if len(streamFetch) != 0:
            OldStream = "mpc"
        # ? Biology, Physics, Chemistry
        cur.execute(f"select * from {db}.catsix where AdmNum={AdmNum}")
        streamFetch = cur.fetchall()
        if len(streamFetch) != 0:
            OldStream = "bipc"
        # ? Commerce
        cur.execute(f"select * from {db}.catseven where AdmNum={AdmNum}")
        streamFetch = cur.fetchall()
        if len(streamFetch) != 0:
            OldStream = "cec"
        # ? Humanities
        cur.execute(f"select * from {db}.cateight where AdmNum={AdmNum}")
        streamFetch = cur.fetchall()
        if len(streamFetch) != 0:
            OldStream = "humanities"
    # ? New Class
    NewClass = BetterInput(f"Enter {Name}'s new class: ", "+", int)
    # ? Section
    Section = BetterInput("Enter student's new section: ", "upper", str)
    # ? Roll Number
    RollNum = IsProperRollNum(
        BetterInput("Enter student's new roll number: ", "+", int)
    )
    # ? Updating data in the main table
    cur.execute(
        f"update {db}.allstudents set Name='{Name}', Class={NewClass}, Section='{Section}' where AdmNum={AdmNum}"
    )
    # ! Choosing new subjects
    if 1 <= NewClass <= 3:
        # ? Asking for 2nd language name without french
        Lang2Name = IsProperLang2WOF(
            BetterInput(
                f"Enter {Name}'s new 2nd language (Hindi, Telugu): ",
                "sentence",
                str,
            )
        )
    elif NewClass == 4:
        # ? Asking for 2nd language name with french
        Lang2Name = IsProperLang2WF(
            BetterInput(
                f"Enter {Name}'s new 2nd language (Hindi, Telugu, French): ",
                "sentence",
                str,
            )
        )
    elif 5 <= NewClass <= 8:
        # ? Asking for 2nd language name with french
        Lang2Name = IsProperLang2WF(
            BetterInput(
                f"Enter {Name}'s new 2nd language (Hindi, Telugu, French): ",
                "sentence",
                str,
            )
        )
        # ? Asking for 3rd language name
        Lang3Name = IsProperLang3(
            BetterInput(
                f"Enter {Name}'s new 3rd language (Sanskrit, Hindi, Telugu, French): ",
                "sentence",
                str,
            ),
            Lang2Name,
        )
    elif 9 <= NewClass <= 10:
        # ? Asking for 2nd language name with french
        Lang2Name = IsProperLang2WF(
            BetterInput(
                f"Enter {Name}'s new 2nd language (Hindi, Telugu, French): ",
                "sentence",
                str,
            )
        )
    elif NewClass in [11, 12]:
        # ! Categorizing by stream
        NewStream = IsProperStream(
            BetterInput(
                f"Enter {Name}'s new stream (mpc, bipc, cec, humanities): ",
                "sentence",
                str,
            )
        )
        # ? Asking for 5th core name
        FcoreName = IsProperFcore(
            BetterInput(
                f"Enter {Name}'s new Fcore (Mathematics, Psychology, Informatics Practices, Physical Education, Fine Arts): ",
                "sentence",
            ),
            NewStream,
        )
    # ! If class hasn't changed, not deleting entry in particular category.
    if OldClass == NewClass:
        # ? Grade one
        if OldClass == 1:
            cur.execute(
                f"update {db}.catone set Name='{Name}', Class={OldClass}, Section='{Section}', RollNumber={RollNum}, Lang2Name='{Lang2Name}' where AdmNum={AdmNum};"
            )
        # ? Grade 2 - 4
        elif 2 <= OldClass <= 4:
            cur.execute(
                f"update {db}.cattwo set Name='{Name}', Class={OldClass}, Section='{Section}', RollNumber={RollNum}, Lang2Name='{Lang2Name}' where AdmNum={AdmNum};"
            )
        # ? Grade 5 - 8
        elif 5 <= OldClass <= 8:
            cur.execute(
                f"update {db}.catthree set Name='{Name}', Class={OldClass}, Section='{Section}', RollNumber={RollNum}, Lang2Name='{Lang2Name}', Lang3Name='{Lang3Name}' where AdmNum={AdmNum};"
            )
        # ? Grade 9 - 10
        elif 9 <= OldClass <= 10:
            cur.execute(
                f"update {db}.catfour set Name='{Name}', Class={OldClass}, Section='{Section}', RollNumber={RollNum}, Lang2Name='{Lang2Name}' where AdmNum={AdmNum};"
            )
        elif 11 <= OldClass <= 12:
            if NewStream.lower() == OldStream.lower():
                # ? Math, Physics, Chemistry
                if NewStream.lower() == "mpc":
                    cur.execute(
                        f"update {db}.catfive set Name='{Name}', Class={OldClass}, Section='{Section}', RollNumber={RollNum}, FcoreName='{FcoreName}' where AdmNum={AdmNum};"
                    )
                # ? Biology, Physics, Chemistry
                elif NewStream.lower() == "bipc":
                    cur.execute(
                        f"update {db}.catsix set Name='{Name}', Class={OldClass}, Section='{Section}', RollNumber={RollNum}, FcoreName='{FcoreName}' where AdmNum={AdmNum};"
                    )
                # ? Commerce
                elif NewStream.lower() == "cec":
                    cur.execute(
                        f"update {db}.catseven set Name='{Name}', Class={OldClass}, Section='{Section}', RollNumber={RollNum}, FcoreName='{FcoreName}' where AdmNum={AdmNum};"
                    )
                # ? Humanities
                elif NewStream.lower() == "humanities":
                    cur.execute(
                        f"update {db}.cateight set Name='{Name}', Class={OldClass}, Section='{Section}', RollNumber={RollNum}, FcoreName='{FcoreName}' where AdmNum={AdmNum};"
                    )
            else:
                cur.execute(f"delete from {db}.catfive where AdmNum={AdmNum}")
                cur.execute(f"delete from {db}.catsix where AdmNum={AdmNum}")
                cur.execute(f"delete from {db}.catseven where AdmNum={AdmNum}")
                cur.execute(f"delete from {db}.cateight where AdmNum={AdmNum}")
                if NewStream.lower() == "mpc":
                    cur.execute(
                        f"insert into {db}.catfive(AdmNum, Name, Class, Section, Rollnumber, FcoreName) values({AdmNum}, '{Name}', {NewClass}, '{Section}', {RollNum}, '{FcoreName}')"
                    )
                elif NewStream.lower() == "bipc":
                    cur.execute(
                        f"insert into {db}.catsix(AdmNum, Name, Class, Section, Rollnumber, FcoreName) values({AdmNum}, '{Name}', {NewClass}, '{Section}', {RollNum}, '{FcoreName}')"
                    )
                elif NewStream.lower() == "cec":
                    cur.execute(
                        f"insert into {db}.catseven(AdmNum, Name, Class, Section, Rollnumber, FcoreName) values({AdmNum}, '{Name}', {NewClass}, '{Section}', {RollNum}, '{FcoreName}')"
                    )
                elif NewStream.lower() == "humanities":
                    cur.execute(
                        f"insert into {db}.cateight(AdmNum, Name, Class, Section, Rollnumber, FcoreName) values({AdmNum}, '{Name}', {NewClass}, '{Section}', {RollNum}, '{FcoreName}')"
                    )
        # ! If classes are different, deleting entry and creating new entry in respective category.
    else:
        cur.execute(f"delete from {db}.catone where AdmNum={AdmNum}")
        cur.execute(f"delete from {db}.cattwo where AdmNum={AdmNum}")
        cur.execute(f"delete from {db}.catthree where AdmNum={AdmNum}")
        cur.execute(f"delete from {db}.catfour where AdmNum={AdmNum}")
        cur.execute(f"delete from {db}.catfive where AdmNum={AdmNum}")
        cur.execute(f"delete from {db}.catsix where AdmNum={AdmNum}")
        cur.execute(f"delete from {db}.catseven where AdmNum={AdmNum}")
        cur.execute(f"delete from {db}.cateight where AdmNum={AdmNum}")
        if NewClass == 1:
            cur.execute(
                f"insert into {db}.catone(AdmNum, Name, Class, Section, Rollnumber, Lang2Name) values({AdmNum}, '{Name}', {NewClass}, '{Section}', {RollNum} '{Lang2Name}')"
            )
        elif 2 <= NewClass <= 4:
            cur.execute(
                f"insert into {db}.cattwo(AdmNum, Name, Class, Section, Rollnumber, Lang2Name) values({AdmNum}, '{Name}', {NewClass}, '{Section}', {RollNum}, '{Lang2Name}')"
            )
        elif 5 <= NewClass <= 8:
            cur.execute(
                f"insert into {db}.catthree(AdmNum, Name, Class, Section, Rollnumber, Lang2Name, Lang3Name) values({AdmNum}, '{Name}', {NewClass}, '{Section}', {RollNum}, '{Lang2Name}', '{Lang3Name}')"
            )
        elif 9 <= NewClass <= 10:
            cur.execute(
                f"insert into {db}.catfour(AdmNum, Name, Class, Section, Rollnumber, Lang2Name) values({AdmNum}, '{Name}', {NewClass}, '{Section}', {RollNum}, '{Lang2Name}')"
            )
        elif 11 <= NewClass <= 12:
            if NewStream.lower() == "mpc":
                cur.execute(
                    f"insert into {db}.catfive(AdmNum, Name, Class, Section, Rollnumber, FcoreName) values({AdmNum}, '{Name}', {NewClass}, '{Section}', {RollNum}, '{FcoreName}')"
                )
            elif NewStream.lower() == "bipc":
                cur.execute(
                    f"insert into {db}.catsix(AdmNum, Name, Class, Section, Rollnumber, FcoreName) values({AdmNum}, '{Name}', {NewClass}, '{Section}', {RollNum}, '{FcoreName}')"
                )
            elif NewStream.lower() == "cec":
                cur.execute(
                    f"insert into {db}.catseven(AdmNum, Name, Class, Section, Rollnumber, FcoreName) values({AdmNum}, '{Name}', {NewClass}, '{Section}', {RollNum}, '{FcoreName}')"
                )
            elif NewStream.lower() == "humanities":
                cur.execute(
                    f"insert into {db}.cateight(AdmNum, Name, Class, Section, Rollnumber, FcoreName) values({AdmNum}, '{Name}', {NewClass}, '{Section}', {RollNum}, '{FcoreName}')"
                )
    con.commit()
    print("Data has been successfully changed.")


# ! <-- Removing the student -->
def RemoveStudent():
    AdmNum = BetterInput(f"Enter student's admission number to delete: ", "+", int)
    while True:
        cur.execute(f"select name from {db}.allstudents where AdmNum={AdmNum}")
        admNumFetch = cur.fetchall()
        try:
            if len(admNumFetch) == 0:
                raise ValueError
            else:
                Name = admNumFetch[0][0]
                break
        except:
            print("This admission number doesn't exist")
            exit()
    AreYouSure = BetterInput(
        f"Are you sure you want to delete {Name}'s information? (Yes/No): ",
        type=str,
    ).lower()
    if AreYouSure in ["yes", "y"]:
        cur.execute(f"delete from {db}.allstudents where AdmNum={AdmNum}")
        cur.execute(f"delete from {db}.catone where AdmNum={AdmNum}")
        cur.execute(f"delete from {db}.cattwo where AdmNum={AdmNum}")
        cur.execute(f"delete from {db}.catthree where AdmNum={AdmNum}")
        cur.execute(f"delete from {db}.catfour where AdmNum={AdmNum}")
        cur.execute(f"delete from {db}.catfive where AdmNum={AdmNum}")
        cur.execute(f"delete from {db}.catsix where AdmNum={AdmNum}")
        cur.execute(f"delete from {db}.catseven where AdmNum={AdmNum}")
        cur.execute(f"delete from {db}.cateight where AdmNum={AdmNum}")
        con.commit()
        print("Successfully Deleted!")
    else:
        print("Action cancelled")


########! Related to jarks !########
# ! <-- Adding Marks -->
def AddMarks():
    # ? Admission Number
    AdmNum = BetterInput(f"Enter admission number of student to add marks: ", "+", int)
    while True:
        cur.execute(f"select class from {db}.allstudents where AdmNum={AdmNum}")
        admNumFetch = cur.fetchall()
        try:
            if len(admNumFetch) == 0:
                raise ValueError
            else:
                break
        except:
            print("This admission number does not exist.")
            AdmNum = BetterInput(f"Enter a valid admission number: ", "+", int)
    Class = admNumFetch[0][0]
    if Class == 1:
        English = BetterInput("Enter marks for English: ", "+", int)
        Math = BetterInput("Enter marks for Mathematics: ", "+", int)
        Science = BetterInput("Enter marks for Science: ", "+", int)
        SocialSciences = BetterInput("Enter marks for Social Science: ", "+", int)
        Lang2 = BetterInput("Enter marks for 2nd language: ", "+", int)
        Total = English + Math + Science + SocialSciences + Lang2
        Average = round((Total / 500) * 100, 2)
        cur.execute(
            f"update {db}.catone set English={English}, Mathematics={Math}, Science={Science}, SocialSciences={SocialSciences}, Lang2={Lang2}, Average={Average}, Total = {Total} where AdmNum={AdmNum}"
        )
    elif 2 <= Class <= 4:
        English = BetterInput("Enter marks for English: ", "+", int)
        Math = BetterInput("Enter marks for Mathematics: ", "+", int)
        Science = BetterInput("Enter marks for Science: ", "+", int)
        SocialSciences = BetterInput("Enter marks for Social Science: ", "+", int)
        Lang2 = BetterInput("Enter marks for 2nd language: ", "+", int)
        Computers = BetterInput("Enter marks for Computers: ", "+", int)
        Total = English + Math + Science + SocialSciences + Lang2 + Computers
        Average = round((Total / 600) * 100, 2)
        cur.execute(
            f"update {db}.cattwo set English={English}, Mathematics={Math}, Science={Science}, SocialSciences={SocialSciences}, Lang2={Lang2}, Computers={Computers}, Average={Average}, Total = {Total} where AdmNum={AdmNum}"
        )

    elif 5 <= Class <= 8:
        English = BetterInput("Enter marks for English: ", "+", int)
        Math = BetterInput("Enter marks for Mathematics: ", "+", int)
        Science = BetterInput("Enter marks for Science: ", "+", int)
        SocialSciences = BetterInput("Enter marks for Social Science: ", "+", int)
        Lang2 = BetterInput("Enter marks for 2nd language: ", "+", int)
        Lang3 = BetterInput("Enter marks for 3nd language: ", "+", int)
        Computers = BetterInput("Enter marks for Computers: ", "+", int)
        Total = English + Math + Science + SocialSciences + Lang2 + Lang3 + Computers
        Average = round((Total / 700) * 100, 2)
        cur.execute(
            f"update {db}.catthree set English={English}, Mathematics={Math}, Science={Science}, SocialSciences={SocialSciences}, Lang2={Lang2}, Lang3={Lang3}, Computers={Computers}, Average={Average}, Total = {Total} where AdmNum={AdmNum}"
        )

    elif 9 <= Class <= 10:
        English = BetterInput("Enter marks for English: ", "+", int)
        Math = BetterInput("Enter marks for Mathematics: ", "+", int)
        Science = BetterInput("Enter marks for Science: ", "+", int)
        SocialSciences = BetterInput("Enter marks for Social Science: ", "+", int)
        Lang2 = BetterInput("Enter marks for 2nd language: ", "+", int)
        Total = English + Math + Science + SocialSciences + Lang2
        Average = round((Total / 500) * 100, 2)
        cur.execute(
            f"update {db}.catfour set English={English}, Mathematics={Math}, Science={Science}, SocialSciences={SocialSciences}, Lang2={Lang2}, Average={Average}, Total = {Total} where AdmNum={AdmNum}"
        )

    elif 11 <= Class <= 12:
        # ? Mathematics, Physics, Chemistry
        cur.execute(f"select FcoreName from {db}.catfive where AdmNum={AdmNum}")
        MPCFetch = cur.fetchall()
        if len(MPCFetch) != 0:
            FcoreName = MPCFetch[0][0]
            English = BetterInput("Enter marks for English: ", "+", int)
            Math = BetterInput("Enter marks for Mathematics: ", "+", int)
            Physics = BetterInput("Enter marks for Physics: ", "+", int)
            Chemistry = BetterInput("Enter marks for Chemistry: ", "+", int)
            Fcore = BetterInput(f"Enter marks for {FcoreName}: ", "+", int)
            Total = English + Math + Physics + Chemistry + Fcore
            Average = round((Total / 500) * 100, 2)
            cur.execute(
                f"update {db}.catfive set English={English}, Mathematics={Math}, Physics={Physics}, Chemistry={Chemistry}, Fcore={Fcore}, Average={Average}, Total = {Total} where AdmNum={AdmNum}"
            )

        # ? Biology, Physics, Chemistry
        cur.execute(f"select FcoreName from {db}.catsix where AdmNum={AdmNum}")
        BiPCFetch = cur.fetchall()
        if len(BiPCFetch) != 0:
            FcoreName = BiPCFetch[0][0]
            English = BetterInput("Enter marks for English: ", "+", int)
            Biology = BetterInput("Enter marks for Biology: ", "+", int)
            Physics = BetterInput("Enter marks for Physics: ", "+", int)
            Chemistry = BetterInput("Enter marks for Chemistry: ", "+", int)
            Fcore = BetterInput(f"Enter marks for {FcoreName}: ", "+", int)
            Total = English + Biology + Physics + Chemistry + Fcore
            Average = round((Total / 500) * 100, 2)
            cur.execute(
                f"update {db}.catsix set English={English}, Biology={Biology}, Physics={Physics}, Chemistry={Chemistry}, Fcore={Fcore}, Average={Average}, Total = {Total} where AdmNum={AdmNum}"
            )

        # ? Commerce
        cur.execute(f"select FcoreName from {db}.catseven where AdmNum={AdmNum}")
        CECFetch = cur.fetchall()
        if len(CECFetch) != 0:
            FcoreName = CECFetch[0][0]
            English = BetterInput("Enter marks for English: ", "+", int)
            Accounts = BetterInput("Enter marks for Accounts: ", "+", int)
            BusinessStudies = BetterInput(
                "Enter marks for Business Studies: ", "+", int
            )
            Econ = BetterInput("Enter marks for Economics: ", "+", int)
            Fcore = BetterInput(f"Enter marks for {FcoreName}: ", "+", int)
            Total = English + Accounts + BusinessStudies + Econ + Fcore
            Average = round((Total / 500) * 100, 2)
            cur.execute(
                f"update {db}.catseven set English={English}, Accounts={Accounts}, BusinessStudies={BusinessStudies}, Economics={Econ}, Fcore={Fcore}, Average={Average}, Total = {Total} where AdmNum={AdmNum}"
            )

        # ? Humanities
        cur.execute(f"select FcoreName from {db}.cateight where AdmNum={AdmNum}")
        HumanitiesFetch = cur.fetchall()
        if len(HumanitiesFetch) != 0:
            FcoreName = HumanitiesFetch[0][0]
            English = BetterInput("Enter marks for English: ", "+", int)
            History = BetterInput("Enter marks for History: ", "+", int)
            PolSci = BetterInput("Enter marks for Political Sciences: ", "+", int)
            Econ = BetterInput("Enter marks for Economics: ", "+", int)
            Fcore = BetterInput(f"Enter marks for {FcoreName}: ", "+", int)
            Total = English + History + PolSci + Econ + Fcore
            Average = round((Total / 500) * 100, 2)
            cur.execute(
                f"update {db}.cateight set English={English}, History={History}, PoliticalSciences={PolSci}, Economics={Econ}, Fcore={Fcore}, Average={Average}, Total = {Total} where AdmNum={AdmNum}"
            )
    con.commit()
    print(f"Marks have successfully been added.")


# ! <-- Editing Marks -->
def EditMarks():
    # ? Admission Number
    AdmNum = BetterInput(
        f"Enter admission number of student to change marks: ", "+", int
    )
    while True:
        cur.execute(f"select class from {db}.allstudents where AdmNum={AdmNum}")
        admNumFetch = cur.fetchall()
        try:
            if len(admNumFetch) == 0:
                raise ValueError
            else:
                break
        except:
            print("This admission number does not exist.")
            AdmNum = BetterInput(f"Enter a valid admission number: ", "+", int)
    Class = admNumFetch[0][0]
    if Class == 1:
        English = BetterInput("Enter new marks for English: ", "+", int)
        Math = BetterInput("Enter new marks for Mathematics: ", "+", int)
        Science = BetterInput("Enter new marks for Science: ", "+", int)
        SocialSciences = BetterInput("Enter new marks for Social Science: ", "+", int)
        Lang2 = BetterInput("Enter new marks for 2nd language: ", "+", int)
        Total = English + Math + Science + SocialSciences + Lang2
        Average = (Total / 500) * 100
        cur.execute(
            f"update {db}.catone set English={English}, Mathematics={Math}, Science={Science}, SocialSciences={SocialSciences}, Lang2={Lang2}, Average={Average}, Total = {Total} where AdmNum={AdmNum}"
        )
    elif 2 <= Class <= 4:
        English = BetterInput("Enter new marks for English: ", "+", int)
        Math = BetterInput("Enter new marks for Mathematics: ", "+", int)
        Science = BetterInput("Enter new marks for Science: ", "+", int)
        SocialSciences = BetterInput("Enter new marks for Social Science: ", "+", int)
        Lang2 = BetterInput("Enter new marks for 2nd language: ", "+", int)
        Computers = BetterInput("Enter new marks for Computers: ", "+", int)
        Total = English + Math + Science + SocialSciences + Lang2 + Computers
        Average = (Total / 600) * 100
        cur.execute(
            f"update {db}.cattwo set English={English}, Mathematics={Math}, Science={Science}, SocialSciences={SocialSciences}, Lang2={Lang2}, Computers={Computers}, Average={Average}, Total = {Total} where AdmNum={AdmNum}"
        )

    elif 5 <= Class <= 8:
        English = BetterInput("Enter new marks for English: ", "+", int)
        Math = BetterInput("Enter new marks for Mathematics: ", "+", int)
        Science = BetterInput("Enter new marks for Science: ", "+", int)
        SocialSciences = BetterInput("Enter new marks for Social Science: ", "+", int)
        Lang2 = BetterInput("Enter new marks for 2nd language: ", "+", int)
        Lang3 = BetterInput("Enter new marks for 3nd language: ", "+", int)
        Computers = BetterInput("Enter new marks for Computers: ", "+", int)
        Total = English + Math + Science + SocialSciences + Lang2 + Lang3 + Computers
        Average = (Total / 700) * 100
        cur.execute(
            f"update {db}.catthree set English={English}, Mathematics={Math}, Science={Science}, SocialSciences={SocialSciences}, Lang2={Lang2}, Lang3={Lang3}, Computers={Computers}, Average={Average}, Total = {Total} where AdmNum={AdmNum}"
        )

    elif 9 <= Class <= 10:
        English = BetterInput("Enter new marks for English: ", "+", int)
        Math = BetterInput("Enter new marks for Mathematics: ", "+", int)
        Science = BetterInput("Enter new marks for Science: ", "+", int)
        SocialSciences = BetterInput("Enter new marks for Social Science: ", "+", int)
        Lang2 = BetterInput("Enter new marks for 2nd language: ", "+", int)
        Total = English + Math + Science + SocialSciences + Lang2
        Average = (Total / 500) * 100
        cur.execute(
            f"update {db}.catfour set English={English}, Mathematics={Math}, Science={Science}, SocialSciences={SocialSciences}, Lang2={Lang2}, Average={Average}, Total = {Total} where AdmNum={AdmNum}"
        )

    elif 11 <= Class <= 12:
        # ? Mathematics, Physics, Chemistry
        cur.execute(f"select FcoreName from {db}.catfive where AdmNum={AdmNum}")
        MPCFetch = cur.fetchall()
        if len(MPCFetch) != 0:
            FcoreName = MPCFetch[0][0]
            English = BetterInput("Enter new marks for English: ", "+", int)
            Math = BetterInput("Enter new marks for Mathematics: ", "+", int)
            Physics = BetterInput("Enter new marks for Physics: ", "+", int)
            Chemistry = BetterInput("Enter new marks for Chemistry: ", "+", int)
            Fcore = BetterInput(f"Enter new marks for {FcoreName}: ", "+", int)
            Total = English + Math + Physics + Chemistry + Fcore
            Average = (Total / 500) * 100
            cur.execute(
                f"update {db}.catfive set English={English}, Mathematics={Math}, Physics={Physics}, Chemistry={Chemistry}, Fcore={Fcore}, Average={Average}, Total = {Total} where AdmNum={AdmNum}"
            )

        # ? Biology, Physics, Chemistry
        cur.execute(f"select FcoreName from {db}.catsix where AdmNum={AdmNum}")
        BiPCFetch = cur.fetchall()
        if len(BiPCFetch) != 0:
            FcoreName = BiPCFetch[0][0]
            English = BetterInput("Enter new marks for English: ", "+", int)
            Biology = BetterInput("Enter new marks for Biology: ", "+", int)
            Physics = BetterInput("Enter new marks for Physics: ", "+", int)
            Chemistry = BetterInput("Enter new marks for Chemistry: ", "+", int)
            Fcore = BetterInput(f"Enter new marks for {FcoreName}: ", "+", int)
            Total = English + Biology + Physics + Chemistry + Fcore
            Average = (Total / 500) * 100
            cur.execute(
                f"update {db}.catsix set English={English}, Biology={Biology}, Physics={Physics}, Chemistry={Chemistry}, Fcore={Fcore}, Average={Average}, Total = {Total} where AdmNum={AdmNum}"
            )

        # ? Commerce
        cur.execute(f"select FcoreName from {db}.catseven where AdmNum={AdmNum}")
        CECFetch = cur.fetchall()
        if len(CECFetch) != 0:
            FcoreName = CECFetch[0][0]
            English = BetterInput("Enter new marks for English: ", "+", int)
            Accounts = BetterInput("Enter new marks for Accounts: ", "+", int)
            BusinessStudies = BetterInput(
                "Enter new marks for Business Studies: ", "+", int
            )
            Econ = BetterInput("Enter new marks for Economics: ", "+", int)
            Fcore = BetterInput(f"Enter new marks for {FcoreName}: ", "+", int)
            Total = English + Accounts + BusinessStudies + Econ + Fcore
            Average = (Total / 500) * 100
            cur.execute(
                f"update {db}.catseven set English={English}, Accounts={Accounts}, BusinessStudies={BusinessStudies}, Economics={Econ}, Fcore={Fcore}, Average={Average}, Total = {Total} where AdmNum={AdmNum}"
            )

        # ? Humanities
        cur.execute(f"select FcoreName from {db}.cateight where AdmNum={AdmNum}")
        HumanitiesFetch = cur.fetchall()
        if len(HumanitiesFetch) != 0:
            FcoreName = HumanitiesFetch[0][0]
            English = BetterInput("Enter new marks for English: ", "+", int)
            History = BetterInput("Enter new marks for History: ", "+", int)
            PolSci = BetterInput("Enter new marks for Political Sciences: ", "+", int)
            Econ = BetterInput("Enter new marks for Economics: ", "+", int)
            Fcore = BetterInput(f"Enter new marks for {FcoreName}: ", "+", int)
            Total = English + History + PolSci + Econ + Fcore
            Average = (Total / 500) * 100
            cur.execute(
                f"update {db}.cateight set English={English}, History={History}, PoliticalSciences={PolSci}, Economics={Econ}, Fcore={Fcore}, Average={Average}, Total = {Total} where AdmNum={AdmNum}"
            )
    print("Marks have been successfully changed.")
    con.commit()


# ! <-- Removing Marks -->
def RemoveMarks():
    AdmNum = BetterInput(
        f"Enter admission number of student to remove marks: ", "+", int
    )
    while True:
        cur.execute(f"select name from {db}.allstudents where AdmNum={AdmNum}")
        admNumFetch = cur.fetchall()
        try:
            if len(admNumFetch) == 0:
                raise ValueError
            else:
                Name = admNumFetch[0][0]
                break
        except:
            print("This admission number does not exist.")
            exit()
    AreYouSure = BetterInput(
        f"Are you sure you want to delete the marks of {Name}? (Yes/No): ",
        type=str,
    ).lower()
    if AreYouSure in ["yes", "y"]:
        cur.execute(
            f"update {db}.catone set English=Null, Mathematics=Null, Science=Null, SocialSciences=Null, Lang2=Null, Average=Null, Total=Null where AdmNum={AdmNum}"
        )
        cur.execute(
            f"update {db}.cattwo set English=Null, Mathematics=Null, Science=Null, SocialSciences=Null, Lang2=Null, Computers=Null, Average=Null, Total=Null where AdmNum={AdmNum}"
        )
        cur.execute(
            f"update {db}.catthree set English=Null, Mathematics=Null, Science=Null, SocialSciences=Null, Lang2=Null, Lang3=Null, Computers=Null, Average=Null, Total=Null where AdmNum={AdmNum}"
        )
        cur.execute(
            f"update {db}.catfour set English=Null, Mathematics=Null, Science=Null, SocialSciences=Null, Lang2=Null, Average=Null, Total=Null where AdmNum={AdmNum}"
        )
        cur.execute(
            f"update {db}.catfive set English=Null, Mathematics=Null, Physics=Null, Chemistry=Null, Fcore=Null, Average=Null, Total=Null where AdmNum={AdmNum}"
        )
        cur.execute(
            f"update {db}.catsix set English=Null, Biology=Null, Physics=Null, Chemistry=Null, Fcore=Null, Average=Null, Total=Null where AdmNum={AdmNum}"
        )
        cur.execute(
            f"update {db}.catseven set English=Null, Accounts=Null, BusinessStudies=Null, Economics=Null, Fcore=Null, Average=Null, Total=Null where AdmNum={AdmNum}"
        )
        cur.execute(
            f"update {db}.cateight set English=Null, History=Null, PoliticalSciences=Null, Economics=Null, Fcore=Null, Average=Null, Total=Null where AdmNum={AdmNum}"
        )
        con.commit()
        print("Successfully deleted!")
    else:
        print("Action cancelled")


########! Related to viewing data !########
# ! <-- Showing graph for Marks and Subjects -->
def ShowGraph():
    # ? Admission Number
    AdmNum = BetterInput(f"Enter admission number to view mark statistics: ", "+", int)
    while True:
        cur.execute(f"select class from {db}.allstudents where AdmNum={AdmNum}")
        admNumFetch = cur.fetchall()
        try:
            if len(admNumFetch) == 0:
                raise ValueError
            else:
                break
        except:
            print("This admission number does not exist.")
            AdmNum = BetterInput(f"Enter a valid admission number: ", "+", int)
    Class = admNumFetch[0][0]

    # ? Class 1

    if Class == 1:
        cur.execute(f"select * from {db}.catone where AdmNum={AdmNum}")
        result = cur.fetchall()[0]
        SubMarks = result[4:9]
        name = result[1]
        Subjects = ["English", "Mathematics", "Science", "Social Sciences", "2ndLang"]

    # ? Class 2 - Class 4

    elif 2 <= Class <= 4:
        cur.execute(f"select * from {db}.cattwo where AdmNum={AdmNum}")
        result = cur.fetchall()[0]
        SubMarks = result[4:10]
        name = result[1]
        Subjects = [
            "English",
            "Mathematics",
            "Science",
            "Social Sciences",
            "2ndLang",
            "Computers",
        ]

    # ? Class 5 - Class 8

    elif 5 <= Class <= 8:
        cur.execute(f"select * from {db}.catthree where AdmNum={AdmNum}")
        result = cur.fetchall()[0]
        SubMarks = result[4:11]
        name = result[1]
        Subjects = [
            "English",
            "Mathematics",
            "Science",
            "Social Sciences",
            "2ndLang",
            "3rdLang",
            "Computers",
        ]

    # ? Class 9 to Class 10

    elif 9 <= Class <= 10:
        cur.execute(f"select * from {db}.catfour where AdmNum={AdmNum}")
        result = cur.fetchall()[0]
        SubMarks = result[4:9]
        name = result[1]
        Subjects = ["English", "Mathematics", "Science", "Social Sciences", "2ndLang"]

    elif 11 <= Class <= 12:
        # ? Mathematics, Physics, Chemistry
        cur.execute(f"select * from {db}.catfive where AdmNum = {AdmNum}")
        MPCResult = cur.fetchall()
        if len(MPCResult) != 0:
            MPCResult = MPCResult[0]
            SubMarks = MPCResult[6:11]
            name = MPCResult[1]
            Subjects = ["English", "Mathematics", "Physics", "Chemistry", "5th Core"]

        # ? Biology, Physics, Chemistry
        cur.execute(f"select * from {db}.catsix where AdmNum = {AdmNum}")
        BiPCResult = cur.fetchall()
        if len(BiPCResult) != 0:
            BiPCResult = BiPCResult[0]
            SubMarks = BiPCResult[6:11]
            name = BiPCResult[1]
            Subjects = ["English", "Biology", "Physics", "Chemistry", "5th Core"]

        # ? Commerce
        cur.execute(f"select * from {db}.catseven where AdmNum = {AdmNum}")
        CECResult = cur.fetchall()
        if len(CECResult) != 0:
            CECResult = CECResult[0]
            SubMarks = CECResult[6:11]
            name = CECResult[1]
            Subjects = [
                "English",
                "Accounts",
                "Business Studies",
                "Economics",
                "5th Core",
            ]

        # ? Humanities
        cur.execute(f"select * from {db}.cateight where AdmNum = {AdmNum}")
        HumanitiesResult = cur.fetchall()
        if len(HumanitiesResult) != 0:
            HumanitiesResult = HumanitiesResult[0]
            SubMarks = HumanitiesResult[6:11]
            name = HumanitiesResult[1]
            Subjects = [
                "English",
                "History",
                "Political Sciences",
                "Economics",
                "5th Core",
            ]
    try:
        print("Loading graph", end="\r")
        sleep(0.4)
        print("Loading graph.", end="\r")
        sleep(0.4)
        print("Loading graph..", end="\r")
        sleep(0.4)
        print("Loading graph...")
        sleep(0.4)
        plt.title(f"Name: {name} - Admission Number: {AdmNum}")
        plt.bar(Subjects, SubMarks)
        plt.xlabel("Subjects")
        plt.ylabel("Marks")
        plt.show()

    except:
        print("Marks do not exist.")


# ! <-- Displaying individual student records -->
def StudentRecords():
    # ? Admission Number
    AdmNum = BetterInput(
        f"Enter admission number to view student's records: ", "+", int
    )
    while True:
        cur.execute(f"select class from {db}.allstudents where AdmNum={AdmNum}")
        admNumFetch = cur.fetchall()
        try:
            if len(admNumFetch) == 0:
                raise ValueError
            else:
                break
        except:
            print("This admission number does not exist.")
            AdmNum = BetterInput(f"Enter a valid admission number: ", "+", int)
    Class = admNumFetch[0][0]
    # ? Class 1
    if Class == 1:
        cur.execute(f"select * from {db}.catone where AdmNum={AdmNum}")
        res = cur.fetchall()[0]
        result = {
            "Admission Number": res[0],
            "Name": res[1],
            "Class": res[2],
            "Section": res[3],
            "Roll Number": res[4],
            "2nd Language": res[5],
            "English": res[6],
            "Mathematics": res[7],
            "Science": res[8],
            "Social Sciences": res[9],
            res[5]: res[10],
            "Total": res[11],
            "Average %": res[12],
        }
        if result["English"] == None:
            result = dict(list(result.items())[:6])
            prompt = f"{res[1]}'s details: "
        else:
            prompt = f"{res[1]}'s report card: "

    # ? Class 2 - Class 4
    elif 2 <= Class <= 4:
        cur.execute(f"select * from {db}.cattwo where AdmNum={AdmNum}")
        res = cur.fetchall()[0]
        result = {
            "Admission Number": res[0],
            "Name": res[1],
            "Class": res[2],
            "Section": res[3],
            "Roll Number": res[4],
            "2nd Language": res[5],
            "English": res[6],
            "Mathematics": res[7],
            "Science": res[8],
            "Social Sciences": res[9],
            res[5]: res[10],
            "Computers": res[11],
            "Total": res[12],
            "Average %": res[13],
        }
        if result["English"] == None:
            result = dict(list(result.items())[:6])
            prompt = f"{res[1]}'s details: "
        else:
            prompt = f"{res[1]}'s report card: "
    # ? Class 5 - Class 8
    elif 5 <= Class <= 8:
        cur.execute(f"select * from {db}.catthree where AdmNum={AdmNum}")
        res = cur.fetchall()[0]
        result = {
            "Admission Number": res[0],
            "Name": res[1],
            "Class": res[2],
            "Section": res[3],
            "Roll Number": res[4],
            "2nd Language": res[5],
            "3rd Language": res[6],
            "English": res[7],
            "Mathematics": res[8],
            "Science": res[9],
            "Social Sciences": res[10],
            res[5]: res[11],
            res[6]: res[12],
            "Computers": res[13],
            "Total": res[14],
            "Average %": res[15],
        }
        if result["English"] == None:
            result = dict(list(result.items())[:7])
            prompt = f"{res[1]}'s details: "
        else:
            prompt = f"{res[1]}'s report card: "
    # ? Class 9 & 10
    elif 9 <= Class <= 10:
        cur.execute(f"select * from {db}.catfour where AdmNum={AdmNum}")
        res = cur.fetchall()[0]
        result = {
            "Admission Number": res[0],
            "Name": res[1],
            "Class": res[2],
            "Section": res[3],
            "Roll Number": res[4],
            "2nd Language": res[5],
            "English": res[6],
            "Mathematics": res[7],
            "Science": res[8],
            "Social Sciences": res[9],
            res[5]: res[10],
            "Total": res[11],
            "Average %": res[12],
        }
        if result["English"] == None:
            result = dict(list(result.items())[:6])
            prompt = f"{res[1]}'s details: "
        else:
            prompt = f"{res[1]}'s report card: "
    # ? Class 11 & 12
    elif 11 <= Class <= 12:
        # ? Mathematics, Physics, Chemistry
        cur.execute(f"select * from {db}.catfive where AdmNum={AdmNum}")
        res = cur.fetchall()
        if len(res) != 0:
            res = res[0]
            result = {
                "Admission Number": res[0],
                "Name": res[1],
                "Class": res[2],
                "Section": res[3],
                "Roll Number": res[4],
                "5th Core": res[5],
                "English": res[6],
                "Mathematics": res[7],
                "Physics": res[8],
                "Chemistry": res[9],
                res[5]: res[10],
                "Total": res[11],
                "Average %": res[12],
            }
            if result["English"] == None:
                result = dict(list(result.items())[:6])
                prompt = f"{res[1]}'s details: "
            else:
                prompt = f"{res[1]}'s report card: "
        # ? Biology, Physics, Chemistry
        cur.execute(f"select * from {db}.catsix where AdmNum={AdmNum}")
        res = cur.fetchall()
        if len(res) != 0:
            res = res
            result = {
                "Admission Number": res[0],
                "Name": res[1],
                "Class": res[2],
                "Section": res[3],
                "Roll Number": res[4],
                "5th Core": res[5],
                "English": res[6],
                "Biology": res[7],
                "Physics": res[8],
                "Chemistry": res[9],
                res[5]: res[10],
                "Total": res[11],
                "Average %": res[12],
            }
            if result["English"] == None:
                result = dict(list(result.items())[:6])
                prompt = f"{res[1]}'s details: "
            else:
                prompt = f"{res[1]}'s report card: "
        # ? Commerce
        cur.execute(f"select * from {db}.catseven where AdmNum={AdmNum}")
        res = cur.fetchall()
        if len(res) != 0:
            res = res[0]
            result = {
                "Admission Number": res[0],
                "Name": res[1],
                "Class": res[2],
                "Section": res[3],
                "Roll Number": res[4],
                "5th Core": res[5],
                "English": res[6],
                "Accounts": res[7],
                "Business Studies": res[8],
                "Economics": res[9],
                res[5]: res[10],
                "Total": res[11],
                "Average %": res[12],
            }
            if result["English"] == None:
                result = dict(list(result.items())[:6])
                prompt = f"{res[1]}'s details: "
            else:
                prompt = f"{res[1]}'s report card: "
        # ? Humanities
        cur.execute(f"select * from {db}.cateight where AdmNum={AdmNum}")
        res = cur.fetchall()
        if len(res) != 0:
            res = res[0]
            result = {
                "Admission Number": res[0],
                "Name": res[1],
                "Class": res[2],
                "Section": res[3],
                "Roll Number": res[4],
                "5th Core": res[5],
                "English": res[6],
                "History": res[7],
                "Political Sciences": res[8],
                "Economics": res[9],
                res[5]: res[10],
                "Total": res[11],
                "Average %": res[12],
            }
            if result["English"] == None:
                result = dict(list(result.items())[:6])
                prompt = f"{res[1]}'s details: "
            else:
                prompt = f"{res[1]}'s report card: "

    # ! Displaying Records/Report Card
    system("clear|cls")
    print(prompt)
    print()
    Result = series(result).to_string()
    print(Result)


# ! <-- Displaying one categories records -->
def ClassRecords(Class=None):
    # ? Class for the records
    if Class == None:
        while True:
            try:
                Class = BetterInput(
                    "What class do you want the student records for? ", "+", int
                )
                if 0 > Class or Class > 12:
                    raise ValueError
                break
            except:
                print("Please enter a valid class")
    if Class == 1:
        Grade = 1
    if Class == 2:
        Grade = 2
    if Class == 3:
        Grade = 3
    if Class == 4:
        Grade = 4
    if Class == 5:
        Grade = 5
    if Class == 6:
        Grade = 6
    if Class == 7:
        Grade = 7
    if Class == 8:
        Grade = 8
    if Class == 9:
        Grade = 9
    if Class == 10:
        Grade = 10
    # ? Grade 1
    cur.execute(f"select * from {db}.catone where class={Class}")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        (
            AdmNumList,
            NameList,
            ClassList,
            SectionList,
            RollNumList,
            Lang2NameList,
            EngList,
            MathList,
            ScienceList,
            SocialList,
            Lang2List,
            TotList,
            AvgList,
        ) = (
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
        )
        for i in range(len(res)):
            # ? Adding values to list for dataframe
            AdmNumList.append(res[i][0])
            NameList.append(res[i][1])
            ClassList.append(res[i][2])
            SectionList.append(res[i][3])
            RollNumList.append(res[i][4])
            Lang2NameList.append(res[i][5])
            EngList.append(res[i][6])
            MathList.append(res[i][7])
            ScienceList.append(res[i][8])
            SocialList.append(res[i][9])
            Lang2List.append(res[i][10])
            TotList.append(res[i][11])
            AvgList.append(res[i][12])
        # ? Dataframe Values
        result = {
            "Admission Number": AdmNumList,
            "Name": NameList,
            "Class": ClassList,
            "Section": SectionList,
            "Roll Number": RollNumList,
            "2nd Language Name": Lang2NameList,
            "English": EngList,
            "Mathematics": MathList,
            "Science": ScienceList,
            "Social Sciences": SocialList,
            "2nd Language": Lang2List,
            "Total": TotList,
            "Average %": AvgList,
        }
    else:
        result = {
            "Admission Number": [None],
            "Name": [None],
            "Class": [None],
            "Section": [None],
            "Roll Number": [None],
            "2nd Language Name": [None],
            "English": [None],
            "Mathematics": [None],
            "Science": [None],
            "Social Sciences": [None],
            "2nd Language": [None],
            "Total": [None],
            "Average %": [None],
        }

    # ? Grade 2 to Grade 4
    cur.execute(f"select * from {db}.cattwo where class={Class}")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        (
            AdmNumList,
            NameList,
            ClassList,
            SectionList,
            RollNumList,
            Lang2NameList,
            EngList,
            MathList,
            ScienceList,
            SocialList,
            Lang2List,
            ComputersList,
            TotList,
            AvgList,
        ) = ([], [], [], [], [], [], [], [], [], [], [], [], [], [])
        # ? Adding values to list for dataframe
        for i in range(len(res)):
            AdmNumList.append(res[i][0])
            NameList.append(res[i][1])
            ClassList.append(res[i][2])
            SectionList.append(res[i][3])
            RollNumList.append(res[i][4])
            Lang2NameList.append(res[i][5])
            EngList.append(res[i][6])
            MathList.append(res[i][7])
            ScienceList.append(res[i][8])
            SocialList.append(res[i][9])
            Lang2List.append(res[i][10])
            ComputersList.append(res[i][11])
            TotList.append(res[i][12])
            AvgList.append(res[i][13])
        # ? Dataframe Values
        result = {
            "Admission Number": AdmNumList,
            "Name": NameList,
            "Class": ClassList,
            "Section": SectionList,
            "Roll Number": RollNumList,
            "2nd Language Name": Lang2NameList,
            "English": EngList,
            "Mathematics": MathList,
            "Science": ScienceList,
            "Social Sciences": SocialList,
            "2nd Language": Lang2List,
            "Computers": ComputersList,
            "Total": TotList,
            "Average %": AvgList,
        }
    else:
        result = {
            "Admission Number": [None],
            "Name": [None],
            "Class": [None],
            "Section": [None],
            "Roll Number": [None],
            "2nd Language Name": [None],
            "English": [None],
            "Mathematics": [None],
            "Science": [None],
            "Social Sciences": [None],
            "2nd Language": [None],
            "Computers": [None],
            "Total": [None],
            "Average %": [None],
        }

    # ? Grade 5 - Grade 8
    cur.execute(f"select * from {db}.catthree where class={Class}")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        (
            AdmNumList,
            NameList,
            ClassList,
            SectionList,
            RollNumList,
            Lang2NameList,
            Lang3NameList,
            EngList,
            MathList,
            ScienceList,
            SocialList,
            Lang2List,
            Lang3List,
            ComputersList,
            TotList,
            AvgList,
        ) = ([], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [])
        # ? Adding values to list for dataframe
        for i in range(len(res)):
            AdmNumList.append(res[i][0])
            NameList.append(res[i][1])
            ClassList.append(res[i][2])
            SectionList.append(res[i][3])
            RollNumList.append(res[i][4])
            Lang2NameList.append(res[i][5])
            Lang3NameList.append(res[i][6])
            EngList.append(res[i][7])
            MathList.append(res[i][8])
            ScienceList.append(res[i][9])
            SocialList.append(res[i][10])
            Lang2List.append(res[i][11])
            Lang3List.append(res[i][12])
            ComputersList.append(res[i][13])
            TotList.append(res[i][14])
            AvgList.append(res[i][15])
            # ? Dataframe Values
        result = {
            "Admission Number": AdmNumList,
            "Name": NameList,
            "Class": ClassList,
            "Section": SectionList,
            "Roll Number": RollNumList,
            "2nd Language Name": Lang2NameList,
            "3nd Language Name": Lang3NameList,
            "English": EngList,
            "Mathematics": MathList,
            "Science": ScienceList,
            "Social Sciences": SocialList,
            "2nd Language": Lang2List,
            "3rd Language": Lang3List,
            "Computers": ComputersList,
            "Total": TotList,
            "Average %": AvgList,
        }
    else:
        result = {
            "Admission Number": [None],
            "Name": [None],
            "Class": [None],
            "Section": [None],
            "Roll Number": [None],
            "2nd Language Name": [None],
            "3nd Language Name": [None],
            "English": [None],
            "Mathematics": [None],
            "Science": [None],
            "Social Sciences": [None],
            "2nd Language": [None],
            "3rd Language": [None],
            "Computers": [None],
            "Total": [None],
            "Average %": [None],
        }

    # ? Grade 9 - Grade 10
    cur.execute(f"select * from {db}.catfour where class={Class}")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        (
            AdmNumList,
            NameList,
            ClassList,
            SectionList,
            RollNumList,
            Lang2NameList,
            EngList,
            MathList,
            ScienceList,
            SocialList,
            Lang2List,
            TotList,
            AvgList,
        ) = (
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
        )
        # ? Adding values to list for dataframe
        for i in range(len(res)):
            AdmNumList.append(res[i][0])
            NameList.append(res[i][1])
            ClassList.append(res[i][2])
            SectionList.append(res[i][3])
            RollNumList.append(res[i][4])
            Lang2NameList.append(res[i][5])
            EngList.append(res[i][6])
            MathList.append(res[i][7])
            ScienceList.append(res[i][8])
            SocialList.append(res[i][9])
            Lang2List.append(res[i][10])
            TotList.append(res[i][11])
            AvgList.append(res[i][12])
        # ? Dataframe Values
        result = {
            "Admission Number": AdmNumList,
            "Name": NameList,
            "Class": ClassList,
            "Section": SectionList,
            "Roll Number": RollNumList,
            "2nd Language Name": Lang2NameList,
            "English": EngList,
            "Mathematics": MathList,
            "Science": ScienceList,
            "Social Sciences": SocialList,
            "2nd Language": Lang2List,
            "Total": TotList,
            "Average %": AvgList,
        }
    else:
        result = {
            "Admission Number": [None],
            "Name": [None],
            "Class": [None],
            "Section": [None],
            "Roll Number": [None],
            "2nd Language Name": [None],
            "English": [None],
            "Mathematics": [None],
            "Science": [None],
            "Social Sciences": [None],
            "2nd Language": [None],
            "Total": [None],
            "Average %": [None],
        }

    # ? Mathematics, Physics, Chemistry
    cur.execute(f"select * from {db}.catfive where class={Class}")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        (
            AdmNumList,
            NameList,
            ClassList,
            SectionList,
            RollNumList,
            FcoreNameList,
            EngList,
            MathList,
            PhysicsList,
            ChemistryList,
            FcoreList,
            TotList,
            AvgList,
        ) = (
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
        )
        for i in range(len(res)):
            AdmNumList.append(res[i][0])
            NameList.append(res[i][1])
            ClassList.append(res[i][2])
            SectionList.append(res[i][3])
            RollNumList.append(res[i][4])
            FcoreNameList.append(res[i][5])
            EngList.append(res[i][6])
            MathList.append(res[i][7])
            PhysicsList.append(res[i][8])
            ChemistryList.append(res[i][9])
            FcoreList.append(res[i][10])
            TotList.append(res[i][11])
            AvgList.append(res[i][12])
        MPCResult = {
            "Admission Number": AdmNumList,
            "Name": NameList,
            "Class": ClassList,
            "Section": SectionList,
            "Roll Number": RollNumList,
            "5th Core Name": FcoreNameList,
            "English": EngList,
            "Mathematics": MathList,
            "Physics": PhysicsList,
            "Chemistry": ChemistryList,
            "5th Core": FcoreList,
            "Total": TotList,
            "Average %": AvgList,
        }
    else:
        MPCResult = {
            "Admission Number": [None],
            "Name": [None],
            "Class": [None],
            "Section": [None],
            "Roll Number": [None],
            "5th Core Name": [None],
            "English": [None],
            "Maths": [None],
            "Physics": [None],
            "Chemistry": [None],
            "5th Core": [None],
            "Total": [None],
            "Average %": [None],
        }

    # ? Biology, Physics, Chemistry
    cur.execute(f"select * from {db}.catsix where class={Class}")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        (
            AdmNumList,
            NameList,
            ClassList,
            SectionList,
            RollNumList,
            FcoreNameList,
            EngList,
            BioList,
            PhysicsList,
            ChemistryList,
            FcoreList,
            TotList,
            AvgList,
        ) = (
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
        )
        for i in range(len(res)):
            AdmNumList.append(res[i][0])
            NameList.append(res[i][1])
            ClassList.append(res[i][2])
            SectionList.append(res[i][3])
            RollNumList.append(res[i][4])
            FcoreNameList.append(res[i][5])
            EngList.append(res[i][6])
            BioList.append(res[i][7])
            PhysicsList.append(res[i][8])
            ChemistryList.append(res[i][9])
            FcoreList.append(res[i][10])
            TotList.append(res[i][11])
            AvgList.append(res[i][12])
        BiPCResult = {
            "Admission Number": AdmNumList,
            "Name": NameList,
            "Class": ClassList,
            "Section": SectionList,
            "Roll Number": RollNumList,
            "5th Core Name": FcoreNameList,
            "English": EngList,
            "Biology": BioList,
            "Physics": PhysicsList,
            "Chemistry": ChemistryList,
            "5th Core": FcoreList,
            "Total": TotList,
            "Average %": AvgList,
        }
    else:
        BiPCResult = {
            "Admission Number": [None],
            "Name": [None],
            "Class": [None],
            "Section": [None],
            "Roll Number": [None],
            "5th Core Name": [None],
            "English": [None],
            "Biology": [None],
            "Physics": [None],
            "Chemistry": [None],
            "5th Core": [None],
            "Total": [None],
            "Average %": [None],
        }

    # ? Commerce
    cur.execute(f"select * from {db}.catseven where class={Class}")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        (
            AdmNumList,
            NameList,
            ClassList,
            SectionList,
            RollNumList,
            FcoreNameList,
            EngList,
            AccountsList,
            BStList,
            EconList,
            FcoreList,
            TotList,
            AvgList,
        ) = (
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
        )
        for i in range(len(res)):
            AdmNumList.append(res[i][0])
            NameList.append(res[i][1])
            ClassList.append(res[i][2])
            SectionList.append(res[i][3])
            RollNumList.append(res[i][4])
            FcoreNameList.append(res[i][5])
            EngList.append(res[i][6])
            AccountsList.append(res[i][7])
            BStList.append(res[i][8])
            EconList.append(res[i][9])
            FcoreList.append(res[i][10])
            TotList.append(res[i][11])
            AvgList.append(res[i][12])
        CommerceResult = {
            "Admission Number": AdmNumList,
            "Name": NameList,
            "Class": ClassList,
            "Section": SectionList,
            "Roll Number": RollNumList,
            "5th Core Name": FcoreNameList,
            "English": EngList,
            "Accounts": AccountsList,
            "Business Studies": BStList,
            "Economics": EconList,
            "5th Core": FcoreList,
            "Total": TotList,
            "Average %": AvgList,
        }
    else:
        CommerceResult = {
            "Admission Number": [None],
            "Name": [None],
            "Class": [None],
            "Section": [None],
            "Roll Number": [None],
            "5th Core Name": [None],
            "English": [None],
            "Accounts": [None],
            "Business Studies": [None],
            "Economics": [None],
            "5th Core": [None],
            "Total": [None],
            "Average %": [None],
        }

    # ? Humanities
    cur.execute(f"select * from {db}.cateight where class={Class}")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        (
            AdmNumList,
            NameList,
            ClassList,
            SectionList,
            RollNumList,
            FcoreNameList,
            EngList,
            HistoryList,
            PolSciList,
            EconList,
            FcoreList,
            TotList,
            AvgList,
        ) = (
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
        )
        for i in range(len(res)):
            AdmNumList.append(res[i][0])
            NameList.append(res[i][1])
            ClassList.append(res[i][2])
            SectionList.append(res[i][3])
            RollNumList.append(res[i][4])
            FcoreNameList.append(res[i][5])
            EngList.append(res[i][6])
            HistoryList.append(res[i][7])
            PolSciList.append(res[i][8])
            EconList.append(res[i][9])
            FcoreList.append(res[i][10])
            TotList.append(res[i][11])
            AvgList.append(res[i][12])
        HumanitiesResult = {
            "Admission Number": AdmNumList,
            "Name": NameList,
            "Class": ClassList,
            "Section": SectionList,
            "Roll Number": RollNumList,
            "5th Core Name": FcoreNameList,
            "English": EngList,
            "History": HistoryList,
            "Political Sciences": PolSciList,
            "Economics": EconList,
            "5th Core": FcoreList,
            "Total": TotList,
            "Average %": AvgList,
        }
    else:
        HumanitiesResult = {
            "Admission Number": [None],
            "Name": [None],
            "Class": [None],
            "Section": [None],
            "Roll Number": [None],
            "5th Core Name": [None],
            "English": [None],
            "History": [None],
            "Political Sciences": [None],
            "Economics": [None],
            "5th Core": [None],
            "Total": [None],
            "Average %": [None],
        }

    # ? Uploading the dataframe to web browser
    if Class in [11, 12]:
        # ? For class 11 and 12 creating 4 different dataframes
        # ? MPC
        df1 = dataframe(MPCResult)
        print(df1)
        # ? BiPC
        df2 = dataframe(BiPCResult)
        # ? Commerce
        df3 = dataframe(CommerceResult)
        # ? Humanities
        df4 = dataframe(HumanitiesResult)

        # ? Uploading code
        with open(f"Class {Class} Record.html", "w") as f:
            f.write(
                '<head><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous"></head>'
            )
            f.write(
                "<h5 class='text-center fw-bolder'>Maths, Physics, Chemistry: </h5>"
            )
            f.write(
                "<style>@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500&display=swap'); body{padding:50px 20px;font-family:'JetBrains Mono',sans-serif!important;} table{margin:auto; margin-bottom:20px;width:175vh!important;} tr{border-bottom:1px solid #000;} th,tr,td{text-align:center!important;} table {border-collapse: separate; border-spacing: 10px 0;} td {padding: 10px 0;} table td + td, th + th{ border-left:1px solid #000; } table { border-collapse:collapse; } table thead tr { border-bottom: 1px solid #000; } </style>"
            )
            df1.to_html(f, index=False)
        with open(f"Class {Class} Record.html", "a") as f:
            f.write(
                "<h5 class='text-center fw-bolder'>Biology, Physics, Chemistry: </h5>"
            )
            df2.to_html(f, index=False)
        with open(f"Class {Class} Record.html", "a") as f:
            f.write("<h5 class='text-center fw-bolder'>Commerce: </h5>")
            df3.to_html(f, index=False)
        with open(f"Class {Class} Record.html", "a") as f:
            f.write("<h5 class='text-center fw-bolder'>Humanities: </h5>")
            df4.to_html(f, index=False)

        filename = f"Class {Class} Record.html"
        open_new_tab(filename)
    else:
        # ? For the other classes creating 1 dataframe
        try:
            df = dataframe(result)
        except:
            print("Data for this class is not available.")
        with open(f"Class {Grade} Record.html", "w") as f:
            f.write(f"<h5 class='text-center fw-bolder'>Grade {Grade}: </h5>")
            f.write(
                '<head><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous"></head>'
            )
            f.write(
                "<style>@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500&display=swap'); body{padding:50px 20px;font-family:'JetBrains Mono',sans-serif!important;} table{margin:auto; margin-bottom:20px;width:175vh!important;} tr{border-bottom:1px solid #000;} th,tr,td{text-align:center!important;} table {border-collapse: separate; border-spacing: 10px 0;} td {padding: 10px 0;} table td + td, th + th{ border-left:1px solid #000; } table { border-collapse:collapse; } table thead tr { border-bottom: 1px solid #000; } </style>"
            )
            df.to_html(f, index=False)

        filename = f"Class {Grade} Record.html"
        open_new_tab(filename)


# ! <-- Displaying all students in the school -->
def SchoolRecords():
    # ? Grade 1
    cur.execute(f"select * from {db}.catone where class=1")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        (
            AdmNumList,
            NameList,
            ClassList,
            SectionList,
            RollNumList,
            Lang2NameList,
            EngList,
            MathList,
            ScienceList,
            SocialList,
            Lang2List,
            TotList,
            AvgList,
        ) = (
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
        )
        for i in range(len(res)):
            # ? Adding values to list for dataframe
            AdmNumList.append(res[i][0])
            NameList.append(res[i][1])
            ClassList.append(res[i][2])
            SectionList.append(res[i][3])
            RollNumList.append(res[i][4])
            Lang2NameList.append(res[i][5])
            EngList.append(res[i][6])
            MathList.append(res[i][7])
            ScienceList.append(res[i][8])
            SocialList.append(res[i][9])
            Lang2List.append(res[i][10])
            TotList.append(res[i][11])
            AvgList.append(res[i][12])
        # ? Dataframe Values
        result1 = {
            "Admission Number": AdmNumList,
            "Name": NameList,
            "Class": ClassList,
            "Section": SectionList,
            "Roll Number": RollNumList,
            "2nd Language Name": Lang2NameList,
            "English": EngList,
            "Mathematics": MathList,
            "Science": ScienceList,
            "Social Sciences": SocialList,
            "2nd Language": Lang2List,
            "Total": TotList,
            "Average %": AvgList,
        }
    else:
        result1 = {
            "Admission Number": [None],
            "Name": [None],
            "Class": [None],
            "Section": [None],
            "Roll Number": [None],
            "2nd Language Name": [None],
            "English": [None],
            "Mathematics": [None],
            "Science": [None],
            "Social Sciences": [None],
            "2nd Language": [None],
            "Total": [None],
            "Average %": [None],
        }

    # ? Grade 2 to Grade 4
    cur.execute(f"select * from {db}.cattwo where class=2")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        (
            AdmNumList,
            NameList,
            ClassList,
            SectionList,
            RollNumList,
            Lang2NameList,
            EngList,
            MathList,
            ScienceList,
            SocialList,
            Lang2List,
            ComputersList,
            TotList,
            AvgList,
        ) = ([], [], [], [], [], [], [], [], [], [], [], [], [], [])
        # ? Adding values to list for dataframe
        for i in range(len(res)):
            AdmNumList.append(res[i][0])
            NameList.append(res[i][1])
            ClassList.append(res[i][2])
            SectionList.append(res[i][3])
            RollNumList.append(res[i][4])
            Lang2NameList.append(res[i][5])
            EngList.append(res[i][6])
            MathList.append(res[i][7])
            ScienceList.append(res[i][8])
            SocialList.append(res[i][9])
            Lang2List.append(res[i][10])
            ComputersList.append(res[i][11])
            TotList.append(res[i][12])
            AvgList.append(res[i][13])
        # ? Dataframe Values
        result2 = {
            "Admission Number": AdmNumList,
            "Name": NameList,
            "Class": ClassList,
            "Section": SectionList,
            "Roll Number": RollNumList,
            "2nd Language Name": Lang2NameList,
            "English": EngList,
            "Mathematics": MathList,
            "Science": ScienceList,
            "Social Sciences": SocialList,
            "2nd Language": Lang2List,
            "Computers": ComputersList,
            "Total": TotList,
            "Average %": AvgList,
        }
    else:
        result2 = {
            "Admission Number": [None],
            "Name": [None],
            "Class": [None],
            "Section": [None],
            "Roll Number": [None],
            "2nd Language Name": [None],
            "English": [None],
            "Mathematics": [None],
            "Science": [None],
            "Social Sciences": [None],
            "2nd Language": [None],
            "Computers": [None],
            "Total": [None],
            "Average %": [None],
        }

    # ? Grade 3
    cur.execute(f"select * from {db}.cattwo where class=3")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        (
            AdmNumList,
            NameList,
            ClassList,
            SectionList,
            RollNumList,
            Lang2NameList,
            EngList,
            MathList,
            ScienceList,
            SocialList,
            Lang2List,
            ComputersList,
            TotList,
            AvgList,
        ) = ([], [], [], [], [], [], [], [], [], [], [], [], [], [])
        # ? Adding values to list for dataframe
        for i in range(len(res)):
            AdmNumList.append(res[i][0])
            NameList.append(res[i][1])
            ClassList.append(res[i][2])
            SectionList.append(res[i][3])
            RollNumList.append(res[i][4])
            Lang2NameList.append(res[i][5])
            EngList.append(res[i][6])
            MathList.append(res[i][7])
            ScienceList.append(res[i][8])
            SocialList.append(res[i][9])
            Lang2List.append(res[i][10])
            ComputersList.append(res[i][11])
            TotList.append(res[i][12])
            AvgList.append(res[i][13])
        # ? Dataframe Values
        result3 = {
            "Admission Number": AdmNumList,
            "Name": NameList,
            "Class": ClassList,
            "Section": SectionList,
            "Roll Number": RollNumList,
            "2nd Language Name": Lang2NameList,
            "English": EngList,
            "Mathematics": MathList,
            "Science": ScienceList,
            "Social Sciences": SocialList,
            "2nd Language": Lang2List,
            "Computers": ComputersList,
            "Total": TotList,
            "Average %": AvgList,
        }
    else:
        result3 = {
            "Admission Number": [None],
            "Name": [None],
            "Class": [None],
            "Section": [None],
            "Roll Number": [None],
            "2nd Language Name": [None],
            "English": [None],
            "Mathematics": [None],
            "Science": [None],
            "Social Sciences": [None],
            "2nd Language": [None],
            "Computers": [None],
            "Total": [None],
            "Average %": [None],
        }

    # ? Grade 4
    cur.execute(f"select * from {db}.cattwo where class=4")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        (
            AdmNumList,
            NameList,
            ClassList,
            SectionList,
            RollNumList,
            Lang2NameList,
            EngList,
            MathList,
            ScienceList,
            SocialList,
            Lang2List,
            ComputersList,
            TotList,
            AvgList,
        ) = ([], [], [], [], [], [], [], [], [], [], [], [], [], [])
        # ? Adding values to list for dataframe
        for i in range(len(res)):
            AdmNumList.append(res[i][0])
            NameList.append(res[i][1])
            ClassList.append(res[i][2])
            SectionList.append(res[i][3])
            RollNumList.append(res[i][4])
            Lang2NameList.append(res[i][5])
            EngList.append(res[i][6])
            MathList.append(res[i][7])
            ScienceList.append(res[i][8])
            SocialList.append(res[i][9])
            Lang2List.append(res[i][10])
            ComputersList.append(res[i][11])
            TotList.append(res[i][12])
            AvgList.append(res[i][13])
        # ? Dataframe Values
        result4 = {
            "Admission Number": AdmNumList,
            "Name": NameList,
            "Class": ClassList,
            "Section": SectionList,
            "Roll Number": RollNumList,
            "2nd Language Name": Lang2NameList,
            "English": EngList,
            "Mathematics": MathList,
            "Science": ScienceList,
            "Social Sciences": SocialList,
            "2nd Language": Lang2List,
            "Computers": ComputersList,
            "Total": TotList,
            "Average %": AvgList,
        }
    else:
        result4 = {
            "Admission Number": [None],
            "Name": [None],
            "Class": [None],
            "Section": [None],
            "Roll Number": [None],
            "2nd Language Name": [None],
            "English": [None],
            "Mathematics": [None],
            "Science": [None],
            "Social Sciences": [None],
            "2nd Language": [None],
            "Computers": [None],
            "Total": [None],
            "Average %": [None],
        }

    # ? Grade 5
    cur.execute(f"select * from {db}.catthree where class=5")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        (
            AdmNumList,
            NameList,
            ClassList,
            SectionList,
            RollNumList,
            Lang2NameList,
            Lang3NameList,
            EngList,
            MathList,
            ScienceList,
            SocialList,
            Lang2List,
            Lang3List,
            ComputersList,
            TotList,
            AvgList,
        ) = ([], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [])
        # ? Adding values to list for dataframe
        for i in range(len(res)):
            AdmNumList.append(res[i][0])
            NameList.append(res[i][1])
            ClassList.append(res[i][2])
            SectionList.append(res[i][3])
            RollNumList.append(res[i][4])
            Lang2NameList.append(res[i][5])
            Lang3NameList.append(res[i][6])
            EngList.append(res[i][7])
            MathList.append(res[i][8])
            ScienceList.append(res[i][9])
            SocialList.append(res[i][10])
            Lang2List.append(res[i][11])
            Lang3List.append(res[i][12])
            ComputersList.append(res[i][13])
            TotList.append(res[i][14])
            AvgList.append(res[i][15])
            # ? Dataframe Values
        result5 = {
            "Admission Number": AdmNumList,
            "Name": NameList,
            "Class": ClassList,
            "Section": SectionList,
            "Roll Number": RollNumList,
            "2nd Language Name": Lang2NameList,
            "3nd Language Name": Lang3NameList,
            "English": EngList,
            "Mathematics": MathList,
            "Science": ScienceList,
            "Social Sciences": SocialList,
            "2nd Language": Lang2List,
            "3rd Language": Lang3List,
            "Computers": ComputersList,
            "Total": TotList,
            "Average %": AvgList,
        }
    else:
        result5 = {
            "Admission Number": [None],
            "Name": [None],
            "Class": [None],
            "Section": [None],
            "Roll Number": [None],
            "2nd Language Name": [None],
            "3nd Language Name": [None],
            "English": [None],
            "Mathematics": [None],
            "Science": [None],
            "Social Sciences": [None],
            "2nd Language": [None],
            "3rd Language": [None],
            "Computers": [None],
            "Total": [None],
            "Average %": [None],
        }

    # ? Grade 6
    cur.execute(f"select * from {db}.catthree where class=6")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        (
            AdmNumList,
            NameList,
            ClassList,
            SectionList,
            RollNumList,
            Lang2NameList,
            Lang3NameList,
            EngList,
            MathList,
            ScienceList,
            SocialList,
            Lang2List,
            Lang3List,
            ComputersList,
            TotList,
            AvgList,
        ) = ([], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [])
        # ? Adding values to list for dataframe
        for i in range(len(res)):
            AdmNumList.append(res[i][0])
            NameList.append(res[i][1])
            ClassList.append(res[i][2])
            SectionList.append(res[i][3])
            RollNumList.append(res[i][4])
            Lang2NameList.append(res[i][5])
            Lang3NameList.append(res[i][6])
            EngList.append(res[i][7])
            MathList.append(res[i][8])
            ScienceList.append(res[i][9])
            SocialList.append(res[i][10])
            Lang2List.append(res[i][11])
            Lang3List.append(res[i][12])
            ComputersList.append(res[i][13])
            TotList.append(res[i][14])
            AvgList.append(res[i][15])
            # ? Dataframe Values
        result6 = {
            "Admission Number": AdmNumList,
            "Name": NameList,
            "Class": ClassList,
            "Section": SectionList,
            "Roll Number": RollNumList,
            "2nd Language Name": Lang2NameList,
            "3nd Language Name": Lang3NameList,
            "English": EngList,
            "Mathematics": MathList,
            "Science": ScienceList,
            "Social Sciences": SocialList,
            "2nd Language": Lang2List,
            "3rd Language": Lang3List,
            "Computers": ComputersList,
            "Total": TotList,
            "Average %": AvgList,
        }
    else:
        result6 = {
            "Admission Number": [None],
            "Name": [None],
            "Class": [None],
            "Section": [None],
            "Roll Number": [None],
            "2nd Language Name": [None],
            "3nd Language Name": [None],
            "English": [None],
            "Mathematics": [None],
            "Science": [None],
            "Social Sciences": [None],
            "2nd Language": [None],
            "3rd Language": [None],
            "Computers": [None],
            "Total": [None],
            "Average %": [None],
        }

    # ? Grade 7
    cur.execute(f"select * from {db}.catthree where class=7")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        (
            AdmNumList,
            NameList,
            ClassList,
            SectionList,
            RollNumList,
            Lang2NameList,
            Lang3NameList,
            EngList,
            MathList,
            ScienceList,
            SocialList,
            Lang2List,
            Lang3List,
            ComputersList,
            TotList,
            AvgList,
        ) = ([], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [])
        # ? Adding values to list for dataframe
        for i in range(len(res)):
            AdmNumList.append(res[i][0])
            NameList.append(res[i][1])
            ClassList.append(res[i][2])
            SectionList.append(res[i][3])
            RollNumList.append(res[i][4])
            Lang2NameList.append(res[i][5])
            Lang3NameList.append(res[i][6])
            EngList.append(res[i][7])
            MathList.append(res[i][8])
            ScienceList.append(res[i][9])
            SocialList.append(res[i][10])
            Lang2List.append(res[i][11])
            Lang3List.append(res[i][12])
            ComputersList.append(res[i][13])
            TotList.append(res[i][14])
            AvgList.append(res[i][15])
            # ? Dataframe Values
        result7 = {
            "Admission Number": AdmNumList,
            "Name": NameList,
            "Class": ClassList,
            "Section": SectionList,
            "Roll Number": RollNumList,
            "2nd Language Name": Lang2NameList,
            "3nd Language Name": Lang3NameList,
            "English": EngList,
            "Mathematics": MathList,
            "Science": ScienceList,
            "Social Sciences": SocialList,
            "2nd Language": Lang2List,
            "3rd Language": Lang3List,
            "Computers": ComputersList,
            "Total": TotList,
            "Average %": AvgList,
        }
    else:
        result7 = {
            "Admission Number": [None],
            "Name": [None],
            "Class": [None],
            "Section": [None],
            "Roll Number": [None],
            "2nd Language Name": [None],
            "3nd Language Name": [None],
            "English": [None],
            "Mathematics": [None],
            "Science": [None],
            "Social Sciences": [None],
            "2nd Language": [None],
            "3rd Language": [None],
            "Computers": [None],
            "Total": [None],
            "Average %": [None],
        }

    # ? Grade 8
    cur.execute(f"select * from {db}.catthree where class=8")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        (
            AdmNumList,
            NameList,
            ClassList,
            SectionList,
            RollNumList,
            Lang2NameList,
            Lang3NameList,
            EngList,
            MathList,
            ScienceList,
            SocialList,
            Lang2List,
            Lang3List,
            ComputersList,
            TotList,
            AvgList,
        ) = ([], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [])
        # ? Adding values to list for dataframe
        for i in range(len(res)):
            AdmNumList.append(res[i][0])
            NameList.append(res[i][1])
            ClassList.append(res[i][2])
            SectionList.append(res[i][3])
            RollNumList.append(res[i][4])
            Lang2NameList.append(res[i][5])
            Lang3NameList.append(res[i][6])
            EngList.append(res[i][7])
            MathList.append(res[i][8])
            ScienceList.append(res[i][9])
            SocialList.append(res[i][10])
            Lang2List.append(res[i][11])
            Lang3List.append(res[i][12])
            ComputersList.append(res[i][13])
            TotList.append(res[i][14])
            AvgList.append(res[i][15])
            # ? Dataframe Values
        result8 = {
            "Admission Number": AdmNumList,
            "Name": NameList,
            "Class": ClassList,
            "Section": SectionList,
            "Roll Number": RollNumList,
            "2nd Language Name": Lang2NameList,
            "3nd Language Name": Lang3NameList,
            "English": EngList,
            "Mathematics": MathList,
            "Science": ScienceList,
            "Social Sciences": SocialList,
            "2nd Language": Lang2List,
            "3rd Language": Lang3List,
            "Computers": ComputersList,
            "Total": TotList,
            "Average %": AvgList,
        }
    else:
        result8 = {
            "Admission Number": [None],
            "Name": [None],
            "Class": [None],
            "Section": [None],
            "Roll Number": [None],
            "2nd Language Name": [None],
            "3nd Language Name": [None],
            "English": [None],
            "Mathematics": [None],
            "Science": [None],
            "Social Sciences": [None],
            "2nd Language": [None],
            "3rd Language": [None],
            "Computers": [None],
            "Total": [None],
            "Average %": [None],
        }

    # ? Grade 9
    cur.execute(f"select * from {db}.catfour where class=9")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        (
            AdmNumList,
            NameList,
            ClassList,
            SectionList,
            RollNumList,
            Lang2NameList,
            EngList,
            MathList,
            ScienceList,
            SocialList,
            Lang2List,
            TotList,
            AvgList,
        ) = (
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
        )
        # ? Adding values to list for dataframe
        for i in range(len(res)):
            AdmNumList.append(res[i][0])
            NameList.append(res[i][1])
            ClassList.append(res[i][2])
            SectionList.append(res[i][3])
            RollNumList.append(res[i][4])
            Lang2NameList.append(res[i][5])
            EngList.append(res[i][6])
            MathList.append(res[i][7])
            ScienceList.append(res[i][8])
            SocialList.append(res[i][9])
            Lang2List.append(res[i][10])
            TotList.append(res[i][11])
            AvgList.append(res[i][12])
        # ? Dataframe Values
        result9 = {
            "Admission Number": AdmNumList,
            "Name": NameList,
            "Class": ClassList,
            "Section": SectionList,
            "Roll Number": RollNumList,
            "2nd Language Name": Lang2NameList,
            "English": EngList,
            "Mathematics": MathList,
            "Science": ScienceList,
            "Social Sciences": SocialList,
            "2nd Language": Lang2List,
            "Total": TotList,
            "Average %": AvgList,
        }
    else:
        result9 = {
            "Admission Number": [None],
            "Name": [None],
            "Class": [None],
            "Section": [None],
            "Roll Number": [None],
            "2nd Language Name": [None],
            "English": [None],
            "Mathematics": [None],
            "Science": [None],
            "Social Sciences": [None],
            "2nd Language": [None],
            "Total": [None],
            "Average %": [None],
        }

    # ? Grade 10
    cur.execute(f"select * from {db}.catfour where class=10")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        (
            AdmNumList,
            NameList,
            ClassList,
            SectionList,
            RollNumList,
            Lang2NameList,
            EngList,
            MathList,
            ScienceList,
            SocialList,
            Lang2List,
            TotList,
            AvgList,
        ) = (
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
        )
        # ? Adding values to list for dataframe
        for i in range(len(res)):
            AdmNumList.append(res[i][0])
            NameList.append(res[i][1])
            ClassList.append(res[i][2])
            SectionList.append(res[i][3])
            RollNumList.append(res[i][4])
            Lang2NameList.append(res[i][5])
            EngList.append(res[i][6])
            MathList.append(res[i][7])
            ScienceList.append(res[i][8])
            SocialList.append(res[i][9])
            Lang2List.append(res[i][10])
            TotList.append(res[i][11])
            AvgList.append(res[i][12])
        # ? Dataframe Values
        result10 = {
            "Admission Number": AdmNumList,
            "Name": NameList,
            "Class": ClassList,
            "Section": SectionList,
            "Roll Number": RollNumList,
            "2nd Language Name": Lang2NameList,
            "English": EngList,
            "Mathematics": MathList,
            "Science": ScienceList,
            "Social Sciences": SocialList,
            "2nd Language": Lang2List,
            "Total": TotList,
            "Average %": AvgList,
        }
    else:
        result10 = {
            "Admission Number": [None],
            "Name": [None],
            "Class": [None],
            "Section": [None],
            "Roll Number": [None],
            "2nd Language Name": [None],
            "English": [None],
            "Mathematics": [None],
            "Science": [None],
            "Social Sciences": [None],
            "2nd Language": [None],
            "Total": [None],
            "Average %": [None],
        }

    # ? Grade 11
    # ? Mathematics, Physics, Chemistry
    cur.execute(f"select * from {db}.catfive where class=11")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        (
            AdmNumList,
            NameList,
            ClassList,
            SectionList,
            RollNumList,
            FcoreNameList,
            EngList,
            MathList,
            PhysicsList,
            ChemistryList,
            FcoreList,
            TotList,
            AvgList,
        ) = (
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
        )
        for i in range(len(res)):
            AdmNumList.append(res[i][0])
            NameList.append(res[i][1])
            ClassList.append(res[i][2])
            SectionList.append(res[i][3])
            RollNumList.append(res[i][4])
            FcoreNameList.append(res[i][5])
            EngList.append(res[i][6])
            MathList.append(res[i][7])
            PhysicsList.append(res[i][8])
            ChemistryList.append(res[i][9])
            FcoreList.append(res[i][10])
            TotList.append(res[i][11])
            AvgList.append(res[i][12])
        MPCResult1 = {
            "Admission Number": AdmNumList,
            "Name": NameList,
            "Class": ClassList,
            "Section": SectionList,
            "Roll Number": RollNumList,
            "5th Core Name": FcoreNameList,
            "English": EngList,
            "Mathematics": MathList,
            "Physics": PhysicsList,
            "Chemistry": ChemistryList,
            "5th Core": FcoreList,
            "Total": TotList,
            "Average %": AvgList,
        }
    else:
        MPCResult1 = {
            "Admission Number": [None],
            "Name": [None],
            "Class": [None],
            "Section": [None],
            "Roll Number": [None],
            "5th Core Name": [None],
            "English": [None],
            "Maths": [None],
            "Physics": [None],
            "Chemistry": [None],
            "5th Core": [None],
            "Total": [None],
            "Average %": [None],
        }

    # ? Biology, Physics, Chemistry
    cur.execute(f"select * from {db}.catsix where class=11")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        (
            AdmNumList,
            NameList,
            ClassList,
            SectionList,
            RollNumList,
            FcoreNameList,
            EngList,
            BioList,
            PhysicsList,
            ChemistryList,
            FcoreList,
            TotList,
            AvgList,
        ) = (
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
        )
        for i in range(len(res)):
            AdmNumList.append(res[i][0])
            NameList.append(res[i][1])
            ClassList.append(res[i][2])
            SectionList.append(res[i][3])
            RollNumList.append(res[i][4])
            FcoreNameList.append(res[i][5])
            EngList.append(res[i][6])
            BioList.append(res[i][7])
            PhysicsList.append(res[i][8])
            ChemistryList.append(res[i][9])
            FcoreList.append(res[i][10])
            TotList.append(res[i][11])
            AvgList.append(res[i][12])
        BiPCResult1 = {
            "Admission Number": AdmNumList,
            "Name": NameList,
            "Class": ClassList,
            "Section": SectionList,
            "Roll Number": RollNumList,
            "5th Core Name": FcoreNameList,
            "English": EngList,
            "Biology": BioList,
            "Physics": PhysicsList,
            "Chemistry": ChemistryList,
            "5th Core": FcoreList,
            "Total": TotList,
            "Average %": AvgList,
        }
    else:
        BiPCResult1 = {
            "Admission Number": [None],
            "Name": [None],
            "Class": [None],
            "Section": [None],
            "Roll Number": [None],
            "5th Core Name": [None],
            "English": [None],
            "Biology": [None],
            "Physics": [None],
            "Chemistry": [None],
            "5th Core": [None],
            "Total": [None],
            "Average %": [None],
        }

    # ? Commerce
    cur.execute(f"select * from {db}.catseven where class=11")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        (
            AdmNumList,
            NameList,
            ClassList,
            SectionList,
            RollNumList,
            FcoreNameList,
            EngList,
            AccountsList,
            BStList,
            EconList,
            FcoreList,
            TotList,
            AvgList,
        ) = (
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
        )
        for i in range(len(res)):
            AdmNumList.append(res[i][0])
            NameList.append(res[i][1])
            ClassList.append(res[i][2])
            SectionList.append(res[i][3])
            RollNumList.append(res[i][4])
            FcoreNameList.append(res[i][5])
            EngList.append(res[i][6])
            AccountsList.append(res[i][7])
            BStList.append(res[i][8])
            EconList.append(res[i][9])
            FcoreList.append(res[i][10])
            TotList.append(res[i][11])
            AvgList.append(res[i][12])
        CommerceResult1 = {
            "Admission Number": AdmNumList,
            "Name": NameList,
            "Class": ClassList,
            "Section": SectionList,
            "Roll Number": RollNumList,
            "5th Core Name": FcoreNameList,
            "English": EngList,
            "Accounts": AccountsList,
            "Business Studies": BStList,
            "Economics": EconList,
            "5th Core": FcoreList,
            "Total": TotList,
            "Average %": AvgList,
        }
    else:
        CommerceResult1 = {
            "Admission Number": [None],
            "Name": [None],
            "Class": [None],
            "Section": [None],
            "Roll Number": [None],
            "5th Core Name": [None],
            "English": [None],
            "Accounts": [None],
            "Business Studies": [None],
            "Economics": [None],
            "5th Core": [None],
            "Total": [None],
            "Average %": [None],
        }

    # ? Humanities
    cur.execute(f"select * from {db}.cateight where class=11")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        (
            AdmNumList,
            NameList,
            ClassList,
            SectionList,
            RollNumList,
            FcoreNameList,
            EngList,
            HistoryList,
            PolSciList,
            EconList,
            FcoreList,
            TotList,
            AvgList,
        ) = (
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
        )
        for i in range(len(res)):
            AdmNumList.append(res[i][0])
            NameList.append(res[i][1])
            ClassList.append(res[i][2])
            SectionList.append(res[i][3])
            RollNumList.append(res[i][4])
            FcoreNameList.append(res[i][5])
            EngList.append(res[i][6])
            HistoryList.append(res[i][7])
            PolSciList.append(res[i][8])
            EconList.append(res[i][9])
            FcoreList.append(res[i][10])
            TotList.append(res[i][11])
            AvgList.append(res[i][12])
        HumanitiesResult1 = {
            "Admission Number": AdmNumList,
            "Name": NameList,
            "Class": ClassList,
            "Section": SectionList,
            "Roll Number": RollNumList,
            "5th Core Name": FcoreNameList,
            "English": EngList,
            "History": HistoryList,
            "Political Sciences": PolSciList,
            "Economics": EconList,
            "5th Core": FcoreList,
            "Total": TotList,
            "Average %": AvgList,
        }
    else:
        HumanitiesResult1 = {
            "Admission Number": [None],
            "Name": [None],
            "Class": [None],
            "Section": [None],
            "Roll Number": [None],
            "5th Core Name": [None],
            "English": [None],
            "History": [None],
            "Political Sciences": [None],
            "Economics": [None],
            "5th Core": [None],
            "Total": [None],
            "Average %": [None],
        }
    # ? Mathematics, Physics, Chemistry
    cur.execute(f"select * from {db}.catfive where class=12")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        (
            AdmNumList,
            NameList,
            ClassList,
            SectionList,
            RollNumList,
            FcoreNameList,
            EngList,
            MathList,
            PhysicsList,
            ChemistryList,
            FcoreList,
            TotList,
            AvgList,
        ) = (
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
        )
        for i in range(len(res)):
            AdmNumList.append(res[i][0])
            NameList.append(res[i][1])
            ClassList.append(res[i][2])
            SectionList.append(res[i][3])
            RollNumList.append(res[i][4])
            FcoreNameList.append(res[i][5])
            EngList.append(res[i][6])
            MathList.append(res[i][7])
            PhysicsList.append(res[i][8])
            ChemistryList.append(res[i][9])
            FcoreList.append(res[i][10])
            TotList.append(res[i][11])
            AvgList.append(res[i][12])
        MPCResult2 = {
            "Admission Number": AdmNumList,
            "Name": NameList,
            "Class": ClassList,
            "Section": SectionList,
            "Roll Number": RollNumList,
            "5th Core Name": FcoreNameList,
            "English": EngList,
            "Mathematics": MathList,
            "Physics": PhysicsList,
            "Chemistry": ChemistryList,
            "5th Core": FcoreList,
            "Total": TotList,
            "Average %": AvgList,
        }
    else:
        MPCResult2 = {
            "Admission Number": [None],
            "Name": [None],
            "Class": [None],
            "Section": [None],
            "Roll Number": [None],
            "5th Core Name": [None],
            "English": [None],
            "Maths": [None],
            "Physics": [None],
            "Chemistry": [None],
            "5th Core": [None],
            "Total": [None],
            "Average %": [None],
        }

    # ? Biology, Physics, Chemistry
    cur.execute(f"select * from {db}.catsix where class=12")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        (
            AdmNumList,
            NameList,
            ClassList,
            SectionList,
            RollNumList,
            FcoreNameList,
            EngList,
            BioList,
            PhysicsList,
            ChemistryList,
            FcoreList,
            TotList,
            AvgList,
        ) = (
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
        )
        for i in range(len(res)):
            AdmNumList.append(res[i][0])
            NameList.append(res[i][1])
            ClassList.append(res[i][2])
            SectionList.append(res[i][3])
            RollNumList.append(res[i][4])
            FcoreNameList.append(res[i][5])
            EngList.append(res[i][6])
            BioList.append(res[i][7])
            PhysicsList.append(res[i][8])
            ChemistryList.append(res[i][9])
            FcoreList.append(res[i][10])
            TotList.append(res[i][11])
            AvgList.append(res[i][12])
        BiPCResult2 = {
            "Admission Number": AdmNumList,
            "Name": NameList,
            "Class": ClassList,
            "Section": SectionList,
            "Roll Number": RollNumList,
            "5th Core Name": FcoreNameList,
            "English": EngList,
            "Biology": BioList,
            "Physics": PhysicsList,
            "Chemistry": ChemistryList,
            "5th Core": FcoreList,
            "Total": TotList,
            "Average %": AvgList,
        }
    else:
        BiPCResult2 = {
            "Admission Number": [None],
            "Name": [None],
            "Class": [None],
            "Section": [None],
            "Roll Number": [None],
            "5th Core Name": [None],
            "English": [None],
            "Biology": [None],
            "Physics": [None],
            "Chemistry": [None],
            "5th Core": [None],
            "Total": [None],
            "Average %": [None],
        }

    # ? Commerce
    cur.execute(f"select * from {db}.catseven where class=12")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        (
            AdmNumList,
            NameList,
            ClassList,
            SectionList,
            RollNumList,
            FcoreNameList,
            EngList,
            AccountsList,
            BStList,
            EconList,
            FcoreList,
            TotList,
            AvgList,
        ) = (
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
        )
        for i in range(len(res)):
            AdmNumList.append(res[i][0])
            NameList.append(res[i][1])
            ClassList.append(res[i][2])
            SectionList.append(res[i][3])
            RollNumList.append(res[i][4])
            FcoreNameList.append(res[i][5])
            EngList.append(res[i][6])
            AccountsList.append(res[i][7])
            BStList.append(res[i][8])
            EconList.append(res[i][9])
            FcoreList.append(res[i][10])
            TotList.append(res[i][11])
            AvgList.append(res[i][12])
        CommerceResult2 = {
            "Admission Number": AdmNumList,
            "Name": NameList,
            "Class": ClassList,
            "Section": SectionList,
            "Roll Number": RollNumList,
            "5th Core Name": FcoreNameList,
            "English": EngList,
            "Accounts": AccountsList,
            "Business Studies": BStList,
            "Economics": EconList,
            "5th Core": FcoreList,
            "Total": TotList,
            "Average %": AvgList,
        }
    else:
        CommerceResult2 = {
            "Admission Number": [None],
            "Name": [None],
            "Class": [None],
            "Section": [None],
            "Roll Number": [None],
            "5th Core Name": [None],
            "English": [None],
            "Accounts": [None],
            "Business Studies": [None],
            "Economics": [None],
            "5th Core": [None],
            "Total": [None],
            "Average %": [None],
        }

    # ? Humanities
    cur.execute(f"select * from {db}.cateight where class=12")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        (
            AdmNumList,
            NameList,
            ClassList,
            SectionList,
            RollNumList,
            FcoreNameList,
            EngList,
            HistoryList,
            PolSciList,
            EconList,
            FcoreList,
            TotList,
            AvgList,
        ) = (
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
        )
        for i in range(len(res)):
            AdmNumList.append(res[i][0])
            NameList.append(res[i][1])
            ClassList.append(res[i][2])
            SectionList.append(res[i][3])
            RollNumList.append(res[i][4])
            FcoreNameList.append(res[i][5])
            EngList.append(res[i][6])
            HistoryList.append(res[i][7])
            PolSciList.append(res[i][8])
            EconList.append(res[i][9])
            FcoreList.append(res[i][10])
            TotList.append(res[i][11])
            AvgList.append(res[i][12])
        HumanitiesResult2 = {
            "Admission Number": AdmNumList,
            "Name": NameList,
            "Class": ClassList,
            "Section": SectionList,
            "Roll Number": RollNumList,
            "5th Core Name": FcoreNameList,
            "English": EngList,
            "History": HistoryList,
            "Political Sciences": PolSciList,
            "Economics": EconList,
            "5th Core": FcoreList,
            "Total": TotList,
            "Average %": AvgList,
        }
    else:
        HumanitiesResult2 = {
            "Admission Number": [None],
            "Name": [None],
            "Class": [None],
            "Section": [None],
            "Roll Number": [None],
            "5th Core Name": [None],
            "English": [None],
            "History": [None],
            "Political Sciences": [None],
            "Economics": [None],
            "5th Core": [None],
            "Total": [None],
            "Average %": [None],
        }

    # ? Dataframing the results
    df1 = dataframe(result1)
    df2 = dataframe(result2)
    df3 = dataframe(result3)
    df4 = dataframe(result4)
    df5 = dataframe(result5)
    df6 = dataframe(result6)
    df7 = dataframe(result7)
    df8 = dataframe(result8)
    df9 = dataframe(result9)
    df10 = dataframe(result10)
    dfmpc1 = dataframe(MPCResult1)
    dfbipc1 = dataframe(BiPCResult1)
    dfcec1 = dataframe(CommerceResult1)
    dfhuman1 = dataframe(HumanitiesResult1)
    dfmpc2 = dataframe(MPCResult2)
    dfbipc2 = dataframe(BiPCResult2)
    dfcec2 = dataframe(CommerceResult2)
    dfhuman2 = dataframe(HumanitiesResult2)

    with open(f"All Student Records.html", "w") as f:
        f.write(f"<h5 class='text-center fw-bolder'>Grade 1: </h5>")
        f.write(
            '<head><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous"></head>'
        )
        f.write(
            "<style>@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500&display=swap'); body{padding:50px 20px;font-family:'JetBrains Mono',sans-serif!important;} table{margin:auto; margin-bottom:20px;width:175vh!important;} tr{border-bottom:1px solid #000;} th,tr,td{text-align:center!important;} table {border-collapse: separate; border-spacing: 10px 0;} td {padding: 10px 0;} table td + td, th + th{ border-left:1px solid #000; } table { border-collapse:collapse; } table thead tr { border-bottom: 1px solid #000; } </style>"
        )
        df1.to_html(f, index=False)
        f.write(f"<h5 class='text-center fw-bolder'>Grade 2: </h5>")
        f.write(
            '<head><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous"></head>'
        )
        f.write(
            "<style>@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500&display=swap'); body{padding:50px 20px;font-family:'JetBrains Mono',sans-serif!important;} table{margin:auto; margin-bottom:20px;width:175vh!important;} tr{border-bottom:1px solid #000;} th,tr,td{text-align:center!important;} table {border-collapse: separate; border-spacing: 10px 0;} td {padding: 10px 0;} table td + td, th + th{ border-left:1px solid #000; } table { border-collapse:collapse; } table thead tr { border-bottom: 1px solid #000; } </style>"
        )
        df2.to_html(f, index=False)
        f.write(f"<h5 class='text-center fw-bolder'>Grade 3: </h5>")
        f.write(
            '<head><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous"></head>'
        )
        f.write(
            "<style>@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500&display=swap'); body{padding:50px 20px;font-family:'JetBrains Mono',sans-serif!important;} table{margin:auto; margin-bottom:20px;width:175vh!important;} tr{border-bottom:1px solid #000;} th,tr,td{text-align:center!important;} table {border-collapse: separate; border-spacing: 10px 0;} td {padding: 10px 0;} table td + td, th + th{ border-left:1px solid #000; } table { border-collapse:collapse; } table thead tr { border-bottom: 1px solid #000; } </style>"
        )
        df3.to_html(f, index=False)
        f.write(f"<h5 class='text-center fw-bolder'>Grade 4: </h5>")
        f.write(
            '<head><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous"></head>'
        )
        f.write(
            "<style>@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500&display=swap'); body{padding:50px 20px;font-family:'JetBrains Mono',sans-serif!important;} table{margin:auto; margin-bottom:20px;width:175vh!important;} tr{border-bottom:1px solid #000;} th,tr,td{text-align:center!important;} table {border-collapse: separate; border-spacing: 10px 0;} td {padding: 10px 0;} table td + td, th + th{ border-left:1px solid #000; } table { border-collapse:collapse; } table thead tr { border-bottom: 1px solid #000; } </style>"
        )
        df4.to_html(f, index=False)
        f.write(f"<h5 class='text-center fw-bolder'>Grade 5: </h5>")
        f.write(
            '<head><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous"></head>'
        )
        f.write(
            "<style>@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500&display=swap'); body{padding:50px 20px;font-family:'JetBrains Mono',sans-serif!important;} table{margin:auto; margin-bottom:20px;width:175vh!important;} tr{border-bottom:1px solid #000;} th,tr,td{text-align:center!important;} table {border-collapse: separate; border-spacing: 10px 0;} td {padding: 10px 0;} table td + td, th + th{ border-left:1px solid #000; } table { border-collapse:collapse; } table thead tr { border-bottom: 1px solid #000; } </style>"
        )
        df5.to_html(f, index=False)
        f.write(f"<h5 class='text-center fw-bolder'>Grade 6: </h5>")
        f.write(
            '<head><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous"></head>'
        )
        f.write(
            "<style>@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500&display=swap'); body{padding:50px 20px;font-family:'JetBrains Mono',sans-serif!important;} table{margin:auto; margin-bottom:20px;width:175vh!important;} tr{border-bottom:1px solid #000;} th,tr,td{text-align:center!important;} table {border-collapse: separate; border-spacing: 10px 0;} td {padding: 10px 0;} table td + td, th + th{ border-left:1px solid #000; } table { border-collapse:collapse; } table thead tr { border-bottom: 1px solid #000; } </style>"
        )
        df6.to_html(f, index=False)
        f.write(f"<h5 class='text-center fw-bolder'>Grade 7: </h5>")
        f.write(
            '<head><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous"></head>'
        )
        f.write(
            "<style>@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500&display=swap'); body{padding:50px 20px;font-family:'JetBrains Mono',sans-serif!important;} table{margin:auto; margin-bottom:20px;width:175vh!important;} tr{border-bottom:1px solid #000;} th,tr,td{text-align:center!important;} table {border-collapse: separate; border-spacing: 10px 0;} td {padding: 10px 0;} table td + td, th + th{ border-left:1px solid #000; } table { border-collapse:collapse; } table thead tr { border-bottom: 1px solid #000; } </style>"
        )
        df7.to_html(f, index=False)
        f.write(f"<h5 class='text-center fw-bolder'>Grade 8: </h5>")
        f.write(
            '<head><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous"></head>'
        )
        f.write(
            "<style>@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500&display=swap'); body{padding:50px 20px;font-family:'JetBrains Mono',sans-serif!important;} table{margin:auto; margin-bottom:20px;width:175vh!important;} tr{border-bottom:1px solid #000;} th,tr,td{text-align:center!important;} table {border-collapse: separate; border-spacing: 10px 0;} td {padding: 10px 0;} table td + td, th + th{ border-left:1px solid #000; } table { border-collapse:collapse; } table thead tr { border-bottom: 1px solid #000; } </style>"
        )
        df8.to_html(f, index=False)
        f.write(f"<h5 class='text-center fw-bolder'>Grade 9: </h5>")
        f.write(
            '<head><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous"></head>'
        )
        f.write(
            "<style>@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500&display=swap'); body{padding:50px 20px;font-family:'JetBrains Mono',sans-serif!important;} table{margin:auto; margin-bottom:20px;width:175vh!important;} tr{border-bottom:1px solid #000;} th,tr,td{text-align:center!important;} table {border-collapse: separate; border-spacing: 10px 0;} td {padding: 10px 0;} table td + td, th + th{ border-left:1px solid #000; } table { border-collapse:collapse; } table thead tr { border-bottom: 1px solid #000; } </style>"
        )
        df9.to_html(f, index=False)
        f.write(f"<h5 class='text-center fw-bolder'>Grade 10: </h5>")
        f.write(
            '<head><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous"></head>'
        )
        f.write(
            "<style>@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500&display=swap'); body{padding:50px 20px;font-family:'JetBrains Mono',sans-serif!important;} table{margin:auto; margin-bottom:20px;width:175vh!important;} tr{border-bottom:1px solid #000;} th,tr,td{text-align:center!important;} table {border-collapse: separate; border-spacing: 10px 0;} td {padding: 10px 0;} table td + td, th + th{ border-left:1px solid #000; } table { border-collapse:collapse; } table thead tr { border-bottom: 1px solid #000; } </style>"
        )
        df10.to_html(f, index=False)
        f.write(f"<h5 class='text-center fw-bolder'>Grade 11: </h5>")
        f.write(
            f"<h6 class='text-center fw-bolder'>Mathematics, Physics, Chemistry: </h6>"
        )
        dfmpc1.to_html(f, index=False)
        f.write(f"<h6 class='text-center fw-bolder'>Biology, Physics, Chemistry: </h6>")
        dfbipc1.to_html(f, index=False)
        f.write(f"<h6 class='text-center fw-bolder'>Commerce: </h6>")
        dfcec1.to_html(f, index=False)
        f.write(f"<h6 class='text-center fw-bolder'>Humanities: </h6>")
        dfhuman1.to_html(f, index=False)
        f.write(f"<h5 class='text-center fw-bolder'>Grade 12: </h5>")
        f.write(
            f"<h6 class='text-center fw-bolder'>Mathematics, Physics, Chemistry: </h6>"
        )
        dfmpc2.to_html(f, index=False)
        f.write(f"<h6 class='text-center fw-bolder'>Biology, Physics, Chemistry: </h6>")
        dfbipc2.to_html(f, index=False)
        f.write(f"<h6 class='text-center fw-bolder'>Commerce: </h6>")
        dfcec2.to_html(f, index=False)
        f.write(f"<h6 class='text-center fw-bolder'>Humanities: </h6>")
        dfhuman2.to_html(f, index=False)

    filename = f"All Student Records.html"
    open_new_tab(filename)

