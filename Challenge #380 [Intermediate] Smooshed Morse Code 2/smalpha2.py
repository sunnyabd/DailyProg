import random
import cProfile
import time

file = open("smorse2-bonus1.in", "r")
data = file.readlines()
for x in range(len(data)):
    data[x]=data[x].strip()
  #                  2  4    4    3  1  4   3    4    2   4   3   4   2   2  3   4    4    3   3  1  3   4    3   4    4    4
morsecodesource = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.."
morsecode = morsecodesource.split()
morsealph = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
morsedict = dict(zip(morsecode, morsealph))


def recursive_finder(code, morse, found=None):
    if not morse:
        return found
    if found is None:
        found = []
    for i in range(1, 5):
        part = code[:i]
        if part in morse:
            morse.remove(part)
            found.append(morsedict[part])

            answer = recursive_finder(code[i:], morse, found)
            if answer is None:
                found.pop()
                morse.append(part)
                continue
            return answer

def main():
    counter = 0
    for x in data:
        counter+=1
        morsecode2=morsecode.copy()
        print(str(counter) + str(recursive_finder(x, morsecode2)))

cProfile.run("main()")
# 79.192s runtime for Bonus1