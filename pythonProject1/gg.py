def sumofdigits(s):
    add = 0
    if s >= 0:
        for i in range(0, 6):
            rem = s % 10
            add = add + rem
            s = s / 10
    return add + sumofdigits(s)


s = int(input())
res = sumofdigits(s)
print(res)