l1 = list()
# format string or f string - used for interpolation
print(f"l1 :{l1}")
print(type(l1))

print("-" * 60)
l2 = [1, 2, 3, 4, 5.1, 6.0, 7.6, 8.2, 'nine', 'ten', 'eleven', 'twelve', 13+2j, 14-4j, True, False]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 60)
l3 = list(range(1, 10))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 60)
l1 = list(range(1,11))
print(f"l1 :{l1}")
print(f"l1[0] :{l1[0]}")
print(f"l1[6] :{l1[6]}")

# slicing
print(f"l1[0:5] :{l1[0:5]}")
print(f"l1[0:]  :{l1[0:]}")
print(f"l1[:10]  :{l1[:10]}")
print(f"l1[:]    :{l1[:]}")

print("-" * 60)
# reverse indexing
print(f"l1 :{l1}")
print(f"l1[-1] :{l1[-1]}")
print(f"l1[-7] :{l1[-7]}")
print(f"l1[-10] :{l1[-10]}")

print("-" * 60)
# slicing
print(f"l1[-1:-6:-1] :{l1[-1:-6:-1]}")
print(f"l1[-7:-11:-1] :{l1[-7:-11:-1]}")
print(f"l1[-1::-1]    :{l1[-1::-1]}")
print(f"l1[:-11:-1]    :{l1[:-11:-1]}")

# Write a code to find if a string is a palindrome
#CRUD
print("-" * 60)
# create
l1 = [1, 2, 3,4, 5]
print(f"l1 :{l1}")

print("-" * 60)
# read
print(f"l1[0] :{l1[0]}")
print(f"l1[2] :{l1[2]}")
print(f"l1[-1] :{l1[-1]}")

for i in l1:
    print(i, end=" ")
print()         # print a new line

print("-" * 60)
for i in range(0, len(l1)):
    print(f"l1[i] :{l1[i]}")
print("-" * 60)

#update - modify, add new value
print(f"l1 :{l1}")
#modify
l1[2] = 300
l1[4] = 555
print(f"l1 :{l1}")

# insert a new value
l1[1] = 250
print(f"l1 :{l1}")

# delete
print(f"l1 :{l1}")
del l1[2]
del l1[-1]

print(f"l1 :{l1}")
print("-" * 60)
print(dir(l1))
