
def add(x, y):
    return x + y

# res = add(43, 76)

a = add

res = a(10, 30)

print(f"res :{res}")

print("-" * 60)

b = lambda i, j: i + j

res = b(49, 33)

print(f"res :{res}")

print("map".center(60, "-"))

l1 = list(range(1, 11))
print(f"l1 :{l1}")

sqaures = list(map(lambda x: x ** 2, l1))

print(f"squares :{sqaures}")
print("-" * 60)

sentence = 'the quick brown fox jumps over the lazy dog'
print(f"sentence  :{sentence}")

words = list(map(lambda x: x, sentence.split()))
print(f"words :{words}")

words = list(map(lambda x: len(x), sentence.split()))
print(f"words :{words}")

print("filter".center(60, "-"))
l1 = list(range(1, 31))
print(f"l1 :{l1}")

print("-" * 60)
res = list(filter(lambda x : x % 3 == 0, l1))
print(f"res :{res}")

print("-" * 60)
sentence = 'the quick brown fox jumps over the lazy dog'
print(f"sentence  :{sentence}")

words = list(filter(lambda x: x != 'the', sentence.split()))
print(f"words :{words}")

print("-" * 60)
words = list(filter(lambda x: len(x) == 3, sentence.split()))
print(f"words :{words}")

print("reduce".center(60, "-"))
from functools import reduce
# it reduces the list into a single value

l1 = [10, 4, 7, 1, 9, 3, 5, 2, 6, 8]
print(f"l1 :{l1}")

res = reduce(lambda x, y: x if x > y else y, l1)
print(f"res :{res}")

print("-" * 60)

res = reduce(lambda x, y: x + y, l1)
print(f"res :{res}")
