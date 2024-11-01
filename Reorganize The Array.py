#{
 # Driver Code Starts

# } Driver Code Ends
class Solution:
    def rearrange(self, arr):
        n=len(arr)
        for item in arr:
            if item!=-1:
                idx=item%n
                if arr[idx]!=-1:
                    arr[idx]+=n
                else:
                    arr[idx]=n+idx
        for i in range(n):
            if arr[i]>=n:
                arr[i]=i
            else:
                arr[i]=-1
        return arr

#{
 # Driver Code Starts.
def main():
    t = int(input())
    for _ in range(t):
        input_str = input()
        arr = list(map(int, input_str.split()))
        solution = Solution()
        ans = solution.rearrange(arr)
        print(" ".join(map(str, ans)))

if __name__ == "__main__":
    main()
# } Driver Code Ends