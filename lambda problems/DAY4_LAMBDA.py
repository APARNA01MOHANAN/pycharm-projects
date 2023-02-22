#PROBLEM 8

lst = ["APARNA", '33', "AMMA", '4.44', '000']
print(lst)
output = list(filter(lambda x: (x == "".join(reversed(x))), lst))
print("\nList of palindromes:")
print(output)

#PROBLEM 12

number = [4, -9, 89, -5, 45, 12, -33]
print(number)
output = sorted(number, key = lambda x: 0 if x == 0 else -1 / x)
print("Rearrange positive and negative numbers of the list:")
print(output)

#PROBLEM 21

a = [33, 1, 7, 90, 56]
b = 5
print("enter list: ", a)
print("to multiply with: ", b)
mul=list(map(lambda num:num*b,a))
print("OUTPUT:")
print(' '.join(map(str,mul)))
#PROBLEM 38

def i_list(A, B):
    output = list(filter(lambda a: a not in B, A))
    return output
A = [3,6,4,1,6,7,8,9,10]
B = [2,7,8,4]
print("AFTER REMOVING THE COMMON ELEMENTS FROM LIST 2 THAT ARE IN LIST 1")
print(i_list(A, B))

#PROBLEM 3

lst= [('aparna', 67), ('Siva', 59), ('loosi', 88), ('preethi', 90)]
print(lst)
lst.sort(key = lambda a: a[1])
print("\nSorting the List of Tuples:")
print(lst)
