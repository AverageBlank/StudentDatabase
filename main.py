from time import sleep
import customtkinter as ctk
import pymysql


from TeacherBackend import (
    AddMarks,
    AddStudent,
    ChangePass,
    ClassRecords,
    EditMarks,
    EditStudent,
    LoginUser,
    RegisterUser,
    RemoveMarks,
    RemoveStudent,
    ShowGraph,
    StudentRecords,
    TBackend,
    SchoolRecords,
)

TBackend()
# RegisterUser()
# LoginUser()
# AddStudent()
# EditStudent()
# RemoveStudent()
# AddMarks()
# EditMarks()
# RemoveMarks()
# ShowGraph()
# StudentRecords()
# ClassRecords()
# SchoolRecords()

import customtkinter as ctk


window = ctk.CTk()
window.title("Student Management")
window.geometry("1280x720")
window.resizable(False, False)
window.configure()

frame = ctk.CTkFrame(master=window)


username = ctk.CTkEntry(master=frame, placeholder_text="Enter Username")
username.grid(row=0, column=0, sticky="n", pady=(20, 0))

password = ctk.CTkEntry(master=frame, show="*", placeholder_text="Enter Password")
password.grid(row=1, column=0, sticky="n", pady=(20, 0))

login = ctk.CTkButton(
    master=frame,
    command=lambda: LoginUser(username.get(), password.get()),
    text="Login",
)
login.grid(row=2, column=0, sticky="n", pady=(20, 0))

signup = ctk.CTkButton(
    master=frame,
    command=lambda: RegisterUser(username.get(), password.get()),
    text="Sign Up",
)
signup.grid(row=2, column=1, sticky="n", pady=(20, 0))


frame.pack()

window.mainloop()
