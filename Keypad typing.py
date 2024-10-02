# todo O(N^2)
def printNumber(s, n):
    mydic = {"ABC": 2, "DEF": 3, "GHI": 4, "JKL": 5, "MNO": 6, "PQRS": 7, "TUV": 8, "WXYZ": 9}
    S = s
    res = ""
    for i in S:
        u = i.upper()
        for n, m in mydic.items():
            Str = str(n)
            if u in Str:
                res += str(m)
    return res


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        n = len(s)
        print(printNumber(s, n))


# todo O(N) best case
s = "geeksquiz"
n = len(s)
a = ""
d = {'a': '2', 'b': '2', 'c': '2', 'd': '3', 'e': '3', 'f': '3', 'g': '4', 'h': '4', 'i': '4',
        'j': '5', 'k': '5', 'l': '5', 'm': '6', 'n': '6', 'o': '6', 'p': '7', 'q': '7', 'r': '7',
        's': '7', 't': '8', 'u': '8', 'v': '8', 'w': '9', 'x': '9', 'y': '9', 'z': '9'}

for i in range(n):
    # print(s[i])
    # print(d[s[i]])
    a += d[s[i]]
print(a)



