#PROBLEM 2
items = ("aparna", False,40032118,1.34555)
print(items)

#PROBLEM 9

t = 2, 4, 5, 'siva', 2, 3, 4, 'siva', 4
print(t)
c1 = t.count(4)
c2 = t.count('siva')
print(c1)
print(c2)

#PROBLEM 12

REM=('2','44','CHARU','1.345','TRUE')
L=list(REM)
L.remove('1.345')
print(L)

#PROBLEM 28

test_data = ('234', '33', '45', '56', '700')
print("Original tuple is : " , str(test_data))
test_data = tuple(map(int, test_data))
print("Modified tuple is : " ,str(test_data))

#PROBLEM 24

num_list = [10,11,3,2,9,(1,2,3),44]
count = 0
for i in num_list:
    if type(i) is tuple:
        break
    count = count + 1
print(count)

