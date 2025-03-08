
def fun(x, y):
    print(f"x inside fun before :{x}")
    print(f"y inside fun before:{y}")
    x += 10
    y -= 5
    print("-" * 60)
    print(f"x inside fun after:{x}")
    print(f"y inside fun after:{y}")

i = 50
j = 30

print(f"i, j before calling fun :i = {i} and j = {j}")
print("-" * 60)

fun(i, j)

print("-" * 60)
print(f"i, j after calling fun :i = {i} and j = {j}")
