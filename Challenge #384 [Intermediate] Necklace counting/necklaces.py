import string

alphabets = string.printable
print(alphabets)


# similar to easy challenge, iterates through all words in list, takes a word, doubles it and removes all
# other shifted combinations of the word.
# uses tempPerms to store the part of perms where we search for duplicates
# this is so we dont compare with words we've already cleared.
def check(perms):
    counter = 0
    while counter < len(perms):
        letters = perms[counter]
        size = len(letters)
        letterDouble = letters+letters
        tempPerms = perms[counter+1:]
        for i in range(1, size):
            try:
                tempPerms.remove(str(letterDouble[i:(i+size)]))
            except:
                continue
        perms = perms[:counter+1] + tempPerms
        counter += 1
    print(perms)
    return perms


# BFS(Breadth-First-Search) recursion algo to generate all possible combinations
# letters = int, length = int
def perms(letters, length, curr=[]):
    if length == 0:
        yield curr
        return
    for i in alphabets[0:letters]:
        curr.append(i)
        yield from perms(letters, length-1, curr)
        curr.pop()


def necklace(alpha, length):
    perm = list()
    # generates permutations
    for i in perms(alpha,length):
        perm.append("".join(map(str,i)))
    # checks
    return len(check(perm))

print(necklace(123,18))

