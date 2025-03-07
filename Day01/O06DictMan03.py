
print("fromkeys".center(60, "-"))
# used to convert a list into a dictionary - list elements will become keys in the dictionary

cities = ['blr', 'che', 'mum', 'del', 'hyd', 'kol']
print(f"cities :{cities}")

print("-" * 60)
res1 = dict.fromkeys(cities)
print(f"res1 :{res1}")

print("-" * 60)
res2 = dict.fromkeys(cities, 23)
print(f"res2 :{res2}")

print("setdefault".center(60, "-"))
# can add new key and value but cannot modify the existing

emp1 =  {'empid': 'EMP121', 'empname': 'Peter', 'age': 28, 'desig': 'BDE'}
print(f"emp1 :{emp1}")

# modify
emp1.setdefault('empname', 'John')
emp1.setdefault('age', 75)

# add
emp1.setdefault('dept', "MKT")
emp1.setdefault('salary', 120000)

print("-" * 60)
print(f"emp1 :{emp1}")

print("pop".center(60, "-"))

emp1 = {'empid': 'EMP121', 'empname': 'Peter', 'age': 28, 'desig': 'BDE', 'dept': 'MKT', 'salary': 65000}
print(f"emp1 :{emp1}")

res = emp1.pop('dept')
print(f"res :{res}")

res = emp1.pop('age')
print(f"res :{res}")

# res = emp1.pop()
# print(f"res :{res}")

print(f"emp1 :{emp1}")

print("popitem".center(60, "-"))

emp1 = {'empid': 'EMP121', 'empname': 'Peter', 'age': 28, 'desig': 'BDE', 'dept': 'MKT', 'salary': 65000}


print(f"emp1 :{emp1}")

print("-" * 60)
res = emp1.popitem()
print(f"res :{res}")

print("-" * 60)
res = emp1.popitem()
print(f"res :{res}")

print("-" * 60)
print(f"emp1 :{emp1}")

print("clear".center(60, "-"))

emp1 = {'empid': 'EMP121', 'empname': 'Peter', 'age': 28, 'desig': 'BDE', 'dept': 'MKT', 'salary': 65000}
print(f"emp1 :{emp1}")

print('-' * 60)
emp1.clear()
print(f"emp1 :{emp1}")

