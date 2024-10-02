def Rearrange(a, n):
    temp = [i for i in a if i < 0]
    pos = [i for i in a if i >= 0]

    temp.extend(pos)
    a[:] = temp
    return a

print(Rearrange([-3, 3, -2, 2],4))