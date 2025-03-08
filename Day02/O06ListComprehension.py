
squares = [x ** 2 for x in range(1, 11)]
print(f"squares :{squares}")

print("-" * 60)
sentence = "the quick brown fox jumps over the lazy dog"
print(f"sentence :{sentence}")

words = [(word, len(word)) for word in sentence.split()]
print(f"words :{words}")

print("-" * 60)
word = [(word, len(word)) for word in sentence.split() if len(word) > 3]
print(f"word :{word}")

fruits = [
    ('apple', 285),
    ('orange', 85),
    ('grapes', 145),
    ('pineapple',70 ),
    ('banana', 69),
    ('gauva', 110),
    ('Mango', 235),
    ('strawberry', 450)
]

prices = ["fruit" for fruit in  fruits]
print(prices)

print("-" * 60)
prices = [fruit for fruit in fruits]
print(prices)

print("-" * 60)
price = [fruit[0] for fruit in fruits]
print(price)

print("-" * 60)
price = [fruit[1] for fruit in fruits]
print(price)

print("-" * 60)
price = [fruit[1] * 0.9 for fruit in fruits]
print(price)

print("-" * 60)
price = [fruit[1] * 0.75 for fruit in fruits]
print(price)

print("-" * 60)
expnFruit = [(fruit[0], fruit[1], fruit[1] * 0.9, fruit[1] * 0.75)
             for fruit in fruits if fruit[1] > 100]
print(expnFruit)
