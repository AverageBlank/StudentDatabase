# Starting of the program
# * ------ Made by Aaloke, Hemanth and Hussain
#! --------------------------------------------------
#! ---------- Imports
#! --------------------------------------------------
# region Imports
# ? Maths --> For rounding
from math import ceil

# ? Importing os to get operating system and to run commands in terminal
from os import name, popen, system

# ? Importing string to have a valid name without symbols
from string import ascii_letters, digits, punctuation

# ? Time --> For pausing the program
from time import sleep

# ? Web Browser --> For opening dataframe on browser
from webbrowser import open_new_tab

# ? Questionary --> To provide choices and autocompletions
import questionary
from questionary import Style

# ? Matplotlib --> for plotting a graph
from matplotlib.pyplot import bar, show, title, xlabel, ylabel

# ? PyMySQL --> for connecting to MySQL
from pymysql import connect

# ? Pandas --> for storing data
from pandas import DataFrame

# ? Rich --> For great terminal user interface
from rich import print
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from rich.text import Text
from rich.tree import Tree
from rich import box
from rich.panel import Panel

console = Console()


# endregion
#! --------------------------------------------------
#! --------------------------------------------------

#! --------------------------------------------------
#! ---------- Functions
#! --------------------------------------------------
# region Functions
# ! Function to edit the inputted content to our desired parameters


def BetterInput(prompt, filter="None", type=str, error="Enter a proper value."):
    # ? To check for input parameters and returning the desired input.
    while True:
        try:
            # ? If type is string, check for filters
            if type == str:
                inp = input(prompt)
                if filter.lower() == "lower":
                    return inp.lower()
                elif filter.lower() == "upper":
                    return inp.upper()
                elif filter.lower() == "sentence":
                    return inp.title()
                else:
                    return inp
            # ? If type is int, check for filters
            elif type == int:
                inp = int(input(prompt))
                if filter.lower() in ["positive", "+"]:
                    return abs(inp)
                elif filter.lower() in ["negative", "-"]:
                    return -abs(inp)
                else:
                    return inp
            # ? If type is float, check for filters
            elif type == float:
                inp = float(input(prompt))
                if filter.lower() in ["positive", "+"]:
                    return abs(inp)
                elif filter.lower() in ["negative", "-"]:
                    return -abs(inp)
                else:
                    return inp
        except:
            print(error)


# ! To open our source code when called


def openCode():
    open_new_tab("https://github.com/AverageBlank/StudentDatabase")


def IsProperSection(prompt):
    while True:
        section = questionary.text(prompt, style=minimalStyle).ask()
        try:
            if len(section) > 2 or len(section) <= 0:
                raise ValueError
            elif section[0] not in ascii_letters:
                raise KeyError
            elif len(section) == 2:
                if section[1] not in digits or section[1] == " ":
                    raise TabError
            return section.upper()

        except ValueError:
            print("Length of section cannot have more than 2 or less than 1 character")
        except KeyError:
            print("Section can only have alphabets as the first character")
        except TabError:
            print("Section cannot have symbols")


def IsProperMarks(prompt):
    # ? To check for input parameters and returning the desired input.
    while True:
        try:
            # ? Rounds off the marks to the nearest integer value
            marks = ceil(float(questionary.text(prompt, style=minimalStyle).ask()))
            if 0 > marks or marks > 100:
                # ? If marks aren't between 0 or 100, rejects the marks
                raise AttributeError
            else:
                return marks
        except AttributeError:
            print(f"Marks need to be less than 100 and greater than 0.")
        except:
            print("Enter valid marks.")


# ! Function to avoid getting an error on an improper name


def IsProperName(name):
    # ? Checks for alphanumeric symbols in a name and rejects it if one exists
    NumericSymbols = [x for x in digits + punctuation]
    while True:
        try:
            for i in name:
                if i in NumericSymbols:
                    raise ValueError
            else:
                # ? If no symbols or numbers in a name, return the name
                return name
        except:
            name = questionary.text("Enter a valid student's name: ", style=minimalStyle).ask().title()


# ! Function to avoid getting an error on an improper stream


def IsProperStream(stream):
    while True:
        try:
            # ? If stream is not within the given list, raise a ValueError
            if stream.lower() not in [
                "pcm",
                "mpc",
                "bipc",
                "commerce",
                "cec",
                "humanities",
                "human",
            ]:
                raise ValueError
            else:
                # ? If stream is valid, rename given stream to a common name to keep it uniform
                if stream == "pcm":
                    stream = "mpc"
                if stream == "commerce":
                    stream = "cec"
                if stream == "human":
                    stream = "humanities"
                return stream
        except:
            # ? If all checks fail, ask for input again.
            stream = BetterInput("Enter a valid stream: ", "sentence", str)


# ! Function to avoid getting an error on fcore input depending on user's stream


def IsProperFcore(Fcore, Stream):
    while True:
        try:
            # ? If 5th core is not valid, raise a ValueError
            if Fcore.lower() not in [
                "mathematics",
                "math",
                "maths",
                "psychology",
                "psy",
                "informatics practices",
                "ip",
                "physical education",
                "pe",
                "fine arts",
                "fa",
            ]:
                raise ValueError
            else:
                # ? When chosen stream is valid, rename it to a common name to keep it uniform
                if Stream.lower() == "humanities" or Stream.lower() == "mpc":
                    if Fcore.lower() in ["math", "mathematics", "maths"]:
                        raise ValueError
                if Fcore.lower() == "math" or Fcore.lower() == "maths":
                    Fcore = "Mathematics"
                if Fcore.lower() == "psy":
                    Fcore = "Psychology"
                if Fcore.lower() == "ip":
                    Fcore = "Informatics Practices"
                if Fcore.lower() == "pe":
                    Fcore = "Physical Education"
                if Fcore.lower() == "fa":
                    Fcore = "Fine Arts"
                return Fcore
        except:
            # ? If checks fail, ask for an input again
            Fcore = questionary.select(
                "Choose a valid 5th Core: ",
                choices=[
                    "Mathematics",
                    "Informatics Practices",
                    "Psychology",
                    "Physical Education",
                    "Fine Arts",
                ], style=minimalStyle, instruction="\n"
            ).ask()


# ! Function to avoid getting an error on choosing a 2nd language, without including French


def IsProperLang2WOF(Lang2Name):
    while True:
        try:
            # ? Checks for improper languages given and raises error
            if Lang2Name.lower() not in ["hindi", "h", "telugu", "t"]:
                raise ValueError
            else:
                # ? Refactors given input into a uniform input for all
                if Lang2Name.lower() == "h":
                    Lang2Name = "Hindi"
                if Lang2Name.lower() == "t":
                    Lang2Name = "Telugu"
                return Lang2Name
        except:
            Lang2Name = BetterInput("Enter a valid 2nd Language: ", "sentence", str)


# ! Function to avoid getting an error on choosing a 2nd language, including French


def IsProperLang2WF(Lang2Name):
    while True:
        try:
            # ? Checks for improper languages given and raises error
            if Lang2Name.lower() not in [
                "hindi",
                "h",
                "telugu",
                "t",
                "french",
                "f",
            ]:
                raise ValueError
            else:
                # ? Refactors given input into a uniform input for all
                if Lang2Name.lower() == "h":
                    Lang2Name = "Hindi"
                if Lang2Name.lower() == "t":
                    Lang2Name = "Telugu"
                if Lang2Name.lower() == "f":
                    Lang2Name = "French"
                return Lang2Name
        except:
            Lang2Name = BetterInput("Enter a valid 2nd Language: ", "sentence", str)


# ! Function to avoid getting an error on choosing a 3rd language


def IsProperLang3(Lang3Name, Lang2Name):
    while True:
        try:
            # ? Checks for improper languages given and raises error
            if Lang3Name.lower() not in [
                "hindi",
                "h",
                "telugu",
                "t",
                "french",
                "f",
                "sanskrit",
                "s",
            ]:
                raise ValueError
            else:
                # ? Refactors given input of a language into a uniform input for all
                if Lang3Name.lower() == "h":
                    Lang3Name = "Hindi"
                if Lang3Name.lower() == "t":
                    Lang3Name = "Telugu"
                if Lang3Name.lower() == "f":
                    Lang3Name = "French"
                if Lang3Name.lower() == "s":
                    Lang3Name = "Sanskrit"
                if Lang2Name == Lang3Name:
                    raise ValueError
                return Lang3Name
        except:
            Lang3Name = (
                questionary.select(
                    "Choose a valid 3rd language: ",
                    choices=["Hindi", "Telugu", "French", "Sanskrit"], style=minimalStyle, instruction="\n"
                )
                .ask()
                .title()
            )


# ! Function to avoid getting an error on a wrong roll number input


def IsProperRollNum(RollNum):
    # ? Checks for an incorrect roll number between 0 and 60
    while True:
        try:
            if RollNum > 60 or RollNum <= 0:
                raise ValueError
            else:
                return RollNum
        except:
            RollNum = abs(int(questionary.text("Enter a valid roll number: ", style=minimalStyle).ask()))


# ! Function to clear the terminal screen depending on OS type


def ClearScreen():
    # ? Checks for OS type and then clears the terminal
    sleep(0.5)
    # ? Posix here is Macintosh and Linux, nt is Windows.
    system("clear" if name == "posix" else "cls")
    # print("-" * 70)
    # print(" " * 22 + "[bold italic]Student Management System")
    # print("-" * 70)
    console.print(
        Panel.fit("[bold italic #77DDD4]Student Management System", padding=(0, 20))
    )
    print()


# endregion
#! --------------------------------------------------
#! --------------------------------------------------

#! --------------------------------------------------
#! ---------- Main Program
#! --------------------------------------------------
# region Main Program
########! Connecting to the server !########
# ! <-- Connecting to the server and creating necessary tables -->


def Backend():
    global db, con, cur, console, minimalStyle
    # ! <-- Colors -->
    minimalStyle = Style(
        [
            ('answer', 'fg:#FFFFFF italic'), # ? White
            ('question', 'fg:#FFFFFF bold'), # ? White
            ('pointer', 'fg:#000FFF bold'), # ? Cyan
            ('highlighted', 'fg:#FFFFFF'), # ? White
            ('qmark', 'fg:#77DD77'), # ? Green
        ]
    )
    # ! <-- Connecting to MySQL -->
    ### ! <-- MySQL Smart Password System --> ! ###
    try:
        if name == "nt":
            chk = popen("cd %userprofile% && dir").read()
            CWD = popen("cd %userprofile% && chdir").read()
            CWD = CWD[:-1] + "\\"
            if "mysqlpassword" in chk:
                p = popen("cd %userprofile% && more mysqlpassword").read()
                p = p[:-1]
            else:
                raise ValueError
        elif name == "posix":
            chk = popen("ls ~").read()
            CWD = popen("cd ~ && pwd").read()
            if "mysqlpassword" in chk:
                p = popen("cat ~/mysqlpassword").read()
            else:
                raise ValueError
    except ValueError:
        # ? Clear the screen
        ClearScreen()
        # * Running this if password is not saved
        while True:
            p = questionary.password("Please type in your MySQL Password: ", style=minimalStyle).ask()
            try:
                # ? Connecting
                con = connect(user="root", host="localhost", password=p)
                cur = con.cursor()
                # ? Saving the password
                a = open(CWD[:-1] + "/mysqlpassword", "w")
                a.write(p)
                a.close()
                break
            except:
                print("Password was wrong, please try again.")
    # ? Connecting to the MySQL server
    con = connect(user="root", host="localhost", password=p)
    cur = con.cursor()

    db = "studentdatabase"

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


########! Related to Login !########
# ! <-- If register is called -->


def RegisterUser(User=None, Pass=None):
    # ? Clearing the screen
    ClearScreen()
    if User == None:
        while True:
            # ? Taking username incase not provided
            User = questionary.text("Enter the username: ", style=minimalStyle).ask()

            for i in User:
                if i in punctuation or i in digits:
                    print("Cannot contain symbols or digits")
                    continue
            if len(User) < 3:
                print("Length of the username must be greater than 3")
                continue
            if " " in User:
                print("Username cannot contain spaces")
                continue
            break
    if Pass == None:
        while True:
            # ? Taking password incase not provided
            Pass = questionary.password("Enter your password: ", style=minimalStyle).ask()
            if len(Pass) < 8:
                print("Length of the password must be greater than 8")
                continue
            break
    # ? Running the signup system
    cur.execute(f'select * from {db}.teacherDB where user="{User}"')
    userFetch = cur.fetchall()
    if len(userFetch) == 0:
        cur.execute(rf'insert into {db}.teacherDB values("{User}", "{Pass}")')
        con.commit()
        print("Successfully created user.")
    else:
        ClearScreen()
        print("This user already exists!")
        LoginUser(User, questionary.password("Enter the password for the user: ", style=minimalStyle).ask())


# ! <-- If Login is called -->
def LoginUser(User=None, Pass=None):
    # ? Number of wrong passwords entered
    NPass = 0
    # ? Clearing the screen
    ClearScreen()
    # ? Taking username incase not provided
    if User == None:
        while True:
            User = questionary.text("Enter the username: ", style=minimalStyle).ask()
            for i in User:
                if i in punctuation or i in digits:
                    print("Cannot contain symbols or digits")
                    break
            else:
                break
    # ? Taking password incase not provided
    if Pass == None:
        Pass = questionary.password("Enter your password: ", style=minimalStyle).ask()
    # ? Running the login system
    cur.execute(f'select * from {db}.teacherDB where user="{User}"')
    userFetch = cur.fetchall()
    if len(userFetch) == 0:
        ClearScreen()
        print("Username doesn't exist!")
        register = questionary.confirm(
            "Would you like to create a new user? ", style=minimalStyle
        ).ask()
        if register == True:
            RegisterUser()
        else:
            ClearScreen()
            print("Exiting Program")
            exit()
    else:
        while True:
            if userFetch[0][1] == rf"{Pass}":
                ClearScreen()
                print("Successful login!")
                sleep(1)
                break
            else:
                NPass += 1
                ClearScreen()
                if NPass == 3:
                    print("Wrong password entered too many times.")
                    exit()
                else:
                    print("Wrong Password, please try again.")
                    Pass = questionary.password("Enter your password: ", style=minimalStyle).ask()
                    continue


########! Related to student info !########
# ! <-- Adding students -->


def AddStudent():
    # ? Clearing Screen
    ClearScreen()
    # ? Name
    Name = IsProperName(
        questionary.text(
            "Enter student's name: ", style=minimalStyle
        ).ask()
    ).title()
    # ? Admission Number
    while True:
        try:
            AdmNum = abs(
                int(
                    questionary.text(
                        f"Enter {Name}'s admission number: ", style=minimalStyle
                    ).ask()
                )
            )
            if AdmNum == 0:
                raise ValueError
            break
        except:
            print("Please enter a valid admission number.")
    while True:
        cur.execute(f"select name from {db}.allstudents where AdmNum={AdmNum}")
        admNumFetch = cur.fetchall()
        try:
            if len(admNumFetch) == 0:
                ClearScreen()
                break
            else:
                raise ValueError
        except:
            print("This admission number already exists")
            AdmNum = abs(
                int(questionary.text("Enter a valid admission number: ", style=minimalStyle))
            ).ask()
    # ? Asking for class
    while True:
        Class = abs(int(questionary.text(f"Enter {Name}'s class: ", style=minimalStyle).ask()))
        # ! Categorizing by classes
        if 1 <= Class <= 3:
            # ? Asking for 2nd language name without french
            Lang2Name = questionary.select(
                f"Choose {Name}'s 2nd language: ", choices=["Hindi", "Telugu"] , style=minimalStyle, instruction='\n'
            ).ask()
        elif Class == 4:
            # ? Asking for 2nd language name with french
            Lang2Name = questionary.select(
                f"Choose {Name}'s 2nd language: ",
                choices=["Hindi", "Telugu", "French"], style=minimalStyle, instruction="\n"
            ).ask()
        elif 5 <= Class <= 8:
            # ? Asking for 2nd language name with french
            Lang2Name = questionary.select(
                f"Choose {Name}'s 2nd language: ",
                choices=["Hindi", "Telugu", "French"], style=minimalStyle, instruction="\n"
            ).ask()
            # ? Asking for 3rd language name
            Lang3Name = IsProperLang3(
                questionary.select(
                    f"Choose {Name}'s 3rd language: ",
                    choices=["Hindi", "Telugu", "French", "Sanskrit"], style=minimalStyle, instruction="\n"
                ).ask(),
                Lang2Name,
            )

        elif 9 <= Class <= 10:
            # ? Asking for 2nd language name with french
            Lang2Name = (
                questionary.select(
                    f"Choose {Name}'s 2nd language: ",
                    choices=["Hindi", "Telugu", "French"], style=minimalStyle, instruction='\n'
                )
                .ask()
                .lower()
            )
        elif Class in [11, 12]:
            # ! Categorizing by stream
            Stream = (
                questionary.select(
                    f"Choose {Name}'s stream: ",
                    choices=["MPC", "BiPC", "CEC", "Humanities"], style=minimalStyle, instruction='\n'
                )
                .ask()
                .lower()
            )
            # ? Asking for 5th core name
            FcoreName = IsProperFcore(
                questionary.select(
                    f"Choose {Name}'s 5th Core: ",
                    choices=[
                        "Mathematics",
                        "Informatics Practices",
                        "Psychology",
                        "Physical Education",
                        "Fine Arts",
                    ], style=minimalStyle, instruction='\n'
                ).ask(),
                Stream,
            )
        else:
            ClearScreen()
            print("Enter a valid class.")
            continue
        break
    # ? Clearing Screen
    ClearScreen()
    # ? Section
    Section = IsProperSection(f"Enter {Name}'s section: ")
    # ? Roll Number
    while True:
        try:
            RollNum = IsProperRollNum(
                abs(int(questionary.text(f"Enter {Name}'s roll number: ", style=minimalStyle).ask()))
            )
            break
        except:
            print("Enter a valid roll number.")

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
    # ? Grade 9 - 10
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
    ClearScreen()
    print(f"{Name} has been successfully added.")
    input()


# ! <-- Editing student information -->


def EditStudent():
    # ? Clearing Screen
    ClearScreen()
    # * Admission Number
    # ? Getting autocomplete for admission number
    cur.execute(f"select AdmNum from {db}.allstudents")
    a = cur.fetchall()
    adm = [str(a[i][0]) for i in range(len(a))]
    if len(adm) == 0:
        print("You have yet to add a student.")
        input()
        return None
    # ? Getting the actual admission number
    while True:
        try:
            AdmNum = str(
                int(
                    questionary.autocomplete(
                        f"Enter admission number of the student: ", adm, style=minimalStyle
                    ).ask()
                )
            )
            break
        except:
            print("Please enter a valid admission number.")
    while True:
        cur.execute(f"select class from {db}.allstudents where AdmNum={AdmNum}")
        admNumFetch = cur.fetchall()
        try:
            if len(admNumFetch) == 0:
                raise ValueError
            else:
                break
        except ValueError:
            print("This admission number does not exist.")
            while True:
                try:
                    AdmNum = str(
                        int(
                            questionary.autocomplete(
                                f"Enter admission number of the student: ", adm, style=minimalStyle
                            ).ask()
                        )
                    )
                    break
                except:
                    print("Please enter a valid admission number")
    ClearScreen()
    # ? Name
    Name = IsProperName(questionary.text("Enter new student's name: ", style=minimalStyle).ask()).title()

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
    while True:
        try:
            NewClass = abs(int(questionary.text(f"Enter {Name}'s new class: ", style=minimalStyle).ask()))
            if 1 > NewClass or NewClass > 12:
                ClearScreen()
                print("Enter a valid class.")
                continue
            break
        except:
            print("Please enter a valid class.")
    # ? Section
    Section = IsProperSection(f"Enter {Name}'s new section: ")
    # ? Roll Number
    while True:
        try:
            RollNum = IsProperRollNum(
                abs(int(questionary.text(f"Enter {Name}'s new roll number: ").ask()))
            )
            break
        except:
            print("Enter a valid roll number.")
    # ? Updating data in the main table
    cur.execute(
        f"update {db}.allstudents set Name='{Name}', Class={NewClass}, Section='{Section}' where AdmNum={AdmNum}"
    )
    # ? Clearing Screen
    ClearScreen()
    # ! Choosing new subjects
    if 1 <= NewClass <= 3:
        # ? Asking for 2nd language name without french
        Lang2Name = questionary.select(
            f"Choose {Name}'s new 2nd language: ", choices=["Hindi", "Telugu"], style=minimalStyle, instruction='\n'
        ).ask()
    elif NewClass == 4:
        # ? Asking for 2nd language name with french
        Lang2Name = questionary.select(
            f"Choose {Name}'s new 2nd language: ", choices=["Hindi", "Telugu", "French"], style=minimalStyle, instruction='\n'
        ).ask()
    elif 5 <= NewClass <= 8:
        # ? Asking for 2nd language name with french
        Lang2Name = questionary.select(
            f"Choose {Name}'s new 2nd language: ", choices=["Hindi", "Telugu", "French"], style=minimalStyle, instruction='\n'
        ).ask()
        # ? Asking for 3rd language name
        Lang3Name = IsProperLang3(
            questionary.select(
                f"Choose {Name}'s new 3rd language: ",
                choices=["Hindi", "Telugu", "French", "Sanskrit"], style=minimalStyle, instruction='\n'
            ).ask(),
            Lang2Name,
        )
    elif 9 <= NewClass <= 10:
        # ? Asking for 2nd language name with french
        Lang2Name = questionary.select(
            f"Choose {Name}'s new 2nd language: ", choices=["Hindi", "Telugu", "French"], style=minimalStyle, instruction='\n'
        ).ask()
    elif NewClass in [11, 12]:
        # ! Categorizing by stream
        NewStream = (
            questionary.select(
                f"Choose {Name}'s stream: ",
                choices=["MPC", "BiPC", "CEC", "Humanities"], style=minimalStyle, instruction='\n'
            )
            .ask()
            .lower()
        )
        # ? Asking for 5th core name
        FcoreName = IsProperFcore(
            questionary.select(
                f"Choose {Name}'s 5th Core: ",
                choices=[
                    "Mathematics",
                    "Informatics Practices",
                    "Psychology",
                    "Physical Education",
                    "Fine Arts",
                ], style=minimalStyle, instruction='\n'
            ).ask(),
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
    ClearScreen()
    print("Data has been successfully changed.")
    input()


# ! <-- Removing the student -->


def RemoveStudent():
    # ? Clearing Screen
    ClearScreen()
    # * Admission Number
    # ? Getting autocomplete for admission number
    cur.execute(f"select AdmNum from {db}.allstudents")
    a = cur.fetchall()
    adm = [str(a[i][0]) for i in range(len(a))]
    if len(adm) == 0:
        print("You have yet to add a student.")
        input()
        return None
    # ? Getting the actual admission number
    while True:
        try:
            AdmNum = str(
                int(
                    questionary.autocomplete(
                        f"Enter admission number of the student: ", adm, style=minimalStyle
                    ).ask()
                )
            )
            break
        except:
            print("Please enter a valid admission number.")
    while True:
        cur.execute(f"select name from {db}.allstudents where AdmNum={AdmNum}")
        admNumFetch = cur.fetchall()
        try:
            if len(admNumFetch) == 0:
                raise ValueError
            else:
                Name = admNumFetch[0][0]
                break
        except ValueError:
            print("This admission number does not exist.")
            while True:
                try:
                    AdmNum = str(
                        int(
                            questionary.autocomplete(
                                f"Enter admission number of the student: ", adm, style=minimalStyle
                            ).ask()
                        )
                    )
                    break
                except:
                    print("Please enter a valid admission number.")
    ClearScreen()
    AreYouSure = questionary.confirm(
        f"Are you sure you want to delete {Name}'s information? ", style=minimalStyle
    ).ask()
    if AreYouSure:
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
        ClearScreen()
        print("Successfully Deleted {Name}!")
        input()
    else:
        ClearScreen()
        print("Action cancelled")
        input()


########! Related to marks !########
# ! <-- Adding Marks -->


def AddMarks():
    # ? Clearing Screen
    ClearScreen()
    # * Admission Number
    # ? Getting autocomplete for admission number
    cur.execute(f"select AdmNum from {db}.allstudents")
    a = cur.fetchall()
    adm = [str(a[i][0]) for i in range(len(a))]
    if len(adm) == 0:
        print("You have yet to add a student.")
        input()
        return None
    # ? Getting the actual admission number
    while True:
        try:
            AdmNum = str(
                int(
                    questionary.autocomplete(
                        f"Enter admission number of the student: ", adm, style=minimalStyle
                    ).ask()
                )
            )
            break
        except:
            print("Please enter a valid admission number.")
    while True:
        cur.execute(f"select class from {db}.allstudents where AdmNum={AdmNum}")
        admNumFetch = cur.fetchall()
        try:
            if len(admNumFetch) == 0:
                raise ValueError
            else:
                break
        except ValueError:
            print("This admission number does not exist.")
            while True:
                try:
                    AdmNum = str(
                        int(
                            questionary.autocomplete(
                                f"Enter admission number of the student: ", adm, style=minimalStyle
                            ).ask()
                        )
                    )
                    break
                except:
                    print("Please enter a valid admission number.")
    ClearScreen()
    Class = admNumFetch[0][0]
    if Class == 1:
        English = IsProperMarks("Enter marks for English: ")
        Math = IsProperMarks("Enter marks for Mathematics: ")
        Science = IsProperMarks("Enter marks for Science: ")
        SocialSciences = IsProperMarks("Enter marks for Social Science: ")
        Lang2 = IsProperMarks("Enter marks for 2nd language: ")
        Total = English + Math + Science + SocialSciences + Lang2
        Average = round((Total / 500) * 100, 2)
        cur.execute(
            f"update {db}.catone set English={English}, Mathematics={Math}, Science={Science}, SocialSciences={SocialSciences}, Lang2={Lang2}, Average={Average}, Total = {Total} where AdmNum={AdmNum}"
        )
    elif 2 <= Class <= 4:
        English = IsProperMarks("Enter marks for English: ")
        Math = IsProperMarks("Enter marks for Mathematics: ")
        Science = IsProperMarks("Enter marks for Science: ")
        SocialSciences = IsProperMarks("Enter marks for Social Science: ")
        Lang2 = IsProperMarks("Enter marks for 2nd language: ")
        Computers = IsProperMarks("Enter marks for Computers: ")
        Total = English + Math + Science + SocialSciences + Lang2 + Computers
        Average = round((Total / 600) * 100, 2)
        cur.execute(
            f"update {db}.cattwo set English={English}, Mathematics={Math}, Science={Science}, SocialSciences={SocialSciences}, Lang2={Lang2}, Computers={Computers}, Average={Average}, Total = {Total} where AdmNum={AdmNum}"
        )

    elif 5 <= Class <= 8:
        English = IsProperMarks("Enter marks for English: ")
        Math = IsProperMarks("Enter marks for Mathematics: ")
        Science = IsProperMarks("Enter marks for Science: ")
        SocialSciences = IsProperMarks(
            "Enter marks for Social Science: ",
        )
        Lang2 = IsProperMarks("Enter marks for 2nd language: ")
        Lang3 = IsProperMarks("Enter marks for 3nd language: ")
        Computers = IsProperMarks("Enter marks for Computers: ")
        Total = English + Math + Science + SocialSciences + Lang2 + Lang3 + Computers
        Average = round((Total / 700) * 100, 2)
        cur.execute(
            f"update {db}.catthree set English={English}, Mathematics={Math}, Science={Science}, SocialSciences={SocialSciences}, Lang2={Lang2}, Lang3={Lang3}, Computers={Computers}, Average={Average}, Total = {Total} where AdmNum={AdmNum}"
        )

    elif 9 <= Class <= 10:
        English = IsProperMarks("Enter marks for English: ")
        Math = IsProperMarks("Enter marks for Mathematics: ")
        Science = IsProperMarks("Enter marks for Science: ")
        SocialSciences = IsProperMarks("Enter marks for Social Science: ")
        Lang2 = IsProperMarks("Enter marks for 2nd language: ")
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
            English = IsProperMarks("Enter marks for English: ")
            Math = IsProperMarks("Enter marks for Mathematics: ")
            Physics = IsProperMarks("Enter marks for Physics: ")
            Chemistry = IsProperMarks("Enter marks for Chemistry: ")
            Fcore = IsProperMarks(f"Enter marks for {FcoreName}: ")
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
            English = IsProperMarks("Enter marks for English: ")
            Biology = IsProperMarks("Enter marks for Biology: ")
            Physics = IsProperMarks("Enter marks for Physics: ")
            Chemistry = IsProperMarks("Enter marks for Chemistry: ")
            Fcore = IsProperMarks(f"Enter marks for {FcoreName}: ")
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
            English = IsProperMarks("Enter marks for English: ")
            Accounts = IsProperMarks("Enter marks for Accounts: ")
            BusinessStudies = IsProperMarks("Enter marks for Business Studies: ")
            Econ = IsProperMarks("Enter marks for Economics: ")
            Fcore = IsProperMarks(f"Enter marks for {FcoreName}: ")
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
            English = IsProperMarks("Enter marks for English: ")
            History = IsProperMarks("Enter marks for History: ")
            PolSci = IsProperMarks("Enter marks for Political Sciences: ")
            Econ = IsProperMarks("Enter marks for Economics: ")
            Fcore = IsProperMarks(f"Enter marks for {FcoreName}: ")
            Total = English + History + PolSci + Econ + Fcore
            Average = round((Total / 500) * 100)
            cur.execute(
                f"update {db}.cateight set English={English}, History={History}, PoliticalSciences={PolSci}, Economics={Econ}, Fcore={Fcore}, Average={Average}, Total = {Total} where AdmNum={AdmNum}"
            )
    con.commit()
    ClearScreen()
    print(f"Marks have successfully been added.")


# ! <-- Editing Marks -->


def EditMarks():
    # ? Clearing Screen
    ClearScreen()
    # * Admission Number
    # ? Getting autocomplete for admission number
    cur.execute(f"select AdmNum from {db}.allstudents")
    a = cur.fetchall()
    adm = [str(a[i][0]) for i in range(len(a))]
    if len(adm) == 0:
        print("You have yet to add a student.")
        input()
        return None
    # ? Getting the actual admission number
    while True:
        try:
            AdmNum = str(
                int(
                    questionary.autocomplete(
                        f"Enter admission number of the student: ", adm, style=minimalStyle
                    ).ask()
                )
            )
            break
        except:
            print("Please enter a valid admission number.")
    while True:
        cur.execute(f"select class from {db}.allstudents where AdmNum={AdmNum}")
        admNumFetch = cur.fetchall()
        try:
            if len(admNumFetch) == 0:
                raise ValueError
            else:
                break
        except ValueError:
            print("This admission number does not exist.")
            while True:
                try:
                    AdmNum = str(
                        int(
                            questionary.autocomplete(
                                f"Enter admission number of the student: ", adm, style=minimalStyle
                            ).ask()
                        )
                    )
                    break
                except:
                    print("Please enter a valid admission number.")
    Class = admNumFetch[0][0]
    if Class == 1:
        English = IsProperMarks("Enter new marks for English: ")
        Math = IsProperMarks("Enter new marks for Mathematics: ")
        Science = IsProperMarks("Enter new marks for Science: ")
        SocialSciences = IsProperMarks("Enter new marks for Social Science: ")
        Lang2 = IsProperMarks("Enter new marks for 2nd language: ")
        Total = English + Math + Science + SocialSciences + Lang2
        Average = round((Total / 500) * 100, 2)
        cur.execute(
            f"update {db}.catone set English={English}, Mathematics={Math}, Science={Science}, SocialSciences={SocialSciences}, Lang2={Lang2}, Average={Average}, Total = {Total} where AdmNum={AdmNum}"
        )
    elif 2 <= Class <= 4:
        English = IsProperMarks("Enter new marks for English: ")
        Math = IsProperMarks("Enter new marks for Mathematics: ")
        Science = IsProperMarks("Enter new marks for Science: ")
        SocialSciences = IsProperMarks("Enter new marks for Social Science: ")
        Lang2 = IsProperMarks("Enter new marks for 2nd language: ")
        Computers = IsProperMarks("Enter new marks for Computers: ")
        Total = English + Math + Science + SocialSciences + Lang2 + Computers
        Average = round((Total / 600) * 100, 2)
        cur.execute(
            f"update {db}.cattwo set English={English}, Mathematics={Math}, Science={Science}, SocialSciences={SocialSciences}, Lang2={Lang2}, Computers={Computers}, Average={Average}, Total = {Total} where AdmNum={AdmNum}"
        )

    elif 5 <= Class <= 8:
        English = IsProperMarks("Enter new marks for English: ")
        Math = IsProperMarks("Enter new marks for Mathematics: ")
        Science = IsProperMarks("Enter new marks for Science: ")
        SocialSciences = IsProperMarks("Enter new marks for Social Science: ")
        Lang2 = IsProperMarks("Enter new marks for 2nd language: ")
        Lang3 = IsProperMarks("Enter new marks for 3nd language: ")
        Computers = IsProperMarks("Enter new marks for Computers: ")
        Total = English + Math + Science + SocialSciences + Lang2 + Lang3 + Computers
        Average = round((Total / 700) * 100, 2)
        cur.execute(
            f"update {db}.catthree set English={English}, Mathematics={Math}, Science={Science}, SocialSciences={SocialSciences}, Lang2={Lang2}, Lang3={Lang3}, Computers={Computers}, Average={Average}, Total = {Total} where AdmNum={AdmNum}"
        )

    elif 9 <= Class <= 10:
        English = IsProperMarks("Enter new marks for English: ")
        Math = IsProperMarks("Enter new marks for Mathematics: ")
        Science = IsProperMarks("Enter new marks for Science: ")
        SocialSciences = IsProperMarks("Enter new marks for Social Science: ")
        Lang2 = IsProperMarks("Enter new marks for 2nd language: ")
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
            English = IsProperMarks("Enter new marks for English: ")
            Math = IsProperMarks("Enter new marks for Mathematics: ")
            Physics = IsProperMarks("Enter new marks for Physics: ")
            Chemistry = IsProperMarks("Enter new marks for Chemistry: ")
            Fcore = IsProperMarks(f"Enter new marks for {FcoreName}: ")
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
            English = IsProperMarks("Enter new marks for English: ")
            Biology = IsProperMarks("Enter new marks for Biology: ")
            Physics = IsProperMarks("Enter new marks for Physics: ")
            Chemistry = IsProperMarks("Enter new marks for Chemistry: ")
            Fcore = IsProperMarks(f"Enter new marks for {FcoreName}: ")
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
            English = IsProperMarks("Enter new marks for English: ")
            Accounts = IsProperMarks("Enter new marks for Accounts: ")
            BusinessStudies = IsProperMarks("Enter new marks for Business Studies: ")
            Econ = IsProperMarks("Enter new marks for Economics: ")
            Fcore = IsProperMarks(f"Enter new marks for {FcoreName}: ")
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
            English = IsProperMarks("Enter new marks for English: ")
            History = IsProperMarks("Enter new marks for History: ")
            PolSci = IsProperMarks("Enter new marks for Political Sciences: ")
            Econ = IsProperMarks("Enter new marks for Economics: ")
            Fcore = IsProperMarks(f"Enter new marks for {FcoreName}: ")
            Total = English + History + PolSci + Econ + Fcore
            Average = round((Total / 500) * 100, 2)
            cur.execute(
                f"update {db}.cateight set English={English}, History={History}, PoliticalSciences={PolSci}, Economics={Econ}, Fcore={Fcore}, Average={Average}, Total = {Total} where AdmNum={AdmNum}"
            )
    con.commit()
    ClearScreen()
    print("Marks have been successfully changed.")


# ! <-- Removing Marks -->


def RemoveMarks():
    # ? Clearing Screen
    ClearScreen()
    # * Admission Number
    # ? Getting autocomplete for admission number
    cur.execute(f"select AdmNum from {db}.allstudents")
    a = cur.fetchall()
    adm = [str(a[i][0]) for i in range(len(a))]
    if len(adm) == 0:
        print("You have yet to add a student.")
        input()
        return None
    # ? Getting the actual admission number
    while True:
        try:
            AdmNum = str(
                int(
                    questionary.autocomplete(
                        f"Enter admission number of the student: ", adm, style=minimalStyle
                    ).ask()
                )
            )
            break
        except:
            print("Please enter a valid admission number.")
    while True:
        cur.execute(f"select name from {db}.allstudents where AdmNum={AdmNum}")
        admNumFetch = cur.fetchall()
        try:
            if len(admNumFetch) == 0:
                raise ValueError
            else:
                Name = admNumFetch[0][0]
                break
        except ValueError:
            print("This admission number does not exist.")
            while True:
                try:
                    AdmNum = str(
                        int(
                            questionary.autocomplete(
                                f"Enter admission number of the student: ", adm, style=minimalStyle
                            ).ask()
                        )
                    )
                    break
                except:
                    print("Please enter a valid admission number.")
    ClearScreen()
    AreYouSure = questionary.confirm(f"Are you sure you want to delete the marks of {Name}?", style=minimalStyle).ask()
    if AreYouSure:
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
        ClearScreen()
        print("Successfully deleted!")
    else:
        ClearScreen()
        print("Action cancelled")


########! Related to viewing data !########
# ! <-- Showing graph for Marks and Subjects -->


def ShowGraph():
    # ? Clearing Screen
    ClearScreen()
    # * Admission Number
    # ? Getting autocomplete for admission number
    cur.execute(f"select AdmNum from {db}.allstudents")
    a = cur.fetchall()
    adm = [str(a[i][0]) for i in range(len(a))]
    if len(adm) == 0:
        print("You have yet to add a student.")
        input()
        return None
    # ? Getting the actual admission number
    while True:
        try:
            AdmNum = str(
                int(
                    questionary.autocomplete(
                        f"Enter admission number of the student: ", adm, style=minimalStyle
                    ).ask()
                )
            )
            break
        except:
            print("Please enter a valid admission number.")
    while True:
        cur.execute(f"select class from {db}.allstudents where AdmNum={AdmNum}")
        admNumFetch = cur.fetchall()
        try:
            if len(admNumFetch) == 0:
                raise ValueError
            else:
                break
        except ValueError:
            print("This admission number does not exist.")
            while True:
                try:
                    AdmNum = str(
                        int(
                            questionary.autocomplete(
                                f"Enter admission number of the student: ", adm, style=minimalStyle
                            ).ask()
                        )
                    )
                    break
                except:
                    print("Please enter a valid admission number.")
    ClearScreen()
    Class = admNumFetch[0][0]

    # ? Class 1

    if Class == 1:
        cur.execute(f"select * from {db}.catone where AdmNum={AdmNum}")
        result = cur.fetchall()[0]
        SubMarks = result[6:11]
        name = result[1]
        Subjects = [
            "English",
            "Mathematics",
            "Science",
            "Social Sciences",
            "2ndLang",
        ]

    # ? Class 2 - Class 4

    elif 2 <= Class <= 4:
        cur.execute(f"select * from {db}.cattwo where AdmNum={AdmNum}")
        result = cur.fetchall()[0]
        SubMarks = result[6:12]
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
        SubMarks = result[7:14]
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
        SubMarks = result[6:11]
        name = result[1]
        Subjects = [
            "English",
            "Mathematics",
            "Science",
            "Social Sciences",
            "2ndLang",
        ]

    elif 11 <= Class <= 12:
        # ? Mathematics, Physics, Chemistry
        cur.execute(f"select * from {db}.catfive where AdmNum = {AdmNum}")
        MPCResult = cur.fetchall()
        if len(MPCResult) != 0:
            MPCResult = MPCResult[0]
            SubMarks = MPCResult[6:11]
            name = MPCResult[1]
            Subjects = [
                "English",
                "Mathematics",
                "Physics",
                "Chemistry",
                "5th Core",
            ]

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
        title(f"Name: {name} - Admission Number: {AdmNum}")
        bar(Subjects, SubMarks)
        xlabel("Subjects")
        ylabel("Marks")
        show()
    except:
        print("Marks do not exist.")
        input()


# ! <-- Displaying individual student records -->


def StudentRecords():
    ClearScreen()
    # * Admission Number
    # ? Getting autocomplete for admission number
    cur.execute(f"select AdmNum from {db}.allstudents")
    a = cur.fetchall()
    adm = [str(a[i][0]) for i in range(len(a))]
    if len(adm) == 0:
        print("You have yet to add a student.")
        input()
        return None
    # ? Getting the actual admission number
    while True:
        try:
            AdmNum = str(
                int(
                    questionary.autocomplete(
                        f"Enter admission number of the student: ", adm, style=minimalStyle
                    ).ask()
                )
            )
            break
        except:
            print("Please enter a valid admission number.")
    while True:
        cur.execute(f"select class from {db}.allstudents where AdmNum={AdmNum}")
        admNumFetch = cur.fetchall()
        try:
            if len(admNumFetch) == 0:
                raise ValueError
            else:
                break
        except ValueError:
            print("This admission number does not exist.")
            while True:
                try:
                    AdmNum = str(
                        int(
                            questionary.autocomplete(
                                f"Enter admission number of the student: ", adm, style=minimalStyle
                            ).ask()
                        )
                    )
                    break
                except:
                    print("Please enter a valid admission number.")
    ClearScreen()
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

        table = Table(show_header=True, header_style="bold", box=box.ROUNDED)
        table.add_column("Admission Number", style="green")
        table.add_column("Name", style="cyan")
        table.add_column("Class", style="cyan")
        table.add_column("Section", style="cyan")
        table.add_column("Roll Number", style="cyan")
        table.add_column("2nd Language", style="cyan")
        table.add_column("English", style="magenta")
        table.add_column("Mathematics", style="magenta")
        table.add_column("Science", style="magenta")
        table.add_column("Social Sciences", style="magenta")
        table.add_column(res[5], style="magenta")
        table.add_column("Total", style="red")
        table.add_column("Average %", style="red")
        table.add_row(
            str(res[0]),
            str(res[1]),
            str(res[2]),
            str(res[3]),
            str(res[4]),
            str(res[5]),
            str(res[6]),
            str(res[7]),
            str(res[8]),
            str(res[9]),
            str(res[10]),
            str(res[11]),
            str(res[12]),
        )

        if result["English"] == None:
            table = Table(show_header=True, header_style="bold", box=box.ROUNDED)
            table.add_column("Admission Number", style="green")
            table.add_column("Name", style="cyan")
            table.add_column("Class", style="cyan")
            table.add_column("Section", style="cyan")
            table.add_column("Roll Number", style="cyan")
            table.add_column("2nd Language", style="cyan")
            table.add_row(
                str(res[0]),
                str(res[1]),
                str(res[2]),
                str(res[3]),
                str(res[4]),
                str(res[5]),
            )
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
        table = Table(show_header=True, header_style="bold", box=box.ROUNDED)
        table.add_column("Admission Number", style="green")
        table.add_column("Name", style="cyan")
        table.add_column("Class", style="cyan")
        table.add_column("Section", style="cyan")
        table.add_column("Roll Number", style="cyan")
        table.add_column("2nd Language", style="cyan")
        table.add_column("English", style="magenta")
        table.add_column("Mathematics", style="magenta")
        table.add_column("Science", style="magenta")
        table.add_column("Social Sciences", style="magenta")
        table.add_column(res[5], style="magenta")
        table.add_column("Computers", style="magenta")
        table.add_column("Total", style="red")
        table.add_column("Average %", style="red")
        table.add_row(
            str(res[0]),
            str(res[1]),
            str(res[2]),
            str(res[3]),
            str(res[4]),
            str(res[5]),
            str(res[6]),
            str(res[7]),
            str(res[8]),
            str(res[9]),
            str(res[10]),
            str(res[11]),
            str(res[12]),
            str(res[13]),
        )

        if result["English"] == None:
            table = Table(show_header=True, header_style="bold", box=box.ROUNDED)
            table.add_column("Admission Number", style="green")
            table.add_column("Name", style="cyan")
            table.add_column("Class", style="cyan")
            table.add_column("Section", style="cyan")
            table.add_column("Roll Number", style="cyan")
            table.add_column("2nd Language", style="cyan")
            table.add_row(
                str(res[0]),
                str(res[1]),
                str(res[2]),
                str(res[3]),
                str(res[4]),
                str(res[5]),
            )
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
        table = Table(show_header=True, header_style="bold", box=box.ROUNDED)
        table.add_column("Admission Number", style="green")
        table.add_column("Name", style="cyan")
        table.add_column("Class", style="cyan")
        table.add_column("Section", style="cyan")
        table.add_column("Roll Number", style="cyan")
        table.add_column("2nd Language", style="cyan")
        table.add_column("3rd Language", style="cyan")
        table.add_column("English", style="magenta")
        table.add_column("Mathematics", style="magenta")
        table.add_column("Science", style="magenta")
        table.add_column("Social Sciences", style="magenta")
        table.add_column(res[5], style="magenta")
        table.add_column(res[6], style="magenta")
        table.add_column("Computers", style="magenta")
        table.add_column("Total", style="red")
        table.add_column("Average %", style="red")
        table.add_row(
            str(res[0]),
            str(res[1]),
            str(res[2]),
            str(res[3]),
            str(res[4]),
            str(res[5]),
            str(res[6]),
            str(res[7]),
            str(res[8]),
            str(res[9]),
            str(res[10]),
            str(res[11]),
            str(res[12]),
            str(res[13]),
            str(res[14]),
        )
        if result["English"] == None:
            table = Table(show_header=True, header_style="bold", box=box.ROUNDED)
            table.add_column("Admission Number", style="green")
            table.add_column("Name", style="cyan")
            table.add_column("Class", style="cyan")
            table.add_column("Section", style="cyan")
            table.add_column("Roll Number", style="cyan")
            table.add_column("2nd Language", style="cyan")
            table.add_row(
                str(res[0]),
                str(res[1]),
                str(res[2]),
                str(res[3]),
                str(res[4]),
                str(res[5]),
                str(res[6]),
            )
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
        table = Table(show_header=True, header_style="bold", box=box.ROUNDED)
        table.add_column("Admission Number", style="green")
        table.add_column("Name", style="cyan")
        table.add_column("Class", style="cyan")
        table.add_column("Section", style="cyan")
        table.add_column("Roll Number", style="cyan")
        table.add_column("English", style="magenta")
        table.add_column("Mathematics", style="magenta")
        table.add_column("Science", style="magenta")
        table.add_column("Social Sciences", style="magenta")
        table.add_column(res[5], style="magenta")
        table.add_column("Total", style="red")
        table.add_column("Average %", style="red")
        table.add_row(
            str(res[0]),
            str(res[1]),
            str(res[2]),
            str(res[3]),
            str(res[4]),
            str(res[5]),
            str(res[6]),
            str(res[7]),
            str(res[8]),
            str(res[9]),
            str(res[10]),
            str(res[11]),
        )
        if result["English"] == None:
            table = Table(show_header=True, header_style="bold", box=box.ROUNDED)
            table.add_column("Admission Number", style="green")
            table.add_column("Name", style="cyan")
            table.add_column("Class", style="cyan")
            table.add_column("Section", style="cyan")
            table.add_column("Roll Number", style="cyan")
            table.add_column("2nd Language", style="cyan")
            table.add_row(
                str(res[0]),
                str(res[1]),
                str(res[2]),
                str(res[3]),
                str(res[4]),
                str(res[5]),
            )
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
            table = Table(show_header=True, header_style="bold", box=box.ROUNDED)
            table.add_column("Admission Number", style="green")
            table.add_column("Name", style="cyan")
            table.add_column("Class", style="cyan")
            table.add_column("Section", style="cyan")
            table.add_column("Roll Number", style="cyan")
            table.add_column("5th Core", style="cyan")
            table.add_column("English", style="magenta")
            table.add_column("Mathematics", style="magenta")
            table.add_column("Science", style="magenta")
            table.add_column("Social Sciences", style="magenta")
            table.add_column(res[5], style="magenta")
            table.add_column("Total", style="red")
            table.add_column("Average %", style="red")
            table.add_row(
                str(res[0]),
                str(res[1]),
                str(res[2]),
                str(res[3]),
                str(res[4]),
                str(res[5]),
                str(res[6]),
                str(res[7]),
                str(res[8]),
                str(res[9]),
                str(res[10]),
                str(res[11]),
                str(res[12]),
            )
            if result["English"] == None:
                table = Table(show_header=True, header_style="bold", box=box.ROUNDED)
                table.add_column("Admission Number", style="magenta")
                table.add_column("Name", style="cyan")
                table.add_column("Class", style="cyan")
                table.add_column("Section", style="cyan")
                table.add_column("Roll Number", style="cyan")
                table.add_column("5th Core", style="cyan")
                table.add_row(
                    str(res[0]),
                    str(res[1]),
                    str(res[2]),
                    str(res[3]),
                    str(res[4]),
                    str(res[5]),
                )
                prompt = f"{res[1]}'s details: "
            else:
                prompt = f"{res[1]}'s report card: "
        # ? Biology, Physics, Chemistry
        cur.execute(f"select * from {db}.catsix where AdmNum={AdmNum}")
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
                "Biology": res[7],
                "Physics": res[8],
                "Chemistry": res[9],
                res[5]: res[10],
                "Total": res[11],
                "Average %": res[12],
            }
            table = Table(show_header=True, header_style="bold", box=box.ROUNDED)
            table.add_column("Admission Number", style="green")
            table.add_column("Name", style="cyan")
            table.add_column("Class", style="cyan")
            table.add_column("Section", style="cyan")
            table.add_column("Roll Number", style="cyan")
            table.add_column("5th Core", style="cyan")
            table.add_column("English", style="magenta")
            table.add_column("Mathematics", style="magenta")
            table.add_column("Science", style="magenta")
            table.add_column("Social Sciences", style="magenta")
            table.add_column(res[5], style="magenta")
            table.add_column("Total", style="red")
            table.add_column("Average %", style="red")
            table.add_row(
                str(res[0]),
                str(res[1]),
                str(res[2]),
                str(res[3]),
                str(res[4]),
                str(res[5]),
                str(res[6]),
                str(res[7]),
                str(res[8]),
                str(res[9]),
                str(res[10]),
                str(res[11]),
                str(res[12]),
            )
            if result["English"] == None:
                table = Table(show_header=True, header_style="bold", box=box.ROUNDED)
                table.add_column("Admission Number", style="green")
                table.add_column("Name", style="cyan")
                table.add_column("Class", style="cyan")
                table.add_column("Section", style="cyan")
                table.add_column("Roll Number", style="cyan")
                table.add_column("5th Core", style="cyan")
                table.add_row(
                    str(res[0]),
                    str(res[1]),
                    str(res[2]),
                    str(res[3]),
                    str(res[4]),
                    str(res[5]),
                )
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
            table = Table(show_header=True, header_style="bold", box=box.ROUNDED)
            table.add_column("Admission Number", style="green")
            table.add_column("Name", style="cyan")
            table.add_column("Class", style="cyan")
            table.add_column("Section", style="cyan")
            table.add_column("Roll Number", style="cyan")
            table.add_column("5th Core", style="cyan")
            table.add_column("English", style="magenta")
            table.add_column("Mathematics", style="magenta")
            table.add_column("Science", style="magenta")
            table.add_column("Social Sciences", style="magenta")
            table.add_column(res[5], style="magenta")
            table.add_column("Total", style="red")
            table.add_column("Average %", style="red")
            table.add_row(
                str(res[0]),
                str(res[1]),
                str(res[2]),
                str(res[3]),
                str(res[4]),
                str(res[5]),
                str(res[6]),
                str(res[7]),
                str(res[8]),
                str(res[9]),
                str(res[10]),
                str(res[11]),
                str(res[12]),
            )
            if result["English"] == None:
                table = Table(show_header=True, header_style="bold", box=box.ROUNDED)
                table.add_column("Admission Number", style="green")
                table.add_column("Name", style="cyan")
                table.add_column("Class", style="cyan")
                table.add_column("Section", style="cyan")
                table.add_column("Roll Number", style="cyan")
                table.add_column("5th Core", style="cyan")
                table.add_row(
                    str(res[0]),
                    str(res[1]),
                    str(res[2]),
                    str(res[3]),
                    str(res[4]),
                    str(res[5]),
                )
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
            table = Table(show_header=True, header_style="bold", box=box.ROUNDED)
            table.add_column("Admission Number", style="green")
            table.add_column("Name", style="cyan")
            table.add_column("Class", style="cyan")
            table.add_column("Section", style="cyan")
            table.add_column("Roll Number", style="cyan")
            table.add_column("5th Core", style="cyan")
            table.add_column("English", style="magenta")
            table.add_column("Mathematics", style="magenta")
            table.add_column("Science", style="magenta")
            table.add_column("Social Sciences", style="magenta")
            table.add_column(res[5], style="magenta")
            table.add_column("Total", style="red")
            table.add_column("Average %", style="red")
            table.add_row(
                str(res[0]),
                str(res[1]),
                str(res[2]),
                str(res[3]),
                str(res[4]),
                str(res[5]),
                str(res[6]),
                str(res[7]),
                str(res[8]),
                str(res[9]),
                str(res[10]),
                str(res[11]),
                str(res[12]),
            )
            if result["English"] == None:
                table = Table(show_header=True, header_style="bold", box=box.ROUNDED)
                table.add_column("Admission Number", style="green")
                table.add_column("Name", style="cyan")
                table.add_column("Class", style="cyan")
                table.add_column("Section", style="cyan")
                table.add_column("Roll Number", style="cyan")
                table.add_column("5th Core", style="cyan")
                table.add_row(
                    str(res[0]),
                    str(res[1]),
                    str(res[2]),
                    str(res[3]),
                    str(res[4]),
                    str(res[5]),
                )
                prompt = f"{res[1]}'s details: "
            else:
                prompt = f"{res[1]}'s report card: "

    # ! Displaying Records/Report Card
    print(prompt)
    console.print(table)

    print()
    input()


# ! <-- Displaying one categories records -->


def ClassRecords(Class=None):
    # ? Clearing the screen
    ClearScreen()
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
                print("Enter a valid class")
    Grade = Class
    # ? Grade 1
    if Grade == 1:
        cur.execute(f"select * from {db}.catone where class={Class}")
        res = cur.fetchall()
        if len(res) != 0:
            res = [x for x in res]
            table = Table(show_header=True, header_style="bold", box=box.ROUNDED)
            table.add_column("Admission Number", style="green")
            table.add_column("Name", style="cyan")
            table.add_column("Class", style="cyan")
            table.add_column("Section", style="cyan")
            table.add_column("Roll Number", style="cyan")
            table.add_column("2nd Language Name", style="cyan")
            table.add_column("English", style="magenta")
            table.add_column("Mathematics", style="magenta")
            table.add_column("Science", style="magenta")
            table.add_column("Social Sciences", style="magenta")
            table.add_column("2nd Language", style="magenta")
            table.add_column("Total", style="red")
            table.add_column("Average %", style="red")
            for i in range(len(res)):
                table.add_row(
                    str(res[i][0]),
                    str(res[i][1]),
                    str(res[i][2]),
                    str(res[i][3]),
                    str(res[i][4]),
                    str(res[i][5]),
                    str(res[i][6]),
                    str(res[i][7]),
                    str(res[i][8]),
                    str(res[i][9]),
                    str(res[i][10]),
                    str(res[i][11]),
                    str(res[i][12]),
                )
            console.print(table)
        else:
            print(f"There are no students in Grade {Grade}")
            input()

    # ? Grade 2 to Grade 4
    if 2 <= Grade <= 4:
        cur.execute(f"select * from {db}.cattwo where class={Class}")
        res = cur.fetchall()
        if len(res) != 0:
            res = [x for x in res]
            table = Table(show_header=True, header_style="bold", box=box.ROUNDED)
            table.add_column("Admission Number", style="green")
            table.add_column("Name", style="cyan")
            table.add_column("Class", style="cyan")
            table.add_column("Section", style="cyan")
            table.add_column("Roll Number", style="cyan")
            table.add_column("2nd Language Name", style="cyan")
            table.add_column("English", style="magenta")
            table.add_column("Mathematics", style="magenta")
            table.add_column("Science", style="magenta")
            table.add_column("Social Sciences", style="magenta")
            table.add_column("2nd Language", style="magenta")
            table.add_column("Computers", style="magenta")
            table.add_column("Total", style="red")
            table.add_column("Average %", style="red")
            for i in range(len(res)):
                table.add_row(
                    str(res[i][0]),
                    str(res[i][1]),
                    str(res[i][2]),
                    str(res[i][3]),
                    str(res[i][4]),
                    str(res[i][5]),
                    str(res[i][6]),
                    str(res[i][7]),
                    str(res[i][8]),
                    str(res[i][9]),
                    str(res[i][10]),
                    str(res[i][11]),
                    str(res[i][12]),
                    str(res[i][13]),
                )
            console.print(table)
            input()
        else:
            print(f"There are no students in Grade {Grade}")
            input()

    # ? Grade 5 - Grade 8
    if 5 <= Grade <= 8:
        cur.execute(f"select * from {db}.catthree where class={Class}")
        res = cur.fetchall()
        if len(res) != 0:
            res = [x for x in res]
            table = Table(show_header=True, header_style="bold", box=box.ROUNDED)
            table.add_column("Admission Number", style="green")
            table.add_column("Name", style="cyan")
            table.add_column("Class", style="cyan")
            table.add_column("Section", style="cyan")
            table.add_column("Roll Number", style="cyan")
            table.add_column("2nd Language Name", style="cyan")
            table.add_column("3rd Language Name", style="cyan")
            table.add_column("English", style="magenta")
            table.add_column("Mathematics", style="magenta")
            table.add_column("Science", style="magenta")
            table.add_column("Social Sciences", style="magenta")
            table.add_column("2nd Language", style="magenta")
            table.add_column("3rd Language", style="magenta")
            table.add_column("Computers", style="magenta")
            table.add_column("Total", style="red")
            table.add_column("Average %", style="red")
            for i in range(len(res)):
                table.add_row(
                    str(res[i][0]),
                    str(res[i][1]),
                    str(res[i][2]),
                    str(res[i][3]),
                    str(res[i][4]),
                    str(res[i][5]),
                    str(res[i][6]),
                    str(res[i][7]),
                    str(res[i][8]),
                    str(res[i][9]),
                    str(res[i][10]),
                    str(res[i][11]),
                    str(res[i][12]),
                    str(res[i][13]),
                    str(res[i][14]),
                    str(res[i][15]),
                )
            console.print(table)
            input()
        else:
            print(f"There are no students in Grade {Grade}")
            input()

    # ? Grade 9 - Grade 10
    if 9 <= Grade <= 10:
        cur.execute(f"select * from {db}.catfour where class={Class}")
        res = cur.fetchall()
        if len(res) != 0:
            res = [x for x in res]
            table = Table(show_header=True, header_style="bold", box=box.ROUNDED)
            table.add_column("Admission Number", style="green")
            table.add_column("Name", style="cyan")
            table.add_column("Class", style="cyan")
            table.add_column("Section", style="cyan")
            table.add_column("Roll Number", style="cyan")
            table.add_column("2nd Language Name", style="cyan")
            table.add_column("English", style="magenta")
            table.add_column("Mathematics", style="magenta")
            table.add_column("Science", style="magenta")
            table.add_column("Social Sciences", style="magenta")
            table.add_column("2nd Language", style="magenta")
            table.add_column("Total", style="red")
            table.add_column("Average %", style="red")
            for i in range(len(res)):
                table.add_row(
                    str(res[i][0]),
                    str(res[i][1]),
                    str(res[i][2]),
                    str(res[i][3]),
                    str(res[i][4]),
                    str(res[i][5]),
                    str(res[i][6]),
                    str(res[i][7]),
                    str(res[i][8]),
                    str(res[i][9]),
                    str(res[i][10]),
                    str(res[i][11]),
                    str(res[i][12]),
                )
            console.print(table)
            input()
        else:
            print(f"There are no students in Grade {Grade}")
            input()

    # ? Mathematics, Physics, Chemistry
    if Grade in [11, 12]:
        cur.execute(f"select * from {db}.catfive where class={Class}")
        res = cur.fetchall()
        if len(res) != 0:
            res = [x for x in res]
            table = Table(show_header=True, header_style="bold", box=box.ROUNDED)
            table.add_column("Admission Number", style="green")
            table.add_column("Name", style="cyan")
            table.add_column("Class", style="cyan")
            table.add_column("Section", style="cyan")
            table.add_column("Roll Number", style="cyan")
            table.add_column("5th Core Name", style="cyan")
            table.add_column("English", style="magenta")
            table.add_column("Mathematics", style="magenta")
            table.add_column("Physics", style="magenta")
            table.add_column("Chemistry", style="magenta")
            table.add_column("5th Core", style="magenta")
            table.add_column("Total", style="red")
            table.add_column("Average %", style="red")
            for i in range(len(res)):
                table.add_row(
                    str(res[i][0]),
                    str(res[i][1]),
                    str(res[i][2]),
                    str(res[i][3]),
                    str(res[i][4]),
                    str(res[i][5]),
                    str(res[i][6]),
                    str(res[i][7]),
                    str(res[i][8]),
                    str(res[i][9]),
                    str(res[i][10]),
                    str(res[i][11]),
                    str(res[i][12]),
                )
            console.print(table)
        else:
            print()
            print(f"There are no students in Grade {Grade} MPC")

        # ? Biology, Physics, Chemistry
        cur.execute(f"select * from {db}.catsix where class={Class}")
        res = cur.fetchall()
        if len(res) != 0:
            res = [x for x in res]
            table = Table(show_header=True, header_style="bold", box=box.ROUNDED)
            table.add_column("Admission Number", style="green")
            table.add_column("Name", style="cyan")
            table.add_column("Class", style="cyan")
            table.add_column("Section", style="cyan")
            table.add_column("Roll Number", style="cyan")
            table.add_column("5th Core Name", style="cyan")
            table.add_column("English", style="magenta")
            table.add_column("Biology", style="magenta")
            table.add_column("Physics", style="magenta")
            table.add_column("Chemistry", style="magenta")
            table.add_column("5th Core", style="magenta")
            table.add_column("Total", style="red")
            table.add_column("Average %", style="red")
            for i in range(len(res)):
                table.add_row(
                    str(res[i][0]),
                    str(res[i][1]),
                    str(res[i][2]),
                    str(res[i][3]),
                    str(res[i][4]),
                    str(res[i][5]),
                    str(res[i][6]),
                    str(res[i][7]),
                    str(res[i][8]),
                    str(res[i][9]),
                    str(res[i][10]),
                    str(res[i][11]),
                    str(res[i][12]),
                )
            console.print(table)
        else:
            print()
            print(f"There are no students in Grade {Grade} BiPC")

        # ? Commerce
        cur.execute(f"select * from {db}.catseven where class={Class}")
        res = cur.fetchall()
        if len(res) != 0:
            res = [x for x in res]
            table = Table(show_header=True, header_style="bold", box=box.ROUNDED)
            table.add_column("Admission Number", style="green")
            table.add_column("Name", style="cyan")
            table.add_column("Class", style="cyan")
            table.add_column("Section", style="cyan")
            table.add_column("Roll Number", style="cyan")
            table.add_column("5th Core Name", style="cyan")
            table.add_column("English", style="magenta")
            table.add_column("Accounts", style="magenta")
            table.add_column("Business Studies", style="magenta")
            table.add_column("Economics", style="magenta")
            table.add_column("5th Core", style="magenta")
            table.add_column("Total", style="red")
            table.add_column("Average %", style="red")
            for i in range(len(res)):
                table.add_row(
                    str(res[i][0]),
                    str(res[i][1]),
                    str(res[i][2]),
                    str(res[i][3]),
                    str(res[i][4]),
                    str(res[i][5]),
                    str(res[i][6]),
                    str(res[i][7]),
                    str(res[i][8]),
                    str(res[i][9]),
                    str(res[i][10]),
                    str(res[i][11]),
                    str(res[i][12]),
                )
            console.print(table)
        else:
            print()
            print(f"There are no students in Grade {Grade} CEC")

        # ? Humanities
        cur.execute(f"select * from {db}.cateight where class={Class}")
        res = cur.fetchall()
        if len(res) != 0:
            res = [x for x in res]
            table = Table(show_header=True, header_style="bold", box=box.ROUNDED)
            table.add_column("Admission Number", style="green")
            table.add_column("Name", style="cyan")
            table.add_column("Class", style="cyan")
            table.add_column("Section", style="cyan")
            table.add_column("Roll Number", style="cyan")
            table.add_column("5th Core Name", style="cyan")
            table.add_column("English", style="magenta")
            table.add_column("History", style="magenta")
            table.add_column("Political Sciences", style="magenta")
            table.add_column("Economics", style="magenta")
            table.add_column("5th Core", style="magenta")
            table.add_column("Total", style="red")
            table.add_column("Average %", style="red")
            for i in range(len(res)):
                table.add_row(
                    str(res[i][0]),
                    str(res[i][1]),
                    str(res[i][2]),
                    str(res[i][3]),
                    str(res[i][4]),
                    str(res[i][5]),
                    str(res[i][6]),
                    str(res[i][7]),
                    str(res[i][8]),
                    str(res[i][9]),
                    str(res[i][10]),
                    str(res[i][11]),
                    str(res[i][12]),
                )
            console.print(table)
            input()
        else:
            print()
            print(f"There are no students in Grade {Grade} Humanities")
            input()
        ClearScreen()


# ! <-- Displaying all students in the school -->


def SchoolRecords():
    # ? Clearing the screen
    global grade1, grade2, grade3, grade4, grade5, grade6, grade7, grade8, grade9, grade10, mpc11, mpc12, bipc11, bipc12, cec11, cec12, human11, human12
    ClearScreen()

    # ? Grade 1
    cur.execute(f"select * from {db}.catone where class=1")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        grade1 = Table(show_header=True, header_style="bold", box=box.ROUNDED)
        grade1.add_column("Admission Number", style="green")
        grade1.add_column("Name", style="cyan")
        grade1.add_column("Class", style="cyan")
        grade1.add_column("Section", style="cyan")
        grade1.add_column("Roll Number", style="cyan")
        grade1.add_column("2nd Language Name", style="cyan")
        grade1.add_column("English", style="magenta")
        grade1.add_column("Mathematics", style="magenta")
        grade1.add_column("Science", style="magenta")
        grade1.add_column("Social Sciences", style="magenta")
        grade1.add_column("2nd Language", style="magenta")
        grade1.add_column("Total", style="red")
        grade1.add_column("Average %", style="red")
        for i in range(len(res)):
            grade1.add_row(
                str(res[i][0]),
                str(res[i][1]),
                str(res[i][2]),
                str(res[i][3]),
                str(res[i][4]),
                str(res[i][5]),
                str(res[i][6]),
                str(res[i][7]),
                str(res[i][8]),
                str(res[i][9]),
                str(res[i][10]),
                str(res[i][11]),
                str(res[i][12]),
            )
    else:
        grade1 = False

    # ? Grade 2
    cur.execute(f"select * from {db}.cattwo where class=2")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        grade2 = Table(show_header=True, header_style="bold", box=box.ROUNDED)
        grade2.add_column("Admission Number", style="green")
        grade2.add_column("Name", style="cyan")
        grade2.add_column("Class", style="cyan")
        grade2.add_column("Section", style="cyan")
        grade2.add_column("Roll Number", style="cyan")
        grade2.add_column("2nd Language Name", style="cyan")
        grade2.add_column("English", style="magenta")
        grade2.add_column("Mathematics", style="magenta")
        grade2.add_column("Science", style="magenta")
        grade2.add_column("Social Sciences", style="magenta")
        grade2.add_column("2nd Language", style="magenta")
        grade2.add_column("Computers", style="magenta")
        grade2.add_column("Total", style="red")
        grade2.add_column("Average %", style="red")
        for i in range(len(res)):
            grade2.add_row(
                str(res[i][0]),
                str(res[i][1]),
                str(res[i][2]),
                str(res[i][3]),
                str(res[i][4]),
                str(res[i][5]),
                str(res[i][6]),
                str(res[i][7]),
                str(res[i][8]),
                str(res[i][9]),
                str(res[i][10]),
                str(res[i][11]),
                str(res[i][12]),
                str(res[i][13]),
            )
    else:
        grade2 = False

    # ? Grade 3
    cur.execute(f"select * from {db}.cattwo where class=3")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        grade3 = Table(show_header=True, header_style="bold", box=box.ROUNDED)
        grade3.add_column("Admission Number", style="green")
        grade3.add_column("Name", style="cyan")
        grade3.add_column("Class", style="cyan")
        grade3.add_column("Section", style="cyan")
        grade3.add_column("Roll Number", style="cyan")
        grade3.add_column("2nd Language Name", style="cyan")
        grade3.add_column("English", style="magenta")
        grade3.add_column("Mathematics", style="magenta")
        grade3.add_column("Science", style="magenta")
        grade3.add_column("Social Sciences", style="magenta")
        grade3.add_column("2nd Language", style="magenta")
        grade3.add_column("Computers", style="magenta")
        grade3.add_column("Total", style="red")
        grade3.add_column("Average %", style="red")
        for i in range(len(res)):
            grade3.add_row(
                str(res[i][0]),
                str(res[i][1]),
                str(res[i][2]),
                str(res[i][3]),
                str(res[i][4]),
                str(res[i][5]),
                str(res[i][6]),
                str(res[i][7]),
                str(res[i][8]),
                str(res[i][9]),
                str(res[i][10]),
                str(res[i][11]),
                str(res[i][12]),
                str(res[i][13]),
            )
    else:
        grade3 = False

    # ? Grade 4
    cur.execute(f"select * from {db}.cattwo where class=4")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        grade4 = Table(show_header=True, header_style="bold", box=box.ROUNDED)
        grade4.add_column("Admission Number", style="green")
        grade4.add_column("Name", style="cyan")
        grade4.add_column("Class", style="cyan")
        grade4.add_column("Section", style="cyan")
        grade4.add_column("Roll Number", style="cyan")
        grade4.add_column("2nd Language Name", style="cyan")
        grade4.add_column("English", style="magenta")
        grade4.add_column("Mathematics", style="magenta")
        grade4.add_column("Science", style="magenta")
        grade4.add_column("Social Sciences", style="magenta")
        grade4.add_column("2nd Language", style="magenta")
        grade4.add_column("Computers", style="magenta")
        grade4.add_column("Total", style="red")
        grade4.add_column("Average %", style="red")
        for i in range(len(res)):
            grade4.add_row(
                str(res[i][0]),
                str(res[i][1]),
                str(res[i][2]),
                str(res[i][3]),
                str(res[i][4]),
                str(res[i][5]),
                str(res[i][6]),
                str(res[i][7]),
                str(res[i][8]),
                str(res[i][9]),
                str(res[i][10]),
                str(res[i][11]),
                str(res[i][12]),
                str(res[i][13]),
            )
    else:
        grade4 = False

    # ? Grade 5
    cur.execute(f"select * from {db}.catthree where class=5")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        grade5 = Table(show_header=True, header_style="bold", box=box.ROUNDED)
        grade5.add_column("Admission Number", style="green")
        grade5.add_column("Name", style="cyan")
        grade5.add_column("Class", style="cyan")
        grade5.add_column("Section", style="cyan")
        grade5.add_column("Roll Number", style="cyan")
        grade5.add_column("2nd Language Name", style="cyan")
        grade5.add_column("3rd Language Name", style="cyan")
        grade5.add_column("English", style="magenta")
        grade5.add_column("Mathematics", style="magenta")
        grade5.add_column("Science", style="magenta")
        grade5.add_column("Social Sciences", style="magenta")
        grade5.add_column("2nd Language", style="magenta")
        grade5.add_column("3rd Language", style="magenta")
        grade5.add_column("Computers", style="magenta")
        grade5.add_column("Total", style="red")
        grade5.add_column("Average %", style="red")
        for i in range(len(res)):
            grade5.add_row(
                str(res[i][0]),
                str(res[i][1]),
                str(res[i][2]),
                str(res[i][3]),
                str(res[i][4]),
                str(res[i][5]),
                str(res[i][6]),
                str(res[i][7]),
                str(res[i][8]),
                str(res[i][9]),
                str(res[i][10]),
                str(res[i][11]),
                str(res[i][12]),
                str(res[i][13]),
                str(res[i][14]),
                str(res[i][15]),
            )
    else:
        grade5 = False

    # ? Grade 6
    cur.execute(f"select * from {db}.catthree where class=6")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        grade6 = Table(show_header=True, header_style="bold", box=box.ROUNDED)
        grade6.add_column("Admission Number", style="green")
        grade6.add_column("Name", style="cyan")
        grade6.add_column("Class", style="cyan")
        grade6.add_column("Section", style="cyan")
        grade6.add_column("Roll Number", style="cyan")
        grade6.add_column("2nd Language Name", style="cyan")
        grade6.add_column("3rd Language Name", style="cyan")
        grade6.add_column("English", style="magenta")
        grade6.add_column("Mathematics", style="magenta")
        grade6.add_column("Science", style="magenta")
        grade6.add_column("Social Sciences", style="magenta")
        grade6.add_column("2nd Language", style="magenta")
        grade6.add_column("3rd Language", style="magenta")
        grade6.add_column("Computers", style="magenta")
        grade6.add_column("Total", style="red")
        grade6.add_column("Average %", style="red")
        for i in range(len(res)):
            grade6.add_row(
                str(res[i][0]),
                str(res[i][1]),
                str(res[i][2]),
                str(res[i][3]),
                str(res[i][4]),
                str(res[i][5]),
                str(res[i][6]),
                str(res[i][7]),
                str(res[i][8]),
                str(res[i][9]),
                str(res[i][10]),
                str(res[i][11]),
                str(res[i][12]),
                str(res[i][13]),
                str(res[i][14]),
                str(res[i][15]),
            )
    else:
        grade6 = False

    # ? Grade 7
    cur.execute(f"select * from {db}.catthree where class=7")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        grade7 = Table(show_header=True, header_style="bold", box=box.ROUNDED)
        grade7.add_column("Admission Number", style="green")
        grade7.add_column("Name", style="cyan")
        grade7.add_column("Class", style="cyan")
        grade7.add_column("Section", style="cyan")
        grade7.add_column("Roll Number", style="cyan")
        grade7.add_column("2nd Language Name", style="cyan")
        grade7.add_column("3rd Language Name", style="cyan")
        grade7.add_column("English", style="magenta")
        grade7.add_column("Mathematics", style="magenta")
        grade7.add_column("Science", style="magenta")
        grade7.add_column("Social Sciences", style="magenta")
        grade7.add_column("2nd Language", style="magenta")
        grade7.add_column("3rd Language", style="magenta")
        grade7.add_column("Computers", style="magenta")
        grade7.add_column("Total", style="red")
        grade7.add_column("Average %", style="red")
        for i in range(len(res)):
            grade7.add_row(
                str(res[i][0]),
                str(res[i][1]),
                str(res[i][2]),
                str(res[i][3]),
                str(res[i][4]),
                str(res[i][5]),
                str(res[i][6]),
                str(res[i][7]),
                str(res[i][8]),
                str(res[i][9]),
                str(res[i][10]),
                str(res[i][11]),
                str(res[i][12]),
                str(res[i][13]),
                str(res[i][14]),
                str(res[i][15]),
            )
    else:
        grade7 = False

    # ? Grade 8
    cur.execute(f"select * from {db}.catthree where class=8")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        grade8 = Table(show_header=True, header_style="bold", box=box.ROUNDED)
        grade8.add_column("Admission Number", style="green")
        grade8.add_column("Name", style="cyan")
        grade8.add_column("Class", style="cyan")
        grade8.add_column("Section", style="cyan")
        grade8.add_column("Roll Number", style="cyan")
        grade8.add_column("2nd Language Name", style="cyan")
        grade8.add_column("3rd Language Name", style="cyan")
        grade8.add_column("English", style="magenta")
        grade8.add_column("Mathematics", style="magenta")
        grade8.add_column("Science", style="magenta")
        grade8.add_column("Social Sciences", style="magenta")
        grade8.add_column("2nd Language", style="magenta")
        grade8.add_column("3rd Language", style="magenta")
        grade8.add_column("Computers", style="magenta")
        grade8.add_column("Total", style="red")
        grade8.add_column("Average %", style="red")
        for i in range(len(res)):
            grade8.add_row(
                str(res[i][0]),
                str(res[i][1]),
                str(res[i][2]),
                str(res[i][3]),
                str(res[i][4]),
                str(res[i][5]),
                str(res[i][6]),
                str(res[i][7]),
                str(res[i][8]),
                str(res[i][9]),
                str(res[i][10]),
                str(res[i][11]),
                str(res[i][12]),
                str(res[i][13]),
                str(res[i][14]),
                str(res[i][15]),
            )
    else:
        grade8 = False

    # ? Grade 9
    cur.execute(f"select * from {db}.catfour where class=9")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        grade9 = Table(show_header=True, header_style="bold", box=box.ROUNDED)
        grade9.add_column("Admission Number", style="green")
        grade9.add_column("Name", style="cyan")
        grade9.add_column("Class", style="cyan")
        grade9.add_column("Section", style="cyan")
        grade9.add_column("Roll Number", style="cyan")
        grade9.add_column("2nd Language Name", style="cyan")
        grade9.add_column("English", style="magenta")
        grade9.add_column("Mathematics", style="magenta")
        grade9.add_column("Science", style="magenta")
        grade9.add_column("Social Sciences", style="magenta")
        grade9.add_column("2nd Language", style="magenta")
        grade9.add_column("Total", style="red")
        grade9.add_column("Average %", style="red")
        for i in range(len(res)):
            grade9.add_row(
                str(res[i][0]),
                str(res[i][1]),
                str(res[i][2]),
                str(res[i][3]),
                str(res[i][4]),
                str(res[i][5]),
                str(res[i][6]),
                str(res[i][7]),
                str(res[i][8]),
                str(res[i][9]),
                str(res[i][10]),
                str(res[i][11]),
                str(res[i][12]),
            )
    else:
        grade9 = False

    # ? Grade 10
    cur.execute(f"select * from {db}.catfour where class=10")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        grade10 = Table(show_header=True, header_style="bold", box=box.ROUNDED)
        grade10.add_column("Admission Number", style="green")
        grade10.add_column("Name", style="cyan")
        grade10.add_column("Class", style="cyan")
        grade10.add_column("Section", style="cyan")
        grade10.add_column("Roll Number", style="cyan")
        grade10.add_column("2nd Language Name", style="cyan")
        grade10.add_column("English", style="magenta")
        grade10.add_column("Mathematics", style="magenta")
        grade10.add_column("Science", style="magenta")
        grade10.add_column("Social Sciences", style="magenta")
        grade10.add_column("2nd Language", style="magenta")
        grade10.add_column("Total", style="red")
        grade10.add_column("Average %", style="red")
        for i in range(len(res)):
            grade10.add_row(
                str(res[i][0]),
                str(res[i][1]),
                str(res[i][2]),
                str(res[i][3]),
                str(res[i][4]),
                str(res[i][5]),
                str(res[i][6]),
                str(res[i][7]),
                str(res[i][8]),
                str(res[i][9]),
                str(res[i][10]),
                str(res[i][11]),
                str(res[i][12]),
            )
    else:
        grade10 = False

    # ? Mathematics, Physics, Chemistry - 11
    cur.execute(f"select * from {db}.catfive where class=11")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        mpc11 = Table(show_header=True, header_style="bold", box=box.ROUNDED)
        mpc11.add_column("Admission Number", style="green")
        mpc11.add_column("Name", style="cyan")
        mpc11.add_column("Class", style="cyan")
        mpc11.add_column("Section", style="cyan")
        mpc11.add_column("Roll Number", style="cyan")
        mpc11.add_column("5th Core Name", style="cyan")
        mpc11.add_column("English", style="magenta")
        mpc11.add_column("Mathematics", style="magenta")
        mpc11.add_column("Physics", style="magenta")
        mpc11.add_column("Chemistry", style="magenta")
        mpc11.add_column("5th Core", style="magenta")
        mpc11.add_column("Total", style="red")
        mpc11.add_column("Average %", style="red")
        for i in range(len(res)):
            mpc11.add_row(
                str(res[i][0]),
                str(res[i][1]),
                str(res[i][2]),
                str(res[i][3]),
                str(res[i][4]),
                str(res[i][5]),
                str(res[i][6]),
                str(res[i][7]),
                str(res[i][8]),
                str(res[i][9]),
                str(res[i][10]),
                str(res[i][11]),
                str(res[i][12]),
            )
    else:
        mpc11 = False

    # ? Mathematics, Physics, Chemistry - 12
    cur.execute(f"select * from {db}.catfive where class=12")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        mpc12 = Table(show_header=True, header_style="bold", box=box.ROUNDED)
        mpc12.add_column("Admission Number", style="green")
        mpc12.add_column("Name", style="cyan")
        mpc12.add_column("Class", style="cyan")
        mpc12.add_column("Section", style="cyan")
        mpc12.add_column("Roll Number", style="cyan")
        mpc12.add_column("5th Core Name", style="cyan")
        mpc12.add_column("English", style="magenta")
        mpc12.add_column("Mathematics", style="magenta")
        mpc12.add_column("Physics", style="magenta")
        mpc12.add_column("Chemistry", style="magenta")
        mpc12.add_column("5th Core", style="magenta")
        mpc12.add_column("Total", style="red")
        mpc12.add_column("Average %", style="red")
        for i in range(len(res)):
            mpc12.add_row(
                str(res[i][0]),
                str(res[i][1]),
                str(res[i][2]),
                str(res[i][3]),
                str(res[i][4]),
                str(res[i][5]),
                str(res[i][6]),
                str(res[i][7]),
                str(res[i][8]),
                str(res[i][9]),
                str(res[i][10]),
                str(res[i][11]),
                str(res[i][12]),
            )
    else:
        mpc12 = False

    # ? Biology, Physics, Chemistry - 11
    cur.execute(f"select * from {db}.catsix where class=11")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        bipc11 = Table(show_header=True, header_style="bold", box=box.ROUNDED)
        bipc11.add_column("Admission Number", style="green")
        bipc11.add_column("Name", style="cyan")
        bipc11.add_column("Class", style="cyan")
        bipc11.add_column("Section", style="cyan")
        bipc11.add_column("Roll Number", style="cyan")
        bipc11.add_column("5th Core Name", style="cyan")
        bipc11.add_column("English", style="magenta")
        bipc11.add_column("Biology", style="magenta")
        bipc11.add_column("Physics", style="magenta")
        bipc11.add_column("Chemistry", style="magenta")
        bipc11.add_column("5th Core", style="magenta")
        bipc11.add_column("Total", style="red")
        bipc11.add_column("Average %", style="red")
        for i in range(len(res)):
            bipc11.add_row(
                str(res[i][0]),
                str(res[i][1]),
                str(res[i][2]),
                str(res[i][3]),
                str(res[i][4]),
                str(res[i][5]),
                str(res[i][6]),
                str(res[i][7]),
                str(res[i][8]),
                str(res[i][9]),
                str(res[i][10]),
                str(res[i][11]),
                str(res[i][12]),
            )
    else:
        bipc11 = False

    # ? Biology, Physics, Chemistry - 12
    cur.execute(f"select * from {db}.catsix where class=12")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        bipc12 = Table(show_header=True, header_style="bold", box=box.ROUNDED)
        bipc12.add_column("Admission Number", style="green")
        bipc12.add_column("Name", style="cyan")
        bipc12.add_column("Class", style="cyan")
        bipc12.add_column("Section", style="cyan")
        bipc12.add_column("Roll Number", style="cyan")
        bipc12.add_column("5th Core Name", style="cyan")
        bipc12.add_column("English", style="magenta")
        bipc12.add_column("Biology", style="magenta")
        bipc12.add_column("Physics", style="magenta")
        bipc12.add_column("Chemistry", style="magenta")
        bipc12.add_column("5th Core", style="magenta")
        bipc12.add_column("Total", style="red")
        bipc12.add_column("Average %", style="red")
        for i in range(len(res)):
            bipc12.add_row(
                str(res[i][0]),
                str(res[i][1]),
                str(res[i][2]),
                str(res[i][3]),
                str(res[i][4]),
                str(res[i][5]),
                str(res[i][6]),
                str(res[i][7]),
                str(res[i][8]),
                str(res[i][9]),
                str(res[i][10]),
                str(res[i][11]),
                str(res[i][12]),
            )
    else:
        bipc12 = False

    # ? Commerce - 11
    cur.execute(f"select * from {db}.catseven where class=11")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        cec11 = Table(show_header=True, header_style="bold", box=box.ROUNDED)
        cec11.add_column("Admission Number", style="green")
        cec11.add_column("Name", style="cyan")
        cec11.add_column("Class", style="cyan")
        cec11.add_column("Section", style="cyan")
        cec11.add_column("Roll Number", style="cyan")
        cec11.add_column("5th Core Name", style="cyan")
        cec11.add_column("English", style="magenta")
        cec11.add_column("Accounts", style="magenta")
        cec11.add_column("Business Studies", style="magenta")
        cec11.add_column("Economics", style="magenta")
        cec11.add_column("5th Core", style="magenta")
        cec11.add_column("Total", style="red")
        cec11.add_column("Average %", style="red")
        for i in range(len(res)):
            cec11.add_row(
                str(res[i][0]),
                str(res[i][1]),
                str(res[i][2]),
                str(res[i][3]),
                str(res[i][4]),
                str(res[i][5]),
                str(res[i][6]),
                str(res[i][7]),
                str(res[i][8]),
                str(res[i][9]),
                str(res[i][10]),
                str(res[i][11]),
                str(res[i][12]),
            )
    else:
        cec11 = False

    # ? Commerce - 12
    cur.execute(f"select * from {db}.catseven where class=12")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        cec12 = Table(show_header=True, header_style="bold", box=box.ROUNDED)
        cec12.add_column("Admission Number", style="green")
        cec12.add_column("Name", style="cyan")
        cec12.add_column("Class", style="cyan")
        cec12.add_column("Section", style="cyan")
        cec12.add_column("Roll Number", style="cyan")
        cec12.add_column("5th Core Name", style="cyan")
        cec12.add_column("English", style="magenta")
        cec12.add_column("Accounts", style="magenta")
        cec12.add_column("Business Studies", style="magenta")
        cec12.add_column("Economics", style="magenta")
        cec12.add_column("5th Core", style="magenta")
        cec12.add_column("Total", style="red")
        cec12.add_column("Average %", style="red")
        for i in range(len(res)):
            cec12.add_row(
                str(res[i][0]),
                str(res[i][1]),
                str(res[i][2]),
                str(res[i][3]),
                str(res[i][4]),
                str(res[i][5]),
                str(res[i][6]),
                str(res[i][7]),
                str(res[i][8]),
                str(res[i][9]),
                str(res[i][10]),
                str(res[i][11]),
                str(res[i][12]),
            )
    else:
        cec12 = False

    # ? Humanities - 11
    cur.execute(f"select * from {db}.cateight where class=11")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        human11 = Table(show_header=True, header_style="bold", box=box.ROUNDED)
        human11.add_column("Admission Number", style="green")
        human11.add_column("Name", style="cyan")
        human11.add_column("Class", style="cyan")
        human11.add_column("Section", style="cyan")
        human11.add_column("Roll Number", style="cyan")
        human11.add_column("5th Core Name", style="cyan")
        human11.add_column("English", style="magenta")
        human11.add_column("History", style="magenta")
        human11.add_column("Political Sciences", style="magenta")
        human11.add_column("Economics", style="magenta")
        human11.add_column("5th Core", style="magenta")
        human11.add_column("Total", style="red")
        human11.add_column("Average %", style="red")
        for i in range(len(res)):
            human11.add_row(
                str(res[i][0]),
                str(res[i][1]),
                str(res[i][2]),
                str(res[i][3]),
                str(res[i][4]),
                str(res[i][5]),
                str(res[i][6]),
                str(res[i][7]),
                str(res[i][8]),
                str(res[i][9]),
                str(res[i][10]),
                str(res[i][11]),
                str(res[i][12]),
            )
    else:
        human11 = False

    # ? Humanities - 12
    cur.execute(f"select * from {db}.cateight where class=12")
    res = cur.fetchall()
    if len(res) != 0:
        res = [x for x in res]
        human12 = Table(show_header=True, header_style="bold", box=box.ROUNDED)
        human12.add_column("Admission Number", style="green")
        human12.add_column("Name", style="cyan")
        human12.add_column("Class", style="cyan")
        human12.add_column("Section", style="cyan")
        human12.add_column("Roll Number", style="cyan")
        human12.add_column("5th Core Name", style="cyan")
        human12.add_column("English", style="magenta")
        human12.add_column("History", style="magenta")
        human12.add_column("Political Sciences", style="magenta")
        human12.add_column("Economics", style="magenta")
        human12.add_column("5th Core", style="magenta")
        human12.add_column("Total", style="red")
        human12.add_column("Average %", style="red")
        for i in range(len(res)):
            human12.add_row(
                str(res[i][0]),
                str(res[i][1]),
                str(res[i][2]),
                str(res[i][3]),
                str(res[i][4]),
                str(res[i][5]),
                str(res[i][6]),
                str(res[i][7]),
                str(res[i][8]),
                str(res[i][9]),
                str(res[i][10]),
                str(res[i][11]),
                str(res[i][12]),
            )
    else:
        human12 = False

    tree = Tree("Indus Universal School")
    if grade1:
        tree.add("Grade 1").add(grade1)
    else:
        tree.add("Grade 1").add("None")
    if grade2:
        tree.add("Grade 2").add(grade2)
    else:
        tree.add("Grade 2").add("None")
    if grade3:
        tree.add("Grade 3").add(grade3)
    else:
        tree.add("Grade 3").add("None")
    if grade4:
        tree.add("Grade 4").add(grade4)
    else:
        tree.add("Grade 4").add("None")
    if grade5:
        tree.add("Grade 5").add(grade5)
    else:
        tree.add("Grade 5").add("None")
    if grade6:
        tree.add("Grade 6").add(grade6)
    else:
        tree.add("Grade 6").add("None")
    if grade7:
        tree.add("Grade 7").add(grade7)
    else:
        tree.add("Grade 7").add("None")
    if grade8:
        tree.add("Grade 8").add(grade8)
    else:
        tree.add("Grade 8").add("None")
    if grade9:
        tree.add("Grade 9").add(grade9)
    else:
        tree.add("Grade 9").add("None")
    if grade10:
        tree.add("Grade 10").add(grade10)
    else:
        tree.add("Grade 10").add("None")

    grade11 = tree.add("Grade 11")
    if mpc11:
        grade11.add("MPC").add(mpc11)
    else:
        grade11.add("MPC").add("None")
    if bipc11:
        grade11.add("BiPC").add(bipc11)
    else:
        grade11.add("BiPC").add("None")
    if cec11:
        grade11.add("CEC").add(cec11)
    else:
        grade11.add("CEC").add("None")
    if human11:
        grade11.add("Humanities").add(human11)
    else:
        grade11.add("Humanities").add("None")

    grade12 = tree.add("Grade 12")
    if mpc12:
        grade12.add("MPC").add(mpc12)
    else:
        grade12.add("MPC").add("None")
    if bipc12:
        grade12.add("BiPC").add(bipc12)
    else:
        grade12.add("BiPC").add("None")
    if cec12:
        grade12.add("CEC").add(cec12)
    else:
        grade12.add("CEC").add("None")
    if human12:
        grade12.add("Humanities").add(human12)
    else:
        grade12.add("Humanities").add("None")

    console.print(tree)
    input()


# endregion
#! --------------------------------------------------
#! --------------------------------------------------


#! --------------------------------------------------
#! ---------- Running the program
#! --------------------------------------------------
# region Running the program
########! Imports !########
########! Required for the script to work !########
# ? This runs basic functions such as creating requried databases and tables as well as basic vairables.
Backend()

########! Printing Options on the Screen !########
# ? Login, if username and password do not exist, it will ask if you want to create a user.
# ? Add attributes if you want to provide username and password
# ? For example: LoginUser('Username', 'Password')
LoginUser('hussain', '16computers')

while True:
    # ? Clearing the screen
    ClearScreen()
    # ? Printing the options

    choice = questionary.select(
        "What do you want to do?",
        choices=[
            "Student information",
            "Marks information",
            "Records",
            "Back",
            "Quit",
        ],style=minimalStyle, instruction="\n"
    ).ask()

    ClearScreen()
    if choice == "Student information":
        studentInfoChoice = questionary.select(
            "What do you want to do?",
            choices=[
                "Add a student",
                "Edit a student",
                "Remove a student",
                "Back",
                "Quit",
            ], style=minimalStyle, instruction="\n"
        ).ask()

        if studentInfoChoice == "Add a student":
            AddStudent()
        elif studentInfoChoice == "Edit a student":
            EditStudent()
        elif studentInfoChoice == "Remove a student":
            RemoveStudent()
        elif studentInfoChoice == "Back":
            ClearScreen()
        else:
            # ? If quit is called or a bad choice is given
            exit()
    elif choice == "Marks information":
        marksInfoChoice = questionary.select(
            "What do you want to do?",
            choices=["Add marks", "Edit marks", "Remove marks", "Quit"], style=minimalStyle, instruction="\n"
        ).ask()
        if marksInfoChoice == "Add marks":
            AddMarks()
        elif marksInfoChoice == "Edit marks":
            EditMarks()
        elif marksInfoChoice == "Remove marks":
            RemoveMarks()
        elif marksInfoChoice == "Back":
            ClearScreen()
        else:
            # ? If quit is called or a bad choice is given
            exit()
    elif choice == "Records":
        recordsChoice = questionary.select(
            "What do you want to do?",
            choices=[
                "Student Records",
                "Class Records",
                "School Records",
                "Show Subject-Marks Graph",
                "Back",
                "Quit",
            ], style=minimalStyle, instruction="\n"
        ).ask()

        if recordsChoice == "Student Records":
            StudentRecords()
        elif recordsChoice == "Class Records":
            ClassRecords()
        elif recordsChoice == "School Records":
            SchoolRecords()
        elif recordsChoice == "Show Subject-Marks Graph":
            ShowGraph()
        elif recordsChoice == "Back":
            ClearScreen()
        else:
            # ? If quit is called or a bad choice is given
            exit()
    else:
        # ? If quit is called or a bad choice is given
        exit()
# endregion
#! --------------------------------------------------
#! --------------------------------------------------
# Ending of the program
