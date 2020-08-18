with open('flowers.txt', 'r') as f:
    lines = [i.strip('\n').split(': ') for i in f.readlines()]

flower_dict = {i[0]: i[1] for i in lines}


def flower_lookup(letter: str) -> str:
    letter = letter.capitalize()
    print(flower_dict[letter])

letter = input("Give me a letter in the alphabet: ")

flower_lookup(letter)
