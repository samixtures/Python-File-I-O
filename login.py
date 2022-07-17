def readInput(inpU, inpP, correctU, correctP):
    inpU = ""
    inpP =""
    print("What is the username: ")
    inpU += input()
    print("What is the password: ")
    inpP += input()
    print(inpU, inpP, correctU, correctP)
    if inpU == correctU and inpP == correctP:
        print("Successful log in")
    else:
        print("Incorret credentials, please try again")
        readInput(inpU, inpP, correctU, correctP)


fileR = open("file.txt", "r")
usern = ""
passw = ""
fileList = fileR.readlines()
fileR.close()
if fileList:
    if fileList[0] and fileList[1]:
        readInput(usern, passw, fileList[0].strip(), fileList[1].strip())
else:
    fileW = open("file.txt", "w")
    print("Time to register!")
    print("Type in a username")
    newUsern = input()
    print("Type in a password")
    newPassw = input()
    writer = fileW.write(newUsern)
    writer = fileW.write("\n")
    writer = fileW.write(newPassw)
    fileW.close()

# file = open("file.txt", "w")
# f = file.write("Python")