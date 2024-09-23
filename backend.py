def backClick(text):
    with open("info.txt", "a") as f:
        f.write("\n" + text + " ")
        f.close()