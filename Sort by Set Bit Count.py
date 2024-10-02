
class Solution:
    def sortBySetBitCount(self, arr, n):
       # Your code goes here
       for i in range(n):
           arr[i] = bin(arr[i])[2:]
       arr.sort(key = lambda x:x.count('1'),reverse=True)
       for i in range(n):
           arr[i] = int(arr[i],2)
       return arr

#{
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.sortBySetBitCount(arr, n)
        print(*arr)

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends