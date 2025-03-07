
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 60)

d2 = {'name': 'Sachin', 'age': 36, 'runs': 126, 'oppnt': 'Aus'}
print(f"d2 :{d2}")
print(type(d2))

print("-" * 60)

d3 = dict([('name', 'rahul'), ('age', 34), ('runs', 85), ('oppnt', 'SA')])
print(f"d3 :{d3}")
print(type(d3))

print("-" * 60)
d4 = dict(name='Kevin', age=32, desig='TL', dept='MKT')
print(f"d4 :{d4}")
print(type(d4))

print("-" * 60)
# CRUD

# create
player = {'name': 'Virat', 'age': 36 ,'runs': 55, 'oppnt': 'WI'}
print(f"player :{player}")

print("-" * 60)
# read
print(f"Name :{player['name']}")
print(f"Runs :{player['runs']}")

print("-" * 60)
for i in player:
    print(i, "=>", player[i])

print("-" * 60)
# update - modify, add new key and value
# modify

player['name'] = 'Virat Kholi'
player['runs'] = 160

# addition
player['year'] = 2013
player['venue'] = 'Sabina Park'

print(f'player :{player}')

print("-" * 60)
print(dir(player))
