register_value = [i for i in range(10)]
register_multi = [10**i for i in range(10)]
register = {
  'black':0, 'brown':1, 'red':2, 'orange':3, 'yellow':4, 'green':5, 'blue':6,'violet':7,'grey':8,'white':9}

result = ''
for i in range(3):
  if i <=1:
    result += str(register_value[register[input()]])
  else:
    result = int(result) * register_multi[register[input()]]
print(result)