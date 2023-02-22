'''dict = {
    "Name": "APARNA",
    "PS NO": "40032118",
    "BU": "EMB",
    "DOB": "16-03-2001"
}
if "loc" in dict:
    print("It does exist")
print("no")
print(dict["Name"])
print(dict.get("Name"))
print(dict.keys())
print(dict.values())
print(dict.items())
dict["BU"]="MES"
print(dict["BU"])
for x in dict:
    print(x)
    print(dict[x])
for x in dict.values():
    print(x)
for x,y in dict.items():
    print(x,y)'''
#nested
employeeinfo={
    "emp1":{
        "name":"aparna",
        "dob":"16-03-2001",
        "ps no":"40032118"
    },
    "emp2":{
        "name":"surya",
        "dob":"20-01-2001",
        "ps no":"40032116"
    }
}