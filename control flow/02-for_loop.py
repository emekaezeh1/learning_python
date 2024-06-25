point = (2.1, 3.2, 7.5)
for value in point:
    print(value)


ages = {'kevin': 59, 'bob': 40, 'kayla': 21} 
for key in ages:
    print(key)

for letter in "my_string":
    print(letter)


x,y = (1, 2)
list_of_points = (1, 2), (2, 3), (4, 3)
for x, y in list_of_points:
    print(f"x: {x}, y:{y}")

for name, age in ages.items():
    print(f"Peron named: {name}")
    print(f'Age of:{age}')
 