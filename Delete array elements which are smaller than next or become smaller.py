def deleteElement (arr, n, k) : 

    #Complete the function

    c=0

    l=[]

    l.append(arr.pop(0))

    while c!=k:

        if l==[]:

            l.append(arr.pop(0))

        else:

            if arr:

                if l[-1]<arr[0]:

                    l.pop()

                    c+=1

                else:

                    l.append(arr.pop(0))

            else:

                return l

    return l+arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    k = int(input())
    ans = deleteElement(arr, n, k)
    print(*ans)
# } Driver Code Ends