class Solution:
    def findOnce(self,arr,n):
        r = arr[0]
        for i in range(1, n):
            r = r ^ arr[i]

        return r
# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.findOnce(arr, n))

# d= [1, 1, 2, 4, 4, 5, 5, 6, 6]
# r=d[0]
# for i in range(1,len(d)):
#     r=r^d[i]
#     print(r)
# print(r)

# x=[]
# sig=[]
# n=len(d)
# for i in range(n):
#     for j in range(i+1,n):
#         if d[i] == d[j]:
#             x.append(d[i])
#
# d=set(d)
# d=list(d)
# for a in d:
#     for b in x:
#         if a not in b:
#             print(a)
#
#
# print(x)
# print(d)