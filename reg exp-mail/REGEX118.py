#1-VALID DATE
import re
def is_valid_date():
    date = "^[0-9]{4}\\-[0-1][0-9]{1,2}\\-[0-3][0-9]{1,2}$"
    in_date=input()
    if re.search(date, in_date) :
        print("TRUE")
    else:
        print("FALSE")

is_valid_date()


#2B-EMAIL 
import re
ltts_mail= r'\b[A-Za-z0-9._%+-]+@ltts.com|@LTTS.com'
employee_mail=input('Enter user email ID : ')
if re.search(ltts_mail,employee_mail) :
    print('YES IT IS LTTS MAIL')
else :
    print('NO IT IS NOT LTTS MAIL')



