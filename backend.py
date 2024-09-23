def backClick(text):
    with open("info.txt", "a") as f:
        f.write("\n" + text + " ")
        f.close()

def backGetData():
    with open("info.txt", "r") as f:
        lines = f.read().split("\n")
        f.close()
        text = ""
        i = 0
        for line in lines:
            if i > 0:
                text += line + ", "
                i += 1
            else: text += line
            i += 1
        return text