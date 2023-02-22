#problem 1

class Book:
    def __init__(self,Bookname,Author,TOC,ISBM,Publisher,Price,Edition):
        self.Bookname=Bookname
        self.Author=Author
        self.TOC=TOC
        self.ISBM=ISBM
        self.Publisher=Publisher
        self.Price=Price
        self.Edition=Edition

B1=Book("Country of Eternity","Ken Follett",4556,698160576,"Penguin",480,"Unabridged")
print(B1.Bookname)
print(B1.Author)
print(B1.TOC)
print(B1.ISBM)
print(B1.Publisher)
print(B1.Price)
print(B1.Edition)

B2=Book("My Experiments with Silence","Samir Soni",194,9780698160576,"Bellantine",789,"Abridged")
print(B2.Bookname)
print(B2.Author)
print(B2.TOC)
print(B2.ISBM)
print(B2.Publisher)
print(B2.Price)
print(B2.Edition)

B3=Book("Modi @20: Dreams Meeting Delivery","VP Venkaiah Naidu",689,97805678239,"Bellantine",500,"Abridged")
print(B3.Bookname)
print(B3.Author)
print(B3.TOC)
print(B3.ISBM)
print(B3.Publisher)
print(B3.Price)
print(B3.Edition)

B4=Book("The Terrible, Horrible, Very Bad Good New","Meghna Pant",340,6578930123,"Penguin",890,"Unbridged")
print(B4.Bookname)
print(B4.Author)
print(B4.TOC)
print(B4.ISBM)
print(B4.Publisher)
print(B4.Price)
print(B4.Edition)

B5=Book("The 7 Sins of Being a Mother","Tahira Kashyap Khurrana",458,9767832239,"Bellantine",567,"Abridged")
print(B5.Bookname)
print(B5.Author)
print(B5.TOC)
print(B5.ISBM)
print(B5.Publisher)
print(B5.Price)
print(B5.Edition)

#2A PHASE 1

def monkey_trouble(a_smile, b_smile):
    if a_smile == 1 and b_smile == 1:
        return True
    if a_smile == 0 and b_smile == 0:
        return True
    else:
        return False
try:
    a_smile = int(input("monkey1:"))
    if a_smile > 1 or a_smile < 0:
        raise ValueError("enter 1 or 0")
    b_smile = int(input("monkey2:"))
    if b_smile > 1 or b_smile < 0:
        raise ValueError("pease enter 0 or 1")
    else:
        monkey_trouble(a_smile, b_smile)
        print(monkey_trouble(a_smile, b_smile))
except ValueError:
    print("enter 0 or 1")

#2B PHASE 2

def string_bits(s):
    result = ""
    for i in range(0, len(s), 2):
        result = result + s[i]
    print(result)
try:
    s = str(input("enter the word "))
    if (len(s) == 1):
        raise ValueError("enter valid input")
    else:
        string_bits(s)
except ValueError:
    print("enter valid input")

#2C PHASE 3

def common_end(a, b):
    l1=[]
    l2=[]
    l1=[int(item) for item in input("enter the number").split()]
    l2=[int(item) for item in input("enter the number").split()]
    a=print(l1)
    b=print(l2)
    if(a[-1]==b[-1])or(a[0]==b[0]):
        print("TRUE")
    else:
        print("FALSE")
try:
    a=int(input("enter the number"))
    if a=='':
        raise ValueError("please enter something")
    b=int(input("enter the number"))
    if b==[]:
        raise ValueError("enter something")
    else:
        common_end(a,b)
except ValueError:
    print("enter something")

# PROBLEM 3

class Date(object):
    def get_date(self):
        return "2023-01-11"
class Time(Date):
    def get_time(self):
        return "14:00:00"
d1 = Date()
print(d1.get_date())
print("------")
d2 = Time()
print(d2.get_time())
print(d2.get_date())

