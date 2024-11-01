# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends
# User function Template for python3

class Solution:
    def subArraySum(self, arr, tar):
        # Dictionary to store the count of prefix sums
        prefix_sum_count = {}
        prefix_sum = 0  # Running prefix sum
        count = 0  # Number of subarrays with sum equal to target

        # Initialize with prefix_sum 0 having occurred once
        prefix_sum_count[0] = 1

        for num in arr:
            # Update the running prefix sum
            prefix_sum += num

            # Check if there is a subarray (prefix[j] - tar = prefix[i])
            if (prefix_sum - tar) in prefix_sum_count:
                count += prefix_sum_count[prefix_sum - tar]

            # Update the prefix_sum in the hashmap
            if prefix_sum in prefix_sum_count:
                prefix_sum_count[prefix_sum] += 1
            else:
                prefix_sum_count[prefix_sum] = 1

        return count

        # Your code here


# {
# Driver Code Starts.
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        tar = int(input())
        ob = Solution()
        res = ob.subArraySum(arr, tar)
        print(res)
        # print("~")
        t -= 1

# } Driver Code Ends