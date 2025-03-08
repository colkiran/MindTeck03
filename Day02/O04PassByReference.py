
def fun(names):
    print(f"inside fun before :{names}")
    print("-" * 60)
    names.extend(['kennedy', 'ruben', 'louis'])

    print(f"inside fun after :{names}")

emp = ['Jack', 'Mary', 'Grace', 'Peter', 'Steve', 'Kevin']

print(f"emp before the function call :{emp}")

print("-" * 60)
fun(emp)

print("-" * 60)
print(f"emp after the function call :{emp}")