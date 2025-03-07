
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

print(f"emp :{emp}")

print("-" * 60)
print(f"emp1 :{emp['emp1']}")

print("-" * 60)
print(f"emp2 :{emp['emp2']}")

print("-" * 60)
print(f"emp2 :{emp['emp3']}")

print("-" * 60)
for ky, info in emp.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k + " => " + str(v))
    print("-" * 60)

print("get".center(60, "-"))

emp1 = {'empid': 'EMP121', 'empname': 'Peter', 'age': 28, 'desig': 'BDE', 'dept': 'MKT', 'salary': 65000}

print(f"emp1 :{emp1}")
print(type(emp1))

print("-" * 60)
print(f"empname :{emp1.get('empnme', "Invalid Key, Please enter a valid key....")}")
print(f"Runs    :{emp1.get('dept', "Invalid Key, Please enter a valid key....")}")

print("update".center(60, "-"))

emp1 =  {'empid': 'EMP121', 'empname': 'Peter', 'age': 28, 'desig': 'BDE', 'dept': 'MKT'}

emp2 = {'empid': 'EMP223', 'empname': 'Tina', 'age': 34, 'desig': 'TL', 'salary': 115000}

print(f"emp1 :{emp1}")

print("-" * 60)

print(f"emp2 :{emp2}")

print("-" * 60)
# update emp1 with emp2's values

emp1.update(emp2)

print(f"emp1 :{emp1}")