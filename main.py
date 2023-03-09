mainloop = True
while mainloop:
    print ("-"*64)
    print ("Welcome to the Test Management System")
    print ("-"*64)
    print ("Please pick an option: ")
    print ("[1] Setup")
    print ("[2] Generate Test Paper")
    print ("[3] Help")
    print ("\n[E] Exit")

    def setupmenu():
        print ("todo")

    def testpaper():
        print ("todo")

    def helpmenu():
        print ("todo")

    select = input()

    if select == "1":
        setupmenu()

    elif select == "2":
        testpaper()

    elif select == "3":
        helpmenu()

    elif select == "E":
        print ("Goodbye")
        mainloop = False

    else:
        print ("Error: Invalid Input\nPlease Try Again.")
