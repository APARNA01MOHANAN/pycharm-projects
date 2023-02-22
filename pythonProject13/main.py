#problem 1

lis = []
for i in range(0, 5):
    x = int(input())
    lis.append(x)

#problem 2

NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

print("The Smallest Element in this List is : ", min(NumList))
print("The Largest Element in this List is : ", max(NumList))

#problem 3

list1=[14,25,46,87,98,62,23]
list2=[45,85,9,4,5,6,98]
for x in list1:
    if x in list2:
        print("yes")

#problem 4


list1[14,25,46,87,98,62,23]
list2=[]
temp=[]
for x in list1:
    if x%2==0:
        list2.append(x)
    else:
        temp.append(x)
print(list2)
print


Employee={
    "name": "drishti",
    "psno": "40032485",
    "dob": "28121998",
}
print(Employee.get["name"])
print(Employee.get["psno"])
print(Employee.get["dob"])
print(Employee.items())
print(Employee.keys())
if "dob" in Employee:
    print("it does exist")
    print("it does not exist")