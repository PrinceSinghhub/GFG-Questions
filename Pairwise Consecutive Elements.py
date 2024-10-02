def pairWiseConsecutive(l):
    if len(l) % 2 != 0:
        l.pop()
    for i in range(len(l) // 2):
        if abs(l[i] - l[i + 1]) != 1:
            return False
        else:
            i += 2
    return True

l = [1,2,3,4,50,6,7,8,9]
print(pairWiseConsecutive(l))