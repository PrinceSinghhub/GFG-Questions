class Solution:
    def longest(self, names, n):
        a = {}
        for i in range(0, n):
            a.update({len(names[i]): names[i]})
        return a[max(a.keys())]


def main():
    T = int(input())
    while (T > 0):
        n = int(input())
        names = []
        for i in range(n):
            names.append(input())
        ob = Solution()
        print(ob.longest(names, n))

