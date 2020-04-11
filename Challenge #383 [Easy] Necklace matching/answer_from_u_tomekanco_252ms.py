from collections import defaultdict
TARGET = 4

def canon(str_):
    L = [str_]
    for _ in range(len(str_)):
        str_ = str_[1:] + str_[0]
        L.append(str_)
    return min(L)    

def solve_problem(file):
    with open(file) as f:
        text = f.read().split('\n')

    D = {}
    for word in sorted(text, key=len):
        idx = canon(word)
        D[idx].append(word)  
        if len(D[idx]) ==TARGET:
            print(D[idx])
            return D[idx]

solve_problem('enable1.txt')

