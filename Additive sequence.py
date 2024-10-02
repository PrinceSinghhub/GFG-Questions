
class Solution:

    def checkIsAdditive(self,nums):
        '''Takes in a array of numbers and checks if its additive'''
        if len(nums) < 3:
            return True

        for i in range(2, len(nums)):
            if int(nums[i-2]) + int(nums[i-1]) != int(nums[i]):
                return False

        return True

    def isAdditiveSequence(self,num):
        additiveSubsequenceFound = False

        def recur(str, sub):
            nonlocal additiveSubsequenceFound
            if len(str) == 0:
                if len(sub.split(' ')) >= 3 and self.checkIsAdditive(sub.split(' ')):
                    additiveSubsequenceFound = True
                return

            if additiveSubsequenceFound:
                return

            if len(sub) != 0 and self.checkIsAdditive(sub.split(' ')):
                recur(str[1:], sub + ' ' + str[0])
            recur(str[1:], sub + str[0])

        recur(str(num), '')
        return 1 if additiveSubsequenceFound else 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        s=input()

        print(isAdditiveSequence(s))
# } Driver Code Ends