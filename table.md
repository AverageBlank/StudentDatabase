# 1 -

Name
Class
Section
RollNumber
English
Maths
Science
Social Sciences
Lang2Name
Lang2
Average
Total

# 2-4

Name
Class
Section
RollNumber
English
Maths
Science
Social Sciences
Lang2Name
Lang2
Computers
Average
Total

# 5-8

Name
Class
Section
RollNumber
English
Maths
Science
Social Sciences
Lang2Name
Lang2
Lang3Name
Lang3
Computers
Average
Total

# 9-10

Name
Class
Section
RollNumber
English
Maths
Science
Social Sciences
Lang2Name
Lang2
Average
Total

# MPC

Name
Class
Section
RollNumber
English
Maths
Physics
Chemistry
FcoreName
Fcore
Average
Total

# BiPC

Name
Class
Section
RollNumber
English
Biology
Physics
Chemistry
FcoreName
Fcore
Average
Total

# CEC

Name
Class
Section
RollNumber
English
Accounts
Business Studies
Economics
FcoreName
Fcore
Average
Total

# Human Titties

Name
Class
Section
RollNumber
English
History
Political Sciences
Economics
FcoreName
Fcore
Average
Total

# Code for getting classes

AdmNum = BetterInput(f"Enter admission number to view student's records: ", "+", int)
while True:
cur.execute(f"select class from {db}.AllStudents where AdmNum={AdmNum}")
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

elif 2 <= Class <= 4:

elif 5 <= Class <= 8:

elif 9 <= Class <= 10:

elif 11 <= Class <= 12:

"Admission Number": res[i][0],
"Name": res[i][1],
"Class": res[i][2],
"Section": res[i][3],
"Roll Number": res[i][4],
"2nd Language Name": res[i][5],
"English": res[i][6],
"Mathematics": res[i][7],
"Science": res[i][8],
"Social Sciences": res[i][9],
res[i][5]: res[i][10],
"Average %": res[i][11],
"Total": res[i][12],
