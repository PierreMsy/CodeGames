import sys
import math


# double parcours d'arbre:
# 1 pour le morse to letter et un pour les mots.
# un curseur qui parcours la liste de symbole.

# 1) conversion du dictionnaire et des mots en 1 arbre.
# 2) itération sur le code, on lance un décoding à partir de chaque caractère.
translater = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..'
}

class Node():

    def __init__(self, end):
        self.p = None
        self.b = None 
        self.end = end

def display_in_depth(bt):
    
    if bt.p is not None:
        if bt.p.end:
            print(f'.    END', file=sys.stderr)
        else:
            print(f'.', file=sys.stderr)
        display_in_depth(bt.p)
    if bt.b is not None:
        if bt.b.end:
            print(f'-    END', file=sys.stderr)
        else:
            print(f'-', file=sys.stderr)
        display_in_depth(bt.b)

def add_word_to_bt(bt, word_symbols):

    word_symbols = []
    for letter in word:
        for symbol in translater[letter]:
            word_symbols.append(symbol)

    current = bt

    for symbol in word_symbols[:-1]:
        if symbol == '.':
            if current.p is None:
                current.p = Node(False)
            current = current.p
        else:
            if current.b is None:
                current.b = Node(False)
            current = current.b
    
    if word_symbols[-1] == '.':
        if current.p is None:
            current.p = Node(True)
        else:
            current.p.end=True
    else:
        if current.b is None:
            current.b = Node(True)
        else:
            current.b.end=True

    return bt
    
bt_words = Node(False)    

code = input()
nbr_words = int(input())

for _ in range(nbr_words):
    word = input()
    bt_words = add_word_to_bt(bt_words, word)
    print(word, file=sys.stderr)

#display_in_depth(bt_words)

for symbol in code:
    

print("answer")
