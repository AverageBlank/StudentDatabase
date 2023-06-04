##
########! Imports !########
from TeacherBackend import Backend, LoginUser, AddStudent, EditStudent, RegisterUser, RemoveStudent, EditMarks, AddMarks, RemoveMarks, ShowGraph, StudentRecords, ClassRecords, SchoolRecords
from functions import ClearScreen, BetterInput


########! Required for the script to work !########
# ? This runs basic functions such as creating requried databases and tables as well as basic vairables.
Backend()


########! Printing Options on the Screen !########
# ? Login, if username and password do not exist, it will ask if you want to create a user. 
# ? Add attributes if you want to provide username and password
# ? For example: LoginUser('Username', 'Password')
LoginUser()

while True:
    # ? Clearing the screen
    ClearScreen()
    # ? Printing the options
    print("Press 1 for student information")
    print("Press 2 for marks information")
    print("Press 3 for records")
    print("Press 0 to quit")
    choice = BetterInput("Enter your choice: ", "+", int, "Enter a valid number between 0 and 3.")
    ClearScreen()
    if choice == 1:
        # ? If student information is called
        print("Press 1 to add a student")
        print("Press 2 to edit a student")
        print("Press 3 to remove a student")
        print("Press 0 to quit")
        choice = BetterInput("Enter your choice: ", "+", int, "Enter a valid number between 0 and 3.")
        if choice == 1:
            AddStudent()
        elif choice == 2:
            EditStudent()
        elif choice == 3:
            RemoveStudent()
        else:
            # ? If quit is called or a bad choice is given
            exit()
    elif choice == 2:
        # ? If marks information is called
        print("Press 1 to add marks for a student")
        print("Press 2 to edit marks for a student")
        print("Press 3 to remove marks for a student")
        print("Press 4 to view a subject/marks graph for a student")
        print("Press 0 to quit")
        choice = BetterInput("Enter your choice: ", "+", int, "Enter a valid number between 0 and 4.")
        if choice == 1:
            AddMarks()
        elif choice == 2:
            EditMarks()
        elif choice == 3:
            RemoveMarks()
        elif choice == 4:
            ShowGraph()
        else:
            # ? If quit is called or a bad choice is given
            exit()
    elif choice == 3:
        # ? If records is called
        print("Press 1 to view student records")
        print("Press 2 to view class records")
        print("Press 3 to view the school's records")
        print("Press 0 to quit")
        choice = BetterInput("Enter your choice: ", "+", int, "Enter a valid number between 0 and 3.")
        if choice == 1:
            StudentRecords()
        elif choice == 2:
            ClassRecords()
        elif choice == 3:
            SchoolRecords()
        else:
            # ? If quit is called or a bad choice is given
            exit()
    else:
        # ? If quit is called or a bad choice is given
        exit()
