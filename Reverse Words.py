# User function Template for python3

class Solution:

    # Function to reverse words in a given string.
    def reverseWords(self, S):
        temp = []
        store = ""
        for i in S:

            if i == '.':
                store += '.'
                temp.append(store)
                store = ""
            else:
                store += i
        store += '.'
        temp.append(store)

        ans = ""

        for i in range(len(temp) - 1, -1, -1):
            ans += temp[i]
        return ans[:len(ans) - 1]
