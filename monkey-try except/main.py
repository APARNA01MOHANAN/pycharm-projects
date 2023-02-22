try:

    a_smile=bool(input("is monkey a smiling? "))
    b_smile=bool(input("is monkey b smiling? "))
    if (a_smile==True and b_smile==True):
        print(True,"we are in trouble")
    if (a_smile==True and b_smile==False):
        print(False,"we are not in trouble")
    if (a_smile==False and b_smile==False):
        print(True,"we are in trouble")
    if (a_smile==False and b_smile==True):
        print(False, "we are not in trouble")
except :
    print("wrong input")

