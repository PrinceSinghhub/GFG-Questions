class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self, string):

        try:
            return int(string)
        except:
            return -1


# {
#  Driver Code Starts
# Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        string = input().strip();
        ob = Solution()
        print(ob.atoi(string))