class Solution:
    def farNumber(self, n, a):
        answer = []
        suffix_min = [0 for i in range(n)]
        suffix_min[n - 1] = a[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], a[i])

        for i in range(n):
            low = i + 1
            high = n - 1
            ans = -1

            while (low <= high):
                mid = (low + high) // 2

                # If currnet element in the suffix_min
                # is less than a[i] then move right
                if (suffix_min[mid] < a[i]):
                    ans = mid
                    low = mid + 1
                else:
                    high = mid - 1

            # Print the required answer
            answer.append(ans)
        return answer


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tcs = int(input())
    for _ in range(tcs):
        N = int(input())
        Arr = [int(x) for x in input().split()]

        ob = Solution()
        ans = ob.farNumber(N, Arr)

        for i in ans:
            print(i, end=" ")
        print()
# } Driver Code Ends