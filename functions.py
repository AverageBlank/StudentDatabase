def BetterInput(prompt, filter="None", type=str):
    while True:
        try:
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
            elif type == int:
                inp = int(input(prompt))
                if filter.lower() in ["positive", "+"]:
                    return abs(inp)
                elif filter.lower() in ["negative", "-"]:
                    return -abs(inp)
                else:
                    return inp
            elif type == float:
                inp = float(input(prompt))
                if filter.lower() in ["positive", "+"]:
                    return abs(inp)
                elif filter.lower() in ["negative", "-"]:
                    return -abs(inp)
                else:
                    return inp
        except:
            print("Enter a proper value.")


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
        except:
            name = BetterInput("Enter a valid student's name: ", "sentence", str)


def IsProperStream(stream):
    while True:
        try:
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
                if stream == "pcm":
                    stream = "mpc"
                if stream == "commerce":
                    stream = "cec"
                if stream == "human":
                    stream = "humanities"
                return stream
        except:
            stream = BetterInput("Enter a valid stream: ", "sentence", str)


def IsProperFcore(Fcore, Stream):
    while True:
        try:
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
            Fcore = BetterInput("Enter a valid 5th core: ", "sentence", str)


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
        except:
            Lang2Name = BetterInput("Enter a valid 2nd Language: ", "sentence", str)


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

        except:
            Lang2Name = BetterInput("Enter a valid 2nd Language: ", "sentence", str)


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

        except:
            Lang3Name = BetterInput("Enter a valid 3rd Language: ", "sentence", str)


def IsProperRollNum(RollNum):
    while True:
        try:
            if RollNum > 60:
                raise ValueError
            else:
                return RollNum
        except:
            RollNum = BetterInput("Enter a valid roll number: ", "+", int)
