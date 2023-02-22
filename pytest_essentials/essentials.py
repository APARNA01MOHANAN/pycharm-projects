
#source file
#phase 1

def monkey_trouble(a_smile,b_smile):
    if a_smile and b_smile:
        return True
    elif not a_smile and not b_smile:
        return True
    else:
        return False
monkey_trouble(True,True)
monkey_trouble(False,False)
monkey_trouble(False,True)
monkey_trouble(True,False)

#phase 2

def string_bits(str):
    result=""
    for i in range(0,len(str),2):
        result=result+str[i]
    return result
string_bits("hello")
string_bits("hi")
string_bits("heeololeo")

#phase 3

def common_end(a,b):
    if(a[-1]==b[-1])or(a[0]==b[0]):
        return ("True")
    else:
        return ("False")
common_end(a=[1,2,3],b=[3,4,5])
common_end(a=[1,2,3],b=[4,2,3])
common_end(a=[5,6,7],b=[9,8,7])

