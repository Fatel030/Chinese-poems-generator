import random

with open('dictionary.txt', encoding='utf-8') as f:
    dictionary = dict.fromkeys(f.read().splitlines())


def generate_poem():
    poem = ''
    for j in range(4):
        line = ''
        for i in range(5):
            candidates = list(dictionary.keys())
            word = random.choice(candidates)
            line += word + ' '
        poem += line.strip() + '\n'
    return poem

print(generate_poem())


