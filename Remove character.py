class Solution:
    def removeChars(ob, string1, string2):
        a = string1
        b = string2
        res = ""
        for i in a:
            if i in b:
                continue
            else:
                res += i
        return res

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        string1 = input()
        string2 = input()

        ob = Solution()
        print(ob.removeChars(string1, string2))



