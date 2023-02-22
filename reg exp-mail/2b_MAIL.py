





#2B-EMAIL
import re
ltts_mail= r'\b[A-Za-z0-9._%+-]+@ltts.com|@LTTS.com'
employee_mail=input('Enter user email ID : ')
if re.search(ltts_mail,employee_mail) :
    print('YES IT IS LTTS MAIL')
else :
    print('NO IT IS NOT LTTS MAIL')
