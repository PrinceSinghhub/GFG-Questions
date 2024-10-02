def checkArmstrong(n):
    power = len(str(n))
    Sum = 0
    temp = n
    while temp > 0:
        last = temp % 10
        temp = temp // 10
        powr = last ** power
        Sum+=powr

    if Sum == n:
        return True
    else:
        return False

print(checkArmstrong(103032597))