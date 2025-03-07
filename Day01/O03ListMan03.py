
l1 = [1, 2, 3, 4, 5]
print(f"l1 before :{l1}")

# copy the list l1 to l2
l2 = l1      # shallow copy - copy the data with their address

print(f"l2 before :{l2}")

l2.extend([6, 7, 8, 9, 10])
print(f"l2 after :{l2}")
print(f"l1 after :{l1}")

print("-" * 60)
print("-" * 60)

l3 = [6, 7, 8, 9, 10]
print(f"l3 before :{l3}")

# copy the list l3 to l4
l4 = l3.copy()          # deep copy -only the values are getting copied

print(f"l4 before :{l4}")

l4.append(11)
l4.append(12)
l4.append(13)
l4.append(14)
print(f"l4 afer :{l4}")

print("=" * 60)
print("=" * 60)

l5 = [1, 4, 6, [1, 2, 3, 4, 5], 8, 10]
print(f"l5 before :{l5}")

# copy the list l5 to
#
l6 = l5.copy()

l5[3].append(6)
l5[3].append(7)

print(f"l6 after :{l6}")
print(f"l5 after :{l5}")

print("=" * 60)
print("=" * 60)

l7 = [5, 10, 15, 20, [10, 20, 30, 40], 25]
print(f"l7 before :{l7}")

# copy the elements of l7 to l8}
from copy import deepcopy

l8 = deepcopy(l7)

print(f"l8 before :{l8}")

l8[4].extend([50, 60, 70])
print(f"l8 after :{l8}")
print(f"l7 after :{l7}")