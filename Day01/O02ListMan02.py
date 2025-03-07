l1 = list(range(1, 5))
print(f"l1 :{l1}")

print("append".center(60, "-"))
print(f"l1 :{l1}")
l1.append(5)
l1.append(6)
l1.append(7)
print(f"l1 :{l1}")

l1.append([8, 9, 10, 11, 12])
print(f"l1 :{l1}")

print("pop".center(60, "-"))
l1 = list(range(10, 101, 10))
print(f"l1: {l1}")

res = l1.pop(4)
print(f"res :{res}")

res = l1.pop(1)
print(f"res :{res}")

res = l1.pop()
print(f"res :{res}")

print(f"l1: {l1}")

print("sort".center(60, "-"))
l1 = [8, 5, 9, 6, 10, 2, 4, 1, 3, 7]
print(f"l1 :{l1}")

res_asc = sorted(l1)
res_desc = sorted(l1, reverse=True)

print(f"Ascending order  :{res_asc}")
print(f"Descending order :{res_desc}")
print("-" * 60)
l1 = [8, 'zebra',  5, 'apple', 9, 'x ray', 6, 'blue', 10, 'yellow', 2, 'green', 4, 'white', 1, 'orange', 3, 'violet', 7, 'pink', 'maroon', 'cat', 'dog', 'egg', 185, 1234, 29, 270, 2235]

print(f"l1 :{l1}")

print("-" * 60)
res = sorted(l1, key=ascii)
print(f"Ascending order :{res}")

print("-" * 60)
for i in range(0, len(res)):
    if type(res[i]) == int:
        # print(i)
        break

print(res[:i] + sorted(res[i:]))

print("-" * 60)
cities = ['thiruvananthapuram', 'delhi', 'bangalore', 'chennai', 'ooty', 'mumbai', 'hyderabad', 'pune', 'vishakapatnam', 'kolkata']

print(f"cities :{cities}")

print("-" * 60)
# sort it in ascending order
res_asc = sorted(cities, key=len)
print(f"Ascending order  :{res_asc}")

