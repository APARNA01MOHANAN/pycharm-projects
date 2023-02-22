def monkey_trouble(a_smile,b_smile):
    if a_smile and b_smile:
        return True
    elif not a_smile and not b_smile:
        return True
    else:
        return False
#monkey_trouble(True,True)
#monkey_trouble(False,False)
#monkey_trouble(False,True)
#monkey_trouble(True,False)