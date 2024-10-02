class Solution:
    # Function to reverse every sub-array group of size k.
    def reverseInGroups(self, arr, N, K):
        for i in range(0, N, K):
            arr[i:i + K] = arr[i:i + K][::-1]
        return arr




def main():
    T = int(input())
    while (T > 0):
        nk = [int(x) for x in input().strip().split()]
        N = nk[0]
        K = nk[1]
        arr = [int(x) for x in input().strip().split()]

        ob = Solution()
        ob.reverseInGroups(arr, N, K)
        for i in arr:
            print(i, end=" ")
        print()
        T -= 1


if __name__ == "__main__":
    main()
