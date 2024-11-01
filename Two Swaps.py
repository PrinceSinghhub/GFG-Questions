class Solution:
    def checkSorted(self, arr):
        # code here
        n = len(arr)
        ans = sorted(arr)
        i = 1
        cnt = 0
        if arr == ans:
            return True
        while i <= n and cnt <= 2:
            if i != arr[i - 1]:
                in1 = arr[i - 1] - 1
                arr[i - 1], arr[in1] = arr[in1], arr[i - 1]
                cnt += 1

            i += 1

            if arr[:] == ans[:] and cnt == 2:
                return True

        if arr == ans and cnt == 2:
            return True
        else:
            return False


# {
# Driver Code Starts
if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        arr = list(map(int, input().split()))

        sol = Solution()
        result = sol.checkSorted(arr)
        if result:
            print("true")
        else:
            print("false")

# } Driver Code Ends