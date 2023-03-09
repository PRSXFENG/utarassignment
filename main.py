run = True
def mainloop():
    print ("-"*64)
    print ("Welcome to the Test Management System")
    print ("-"*64)
    print ("Please pick an option: ")
    print ("[1] Setup")
    print ("[2] Generate Test Paper")
    print ("[3] Help")
    print ("\n[E] Exit")
    select = input()

    if select == "1":
        setupmenu()

    elif select == "2":
        testpaper()

    elif select == "3":
        helpmenu()

    elif select == "E" or select == "e":
        print ("Goodbye")
        exit()

    else:
        print ("Error: Invalid Input\nPlease Try Again.")

def setupmenu():
    print ("-"*64)
    print ("Setup Menu")
    print ("-"*64)
    print ("Please pick an option: ")
    print ("[1] Student Menu")
    print ("[2] Courses Menu")
    print ("[3] Question Banks")
    print ("[4] Test Dates")
    print ("\n[E] Exit")
    select2 = input()

    if select2 == "1":
        studentmenu()

    elif select2 == "2":
        coursemenu()

    elif select2 == "3":
        questionbank()

    elif select2 == "4":
        testdate()

    elif select2 == "E" or select2 == "e":
        mainloop()
    
    else:
        print ("Error: Invalid Input\nPlease Try Again.")

def testpaper():
    print ("-"*64)
    print ("Generate Student Test Paper")
    print ("there is supposed to be a list of courses here from another menu but for now it will just be this line of text")
    courseid = input("Enter Course ID or E to Exit: ")

    if courseid == "E" or "e":
        mainloop()

    else:
        print ("itll do something")

def helpmenu():
    print ("todo")

def studentmenu():
    print ("todo")

def coursemenu():
    print ("todo")

def questionbank():
    print ("todo")

def testdate():
    print ("todo")

while run:
    mainloop()