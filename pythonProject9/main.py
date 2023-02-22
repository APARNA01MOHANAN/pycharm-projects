#problem 4
'''dict_content = {"siva": 10, "rama": 20, "bargav": 30}
def k_present(x):
  if x in dict_content:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
k_present("siva")
k_present("aparna")'''

#problem 8
'''a= { "x":"siva","y":"aparna"}
b={"p":300,"q":200}
c=a.copy()
c.update(b)
print(c)'''

#problem 19
'''d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'd': 200, 'e':400}
d3= {}
d3.update(d1)
d3.update(d2)
for i,j in d1.items():
    for x,y in d2.items():
        if i ==x:
            d3[i] = j+y
print(d3)'''

#problem 56

'''original_1 = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
original_2={'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
result_1 = list(map(list, original_1.items()))
result_2 = list(map(list, original_2.items()))
print(result_1,result_2)'''

#problem 72

