import re
loc_temp='''Baroda is 22,Bengaluru is 9,Chennai is 30,Hyderabad is 32,Pune is 35,Mysuru is 20'''
print(loc_temp)
print("the cities are : ")
x = re.findall("[A-Z][a-z]*", loc_temp)
z = re.findall("[0-9][0-9]*", loc_temp)
u = re.sub("is",'was', loc_temp)
print(x)
print("the temperatures are :")
print(z)
print(u)
p = re.findall(r"is\b", loc_temp)
q=len(p)
print(q)
r = re.sub("is",'', loc_temp)

