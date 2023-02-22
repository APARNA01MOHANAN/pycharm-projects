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
print(r)
location="[A-Z][a-z]*"

print(len(re.findall('a',location)))
for cnt in location:
    temp=re.findall('a',cnt)
    print(temp)
    print(len(temp))
    result=len(temp)
    if result>1:
        print(cnt)

#Display cities with temperature between 20-30


print("ppppp")
location=re.findall("[A-Z][a-z]*",loc_temp)
for cnt in location:
    temp=re.findall('a',cnt)
    l=(len(temp))
    if l>1:
        print(cnt)
import re

location_temp = '''Baroda is 22, Bengaluru is 20, Chennai is 30, Hyderabad is 32, Pune is 35, Mysuru is 20'''
cityname = re.findall("[A-Z]\w*", location_temp)

temp = re.findall("\d+", location_temp)

dict1 = {}
x = 0
for name in cityname:
    dict1[name] = temp[x]
    x += 1

for i in dict1:
    if dict1[i] == "35":
        print(i)
#8.Display cities with temperature between 20-30
import re
location_temp="Baroda is 22, Bengaluru is 20, Chennai is 30, Hyderabad is 32, Pune is 35, Mysuru is 20"
cityname=re.findall("[A-Z]\w*",location_temp)
print(cityname)
temp=re.findall("\d+",location_temp)
print(temp)

dict1={}
x=0
for name in cityname:
    dict1[name]=temp[x]
    x+=1
print(dict1)

for i in dict1:
    if dict1[i]>="20" and dict1[i]<="30":
        print(i)