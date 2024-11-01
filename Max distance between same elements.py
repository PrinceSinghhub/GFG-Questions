class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr):
        # Code here
        mp = {}
        for i in range(len(arr)):
            if arr[i] in mp:
                mp[arr[i]] = [mp[arr[i]][0], i]
            else:
                mp[arr[i]] = [i, 0]
                # print(mp)

        mx = 0
        for k, v in mp.items():
            mx = max(v[1] - v[0], mx)
        return mx


# {
# Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.maxDistance(arr))

# } Driver Code Ends