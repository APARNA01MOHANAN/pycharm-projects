#PROBLEM 1

def L_sum(List):
    if len(List) == 1:
        return List[0]
    else:
        return List[0] + L_sum(List[1:])

print(L_sum([9,11,44,33]))

# PROBLEM 6

def sumofdig(a):
  if a == 0:
    return 0
  else:
    return a % 10 + sumofdig(int(a / 10))

print(sumofdig(789))
print(sumofdig(5746))
# PROBLEM 8

def h_sum(x):
  if x < 2:
    return 1
  else:
    return 1 / x + (h_sum(x - 1))

print(h_sum(44))
print(h_sum(3))

# PROBLEM 11

def GCD(a, b):
	L = min(a, b)
	H = max(a, b)

	if L == 0:
		return H
	elif L == 1:
		return 1
	else:
		return GCD(L, H%L)
print(GCD(33,11))


# PROBLEM 3

def l_sum(num):
    Res = 0
    for i in num:
        if type(i) == type([]):
            Res = Res + l_sum(i)
        else:
            Res = Res + i

    return Res


print(l_sum([5, 23, [9, 0], [8, 3]]))
