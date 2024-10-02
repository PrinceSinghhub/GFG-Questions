import string


class Solution:

    # Function to check if a string is Pangram or not.
    def checkPangram(self, s):
        if len(s) < 26:
            return False

        a = set(string.ascii_lowercase)

        return set(s.lower()) >= a