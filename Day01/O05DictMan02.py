
print("keys".center(60, "-"))
player = {'name': 'Sachin', 'age': 36, 'runs': 89, 'oppn': 'Eng'}
print(f"player :{player}")

print("-" * 60)
k = player.keys()
print(f"k :{k}")

print("-" * 60)
for k in player.keys():
    print(k, "=>", player[k])

print("values".center(60, "-"))

player = {'name': 'Sachin', 'age': 36, 'runs': 89, 'oppn': 'Eng'}
print(f"player :{player}")

v = player.values()
print(f"v :{v}")

print("items".center(60, "-"))
# items is a combination of keys and values

emp = {
    'emp1': {'empid': 'EMP121', 'empname': 'Peter', 'age': 28, 'desig': 'BDE', 'dept': 'MKT', 'salary': 65000},
    'emp2': {'empid': 'EMP223', 'empname': 'Tina', 'age': 34, 'desig': 'TL', 'dept': 'Finance', 'salary': 115000},
    'emp3': {'empid': 'EMP303', 'empname': 'Richard', 'age': 42, 'desig': 'MGR', 'dept': 'HR', 'salary': 145000}
}