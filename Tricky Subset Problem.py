class Solution:

    def isPossible(self, S, N, X, A):

        # code here

        newArray = [S]

        sumArr = newArray[0]

        temp = 0

        for i in range(1, N + 1):

            newArray.append(A[i - 1] + sumArr)

            if (newArray[i] > X):
                temp = i

                break

            sumArr += newArray[i]

        for i in range(temp - 1, -1, -1):

            if (X < newArray[i]):

                continue

            else:

                X -= newArray[i]

            if (X == 0):
                return 1

        return 0


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S, N, X = [int(y) for y in input().split()]
        A = input().split()
        for i in range(N):
            A[i] = int(A[i])

        ob = Solution()
        if ob.isPossible(S, N, X, A) == 1:
            print("yes")
        else:
            print("no")
# } Driver Code Ends