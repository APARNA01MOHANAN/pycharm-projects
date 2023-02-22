#problem 1

total = 0

list1 = [5, 17, 18, 23]

for ele in range(0, len(list1)):
    total = total + list1[ele]

print("Sum of all elements in a given list: ", total)


#problem 2

l = []
x = int(input('How many numbers: '))
for i in range(x):
    num = int(input('input: '))
    l.append(num)
print("Maximum element in the list is :", max(l))
print("Minimum element in the list is :", min(l))

#problem 3

l1=['app',45,88,0,98,9]
l2=[5,15,8,74,'app',11]
for i in l1:
    if i in l2:
        print("yes,there is a common value")

#problem 4


list1=[14,25,46,87,98,62,23]
list2=[]
temp=[]
for x in list1:
    if x%2==0:
        list2.append(x)
    else:
        temp.append(x)
print(list2)
print(temp)

#PROBLEM 5

INPUT = [9, 2, 0, 8, 4, 2, 5]
print("THE INPUT IS : " + str(INPUT))
X = 9
OUTPUT = len(INPUT) - INPUT.index(X)
print("THE OUTPUT IS : -" + str(OUTPUT))
