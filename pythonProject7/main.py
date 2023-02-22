#problem 3 monkey_trouble
try:
    def trouble (smile_a,smile_b):
        if smile_a and smile_b:
            print("True")
        elif not smile_a and not smile_b:
            print("True")
        else:
            print("False")
except NameError:
    print("invalid entry")
trouble(True,True)
trouble(False,False)
trouble(True,False)
trouble(False,True)
trouble(21,23)