#User function Template for python3

class Solution():
    def lexicographicallyLargest(self, a, n):
        #your code here
        b=[]
        small=[]
        for i in range(n):
            if not small:
                small.append(a[i])
            elif not (small[-1]+a[i])%2:
                small.append(a[i])
            else:
                small.sort()
                while small:
                    b.append(small.pop())
                small.append(a[i])
        if small:
            small.sort()
            while small:
                b.append(small.pop())
        return b

#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        a = [int(i) for i in input().split()]
        ans = Solution().lexicographicallyLargest(a, n)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends