
squares = {x: x ** 2 for x in range(1, 11)}
print(f"squares :{squares}")

print("-" * 60)
sentence = 'the quick brown fox jumps over the lazy dog'
print(f"sentence :{sentence}")

words = {word: len(word) for word in sentence.split()}
print(f"words :{words}")

players = {
    'sachin': [350, 250, 300, 400, 385],
    'rahul': [200, 300, 450, 150, 185],
    'sehwag':[300, 350, 425, 400, 360],
    'sourav':[180, 250, 200, 350, 150],
    'laxman':[345, 300, 200, 150, 190],
    'yuvraj':[190, 150, 120, 250, 275]
}