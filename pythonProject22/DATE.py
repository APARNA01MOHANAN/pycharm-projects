import re
def is_valid_date():
    date = "^[0-9]{4}\\-[0-1][0-9]{1,2}\\-[0-3][0-9]{1,2}$"
    in_date=input()
    if re.search(date, in_date) :
        print("TRUE")
    else:
        print("FALSE")

is_valid_date()