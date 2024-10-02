class Solution:

    # Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self, a, b):

        if len(a) == len(b):
            if sorted(a) == sorted(b):
                return True
        else:
            return False

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a,b=map(str,input().strip().split())

        if (Solution().isAnagram(a, b)):
            print("YES")
        else:
            print("NO")
