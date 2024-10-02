def findAll():

    r={'1','2','3'}
    for val in range(1,1000001):
        s=set(str(val))
        if s.issubset(r):
            mp[val]=1
    #code here

#{
#  Driver Code Starts
#Initial Template for Python 3

mp = {}

#Position this line where user code will be pasted.


if __name__ == '__main__':
    findAll()
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr=[int(x) for x in input().strip().split()]
        arr.sort()
        flag = 0
        for i in range(n):
            if arr[i] in mp:
                print(arr[i], end=" ")
                flag=1
        if(flag==0):
            print(-1)
        else:
            print()