##
from functions import BetterInput, ClearScreen
from pandas import Series
from pymysql import connect
from matplotlib.pyplot import title, xlabel, ylabel, plot, show

# ! <-- Connecting to MySQL -->
db = "studentdatabase"
con = connect(host="localhost", user="root", password="16computers", database="mysql")
cur = con.cursor()


def StudentRecords():
    # ? Clearing the screen
    ClearScreen()
    # ? Admission Number
    AdmNum = BetterInput(
        f"Enter your admission number to view your records: ", "+", int
    )
    viewGraph = BetterInput(
        prompt=f"Would you like to view your marks in a graph? (Y/n): ",
        filter="lower",
        type=str,
    )
    if viewGraph in ["yes", "y", "ye", "ya"]:
        while True:
            cur.execute(f"select class from {db}.allstudents where AdmNum={AdmNum}")
            admNumFetch = cur.fetchall()
            try:
                if len(admNumFetch) == 0:
                    raise ValueError
                else:
                    break
            except KeyboardInterrupt:
                exit()
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
                marks = [res[6], res[7], res[8], res[9], res[10]]
                subs = ["English", "Mathematics", "Science", "Social Sciences", res[5]]
                title(f"{res[1]}'s marks")
                xlabel("Subjects")
                ylabel("Marks")
                plot(marks, subs)

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
                marks = [res[6], res[7], res[8], res[9], res[10], res[11]]
                subs = [
                    "English",
                    "Mathematics",
                    "Science",
                    "Social Sciences",
                    res[5],
                    "Computers",
                ]
                title(f"{res[1]}'s marks")
                xlabel("Subjects")
                ylabel("Marks")
                plot(marks, subs)
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
                marks = [res[7], res[8], res[9], res[10], res[11], res[12], res[13]]
                subs = [
                    "English",
                    "Mathematics",
                    "Science",
                    "Social Sciences",
                    res[5],
                    res[6],
                    "Computers",
                ]
                title(f"{res[1]}'s marks")
                xlabel("Subjects")
                ylabel("Marks")
                plot(marks, subs)
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
                marks = [res[6], res[7], res[8], res[9], res[10]]
                subs = ["English", "Mathematics", "Science", "Social Sciences", res[5]]
                title(f"{res[1]}'s marks")
                xlabel("Subjects")
                ylabel("Marks")
                plot(subs, marks)
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
                    marks = [res[6], res[7], res[8], res[9], res[10]]
                    subs = ["English", "Mathematics", "Physics", "Chemistry", res[5]]
                    title(f"{res[1]}'s marks")
                    xlabel("Subjects")
                    ylabel("Marks")
                    plot(subs, marks)
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
                    marks = [res[6], res[7], res[8], res[9], res[10]]
                    subs = ["English", "Biology", "Physics", "Chemistry", res[5]]
                    title(f"{res[1]}'s marks")
                    xlabel("Subjects")
                    ylabel("Marks")
                    plot(subs, marks)
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
                    marks = [res[6], res[7], res[8], res[9], res[10]]
                    subs = [
                        "English",
                        "Accounts",
                        "Business Studies",
                        "Economics",
                        res[5],
                    ]
                    title(f"{res[1]}'s marks")
                    xlabel("Subjects")
                    ylabel("Marks")
                    plot(subs, marks)

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
                    marks = [res[6], res[7], res[8], res[9], res[10]]
                    subs = [
                        "English",
                        "History",
                        "Political Sciences",
                        "Economics",
                        res[5],
                    ]
                    title(f"{res[1]}'s marks")
                    xlabel("Subjects")
                    ylabel("Marks")
                    plot(subs, marks)
        # ! Displaying Records/Report Card
        ClearScreen()
        print(prompt)
        print()
        Result = Series(result).to_string()
        print(Result)
        show()
    else:
        while True:
            cur.execute(f"select class from {db}.allstudents where AdmNum={AdmNum}")
            admNumFetch = cur.fetchall()
            try:
                if len(admNumFetch) == 0:
                    raise ValueError
                else:
                    break
            except KeyboardInterrupt:
                exit()
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
        ClearScreen()
        print(prompt)
        print()
        Result = Series(result).to_string()
        print(Result)


StudentRecords()