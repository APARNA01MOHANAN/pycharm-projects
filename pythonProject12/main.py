#sets

#PROBLEM 5

your_set = set([22, 'siva', 2, 3.33, 4, 'true'])
print("Original set elements:")
print(your_set)
print("\nafter removing from the set:")
your_set.discard('siva')
print(your_set)
print("\nafter removing from the set :")
your_set.discard(4)
print(your_set)

#PROBLEM 9

s1 = set([8, 7, 6, 3, 4, 5])
s2 = set([9, 5, 1, 7, 8, 0])
print("\nREAL SET:")
print(s1)
print(s2)
r1 = s1.symmetric_difference(s2)
print("\nSymmetric difference of s1 - s2:")
print(r1)
r2 = s2.symmetric_difference(s1)
print("\nSymmetric difference of s2 - s1:")
print(r2)

#PROBLEM 10

A = {'SIVA', 'RAJESH', 'BANU'}
B = {'BANU', 'SIVA', 'RAJESH', 'DEENA', 'ANJAI'}

print('A is subset of B:', A.issubset(B))
print('B is subset of A:', B.issubset(A))

#PROBLEM 20

set1 = {'RAHI',2,3,'JOHN',5}
set2 = {'JOHN',5,6,3,8}
print("\nRemove the intersection of a 2nd set from the 1st set :")
set1-=set2
print("set1: ",set1)
print("set2: ",set2)

#PROBLEM 17

x = {1,2,3,4}
y = {4,5,6,7}
print(x)
print(y)
print("\nWHEATHER TWO SETS HAVE COMMON ELEMENTS")
print(x.isdisjoint(y))




