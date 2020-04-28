boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

comparison = zip(sorted(boys), sorted(girls))

if len(boys) == len(girls):
  print(list(comparison))
else:
  print('Пара найдется или всем или никому!')

