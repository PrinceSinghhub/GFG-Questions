# User function Template for python3

# User function Template for python3

class Solution:
    def armstrongNumber(self, n):
        a = n // 100
        b = (n // 10) % 10  # Tens place
        c = n % 10  # Units place

        # Calculate the sum of cubes of digits
        sum_of_cubes = a ** 3 + b ** 3 + c ** 3

        # Check if the sum of cubes is equal to the original number
        if sum_of_cubes == n:
            return "true"
        return "false"


# {
# Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        n = int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))

# } Driver Code Ends