##
# ! Function to edit the inputted content to our desired parameters
def BetterInput(prompt, filter="None", type=str):
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
        except KeyboardInterrupt:
            exit()
        except:
            print("Enter a proper value.")

def IsProperMarks(prompt):
   # ? To check for input parameters and returning the desired input. 
    while True:
        try:
            marks = round(float(input(prompt)))
            if 0 > marks or marks > 100:
                raise AttributeError
            else:
                return marks
        except KeyboardInterrupt:
            exit()
        except AttributeError:
            print(f"Marks need to be less than 100 and greater than 0.")
        except:
            print('Enter valid marks.')


# ! Function to avoid getting an error on a wrong yes/no question
def IsProperAnswer(answer):
    while True:
        if answer not in ['yes', 'no']:
            answer = input("Please type either yes or no: ").lower()
        else:
            return answer

# ! Function to avoid getting an error on an improper name
def IsProperName(name):
    from string import digits, punctuation

    NumericSymbols = [x for x in digits + punctuation]
    while True:
        try:
            for i in name:
                if i in NumericSymbols:
                    raise ValueError
            else:
                return name
        except KeyboardInterrupt:
            exit()
        except:
            name = BetterInput("Enter a valid student's name: ", "sentence", str)

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
        except KeyboardInterrupt:
            exit()
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
        except KeyboardInterrupt:
            exit()
        except:
            # ? If checks fail, ask for an input again

            Fcore = BetterInput("Enter a valid 5th core: ", "sentence", str)

# ! Function to avoid getting an error on choosing a 2nd language, without including French
def IsProperLang2WOF(Lang2Name):
    while True:
        try:
            if Lang2Name.lower() not in ["hindi", "h", "telugu", "t"]:
                raise ValueError
            else:
                if Lang2Name.lower() == "h":
                    Lang2Name = "Hindi"
                if Lang2Name.lower() == "t":
                    Lang2Name = "Telugu"
                return Lang2Name
        except KeyboardInterrupt:
            exit()
        except:
            Lang2Name = BetterInput("Enter a valid 2nd Language: ", "sentence", str)

# ! Function to avoid getting an error on choosing a 2nd language, including French
def IsProperLang2WF(Lang2Name):
    while True:
        try:
            if Lang2Name.lower() not in ["hindi", "h", "telugu", "t", "french", "f"]:
                raise ValueError
            else:
                if Lang2Name.lower() == "h":
                    Lang2Name = "Hindi"
                if Lang2Name.lower() == "t":
                    Lang2Name = "Telugu"
                if Lang2Name.lower() == "f":
                    Lang2Name = "French"
                return Lang2Name
        except KeyboardInterrupt:
            exit()
        except:
            Lang2Name = BetterInput("Enter a valid 2nd Language: ", "sentence", str)

# ! Function to avoid getting an error on choosing a 3rd language
def IsProperLang3(Lang3Name, Lang2Name):
    while True:
        try:
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
        except KeyboardInterrupt:
            exit()
        except:
            Lang3Name = BetterInput("Enter a valid 3rd Language: ", "sentence", str)

# ! Function to avoid getting an error on a wrong roll number input
def IsProperRollNum(RollNum):
    while True:
        try:
            if RollNum > 60:
                raise ValueError
            else:
                return RollNum
        except KeyboardInterrupt:
            exit()
        except:
            RollNum = BetterInput("Enter a valid roll number: ", "+", int)

# ! Function to clear the terminal screen depending on OS type
def ClearScreen():
    from time import sleep
    from os import system, name
    sleep(0.5)
    if name == 'posix':
        system('clear')
    elif name == 'nt':
        system('cls')
    print("-" * 70)
    print("-" * 10, "This is a Student Management system")
    print("-" * 70)
    print()
    
