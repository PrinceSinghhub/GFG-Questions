class Solution:
    def chooseandswap(self, a):
        # code here
        s = list(set(a))
        s.sort()
        # print(s)
        for smallestchar in s:
            # print(smallestchar)
            smallestpos = a.index(smallestchar)
            found = False
            for ch in a:
                if ch > smallestchar:
                    found = True
                    break
            if not found:
                continue
            biggerpos = a.index(ch)

            # print(smallestpos,biggerpos)
            if biggerpos < smallestpos:
                a = a.replace(ch, '#')
                a = a.replace(smallestchar, ch)
                a = a.replace('#', smallestchar)
                return a

        # print(ch)
        return a




if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        A = input()
        ans = ob.chooseandswap(A)
        print(ans)