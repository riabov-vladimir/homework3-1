boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

comparison = zip(sorted(boys), sorted(girls))

if len(boys) == len(girls):
  for a, b in comparison:
    print(a, b, sep=' и ')
else:
  print('Пара найдется или всем или никому!')

