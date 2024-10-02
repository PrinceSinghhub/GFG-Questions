def convertFive(n):
    ans = ""
    arr = list(str(n))

    for i in arr:
        if i == '0':
            ans += '5'
        else:
            ans += i
    return int(ans)
# return int(str(n).replace('0','5'))


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        print(convertFive(int(input().strip())))



