T = int(input())
while (T > 0):
    s = input()
    s = sorted(s)
    res = ""
    for i in s:
        res += i
    print(res)
    T -= 1

