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
sortedMorse = sorted(morsecode)
sortedDict = dict()
for x in morsecode:
    sortedDict.update({x:morsedict[x]})


def recursive_finder(code, morse, found=None):
    # iteration = iter+1
    # if iteration > 24:
        # time.sleep(3)
    if not morse:
        return found
    if found is None:
        found = []
    for i in range(1, 5):
        # time.sleep(0.1)
        # print("checking for + {}".format(i))
        # print("morse =  {}".format(morse))
        part = code[:i]
        if part in morse:
            tmorse = morse.copy()
            tmorse.remove(part)
            found.append(sortedDict[part])
            # print(iteration)
            # print(str(found)+str(code))
            # print("tmorse = {}".format(tmorse))

            answer = recursive_finder(code[i:], tmorse, found)
            # print(iteration)
            # print(answer)
            if answer is None:
                found.pop()
                #tmorse = [part] + tmorse
                # print("GO BACK")
                # print("GO BACK")
                continue
            return answer

def main():
    counter = 0
    for x in data:
        counter+=1
        print(str(counter) + str(recursive_finder(x,sortedMorse)))

cProfile.run("main()")
# 89.341s runtime for Bonus1