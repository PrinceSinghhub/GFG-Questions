class Solution:
    def countWords(self,List, n):
        list = List
        data = (set(list))
        res = 0
        for i in data:
            r = list.count(i)

            if r == 2:
                res += 1
        return res


if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        n = int(input())
        List = input().split()
        ob = Solution()
        print(ob.countWords(List, n))



