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
morsedict = dict(zip(morsecode,morsealph))

def recursive_finder(sequence, available,found):
    if not sequence:
        # print(found)
        return found

    for i in range(1,5):
        part = sequence[:i]
        if part in available:
            # print(part)
            # print(morsedict[part]+sequence[i:])
            # print(available)
            temp = available.copy()
            temp.remove(part)
            found.append(morsedict[part])
            # print(sequence[i:])
            answer = recursive_finder(sequence[i:],temp, found)
            if answer == None:
                # print("GO BACK")
                found.pop()
                continue
            # time.sleep(100)
            # print(answer)
            return answer

def main():
    counter = 0
    for x in data:
        counter+=1
        print(str(counter) + str(recursive_finder(x, set(morsedict), [])))
        #time.sleep(100)

cProfile.run("main()")
# 0.496s runtime for Bonus1