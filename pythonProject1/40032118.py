#problem 1

def cubes(n):
    sum = 0
    while n > 0:
        sum =sum +(n * n * n)
        n=n-1
    return sum
n=int(input("enter the number  ="))
print("Sum of cubes of given range of numbers",cubes(n))

#problem 2
def operations(s):
    lis=[]
    l=lis.append(s)
    sum=0
    for i in range(0,len(l)):
        if (l[i]%3==0 or l[i]%5==0):
            sum=sum+l[i]
            print(l[i])
        else:
            l.remove(l[i])
s=int(input())
if(s<=0):
    print("enter a positive number and not equal to zero")
else:
    print("the sum of the list",operations(s))

#problem 3
def sumofdigits(s):
    add=0
    if s>=0:
        for i in range(0,6):
            rem=s%10
            add=add+rem
            s=s/10
    return add+sumofdigits(s)

s=int(input())
res=sumofdigits(s)
print(res)

#problem 4
def common():

    s=list(a)
    u=list(b)
    count=0
    for i in range(a,b):
        if(a[i]==b[i]):
            count=count+1
            print("there are ",count,"elements common")
        else:
            print("no common element")
a=str(input())
b=str(input())
res=common()
print(res)










