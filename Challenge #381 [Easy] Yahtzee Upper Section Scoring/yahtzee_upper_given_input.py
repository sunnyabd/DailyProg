import cProfile
# load and sort rolls. given that yahtzee gives rolls in ascending order
rolls = open("yahtzee-upper-1.txt", "r")
roll = []
for x in rolls.readlines():
    roll.append(int(x.strip()))
roll = sorted(roll)


def yahtzee_upper(roll = [2, 3, 5, 5, 6]):

    # initialize variables
    # since numbers sorted, similar numbers will be grouped together,
    # currNum used to find last of group of numbers
    # count used to count how many of the same numbers are in the roll
    # highscore used to save highest score
    currNum = 0
    count = 1
    highscore = 0
    roll.append(0)
    for nextNum in roll:
        if currNum != nextNum:
            if currNum*count > highscore:
                highscore = currNum*count
            currNum = nextNum
            count = 1
        elif currNum == nextNum:
            count += 1
    print(highscore)

#print(yahtzee_upper([1, 1, 1, 3, 3]))
cProfile.run('yahtzee_upper(roll)')
# 0.011s function runtime