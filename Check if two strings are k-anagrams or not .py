class Solution:

    # Function to check that is
    # k-anagram or not
    def areKAnagrams(self, str1, str2, k):

        MAX_CHAR = 26

        # If both strings are not of equal
        # length then return false
        n = len(str1)
        if (len(str2) != n):
            return False

        count1 = [0] * MAX_CHAR
        count2 = [0] * MAX_CHAR

        # Store the occurrence of all
        # characters in a hash_array
        for i in range(n):
            count1[ord(str1[i]) -
                   ord('a')] += 1

        for i in range(n):
            count2[ord(str2[i]) -
                   ord('a')] += 1

        count = 0

        # Count number of characters that
        # are different in both strings
        for i in range(MAX_CHAR):
            if (count1[i] > count2[i]):
                count = count + abs(count1[i] -
                                    count2[i])

                # Return true if count is less
        # than or equal to k
        return (count <= k)
        # def areKAnagrams(self,str1, str2, k):

    #     c=0
    #     if (len(str1)==len(str2)):
    #         for i in str1:
    #             if i not in str2:
    #                 c+=1
    #     if c<=k:
    #         return 1

    #     return 0


# {
#  Driver Code Starts
# Initial template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = input().strip().split()
        k = int(input())
        ob = Solution()
        if ob.areKAnagrams(arr[0], arr[1], k):
            print(1)
        else:
            print(0)