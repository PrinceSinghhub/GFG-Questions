# User function Template for python3

class Solution:
    def search(self, pattern, text):

        indices = []
        text_length = len(text)
        pattern_length = len(pattern)

        # Calculate rolling hash parameters
        prime = 101  # A prime number
        mod = 10 ** 9 + 7  # A large prime number

        # Calculate hash for pattern and first substring of text
        pattern_hash = 0
        text_hash = 0
        for i in range(pattern_length):
            pattern_hash = (pattern_hash * prime + ord(pattern[i])) % mod
            text_hash = (text_hash * prime + ord(text[i])) % mod

        # Iterate through the text to find the pattern
        for i in range(text_length - pattern_length + 1):
            if pattern_hash == text_hash:
                # Check if the substrings match
                if text[i:i + pattern_length] == pattern:
                    indices.append(i + 1)  # Adjust index to 1-based
            if i < text_length - pattern_length:
                # Update rolling hash for the next substring
                text_hash = (text_hash - ord(text[i]) * pow(prime, pattern_length - 1, mod)) % mod
                text_hash = (text_hash * prime + ord(text[i + pattern_length])) % mod
                text_hash = (text_hash + mod) % mod  # Ensure positive value

        return indices


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        for value in ans:
            print(value, end=' ')
        print()
# } Driver Code Ends