class Solution:

    # Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self, arr, n):

        s = set([])
        prefix_sum = 0
        for i in range(n):
            prefix_sum += arr[i]
            if prefix_sum in s:
                return True
            if prefix_sum == 0:
                return True
            s.add(prefix_sum)
        return False

        # arr.sort()

        # for i in range(n):
        #     Sum = arr[i]

        #     for j in range(i+1,n):

        #         Sum+=arr[j]
        #         if Sum == 0:
        #             return "Yes"

        # return "No"


# {
#  Driver Code Starts
# Initial Template for Python 3


def main():
    T = int(input())
    while (T > 0):

        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        if (Solution().subArrayExists(arr, n)):
            print("Yes")
        else:
            print("No")

        T -= 1


if __name__ == "__main__":
    main()