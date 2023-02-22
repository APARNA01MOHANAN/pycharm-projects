#PROBLEM 5

def inter(x,y):
  a = y[:2] + x[2:]
  b = x[:2] + y[2:]

  return a + ' ' + b
print(inter('ter', 'sem'))

#PROBLEM 20

def rev(string):
    if len(string) % 4 == 0:
       return ''.join(reversed(string))
    return string
print(rev('1234'))
print(rev('call me aparna'))

#PROBLEM 35

a = 78965
b = 8906543
print("enter a number: ", a)
print("the number is formated with comma seperator as: "+"{:,}".format(a));
print("Original Number: ", b)
print("the number is formated with comma seperator as: "+"{:,}".format(b));


#PROBLEM 49

def vow(sen):
    x = "aeiuoAEIOU"
    print(len([text for text in sen if text in x]))
    print([text for text in sen if text in x])
vow('aparna is a girl')

#PROBLEM 23
input='call her\n'
print(input)
print(input.rstrip())