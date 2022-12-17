from random import randint

with open('wordlist.txt') as f:
    list = f.read().splitlines()


def word():
    return list[randint(0, len(list)-1)]
