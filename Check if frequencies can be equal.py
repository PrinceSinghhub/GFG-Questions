# User function Template for python3
from string import ascii_lowercase


class Solution:
    def sameFreq(self, s):
        letter_count = [s.count(letter) for letter in ascii_lowercase if s.count(letter) is not 0]
        return len(set(letter_count)) == 1 or (len(set(letter_count)) == 2 and (
                    min(letter_count) == 1 or letter_count.count(max(letter_count)) == 1 and max(letter_count) - min(
                letter_count) <= 1))

        # code here


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        s = input()
        ob = Solution()
        answer = ob.sameFreq(s)
        if answer:
            print(1)
        else:
            print(0)

# } Driver Code Ends