orig = "abcabcabc"
check = "bcabcabca"
namelist = open("enable1.txt", "r")

def same_necklace(orig = "nicole", check = "icolen"):
    if len(orig) != len(check):
        return False
    check2 = check+check
    if orig in check2:
        return True
    else:
        return False

def bonus1(orig = "nicole", check = "icolen"):
    counter = 0
    check2 = check
    for x in check:
        if orig == check2:
            counter += 1
        check2 = check2 + x
        check2 = check2[1:]
        print(check2)
    print(counter)

def bonus2(namelist):
    group = []
    names = namelist.readlines()
    for x in range(0,len(names)):
        names[x]=names[x].strip()
    for l in range(0,len(max(names, key = len))):
        for n in names:
            if len(n) == l:
                group.append(n)
        for orig in group:
            groupSame = []
            for check in group:
                if same_necklace(orig,check):
                    groupSame.append(check)
                    group.remove(check)
            if len(groupSame)==4:
                print(groupSame)
                return(groupSame)
                               
            
same_necklace(orig,check)
bonus1(orig,check)
bonus2(namelist)
