class Solution:
    def kSubstrConcat(self, n, s, k):
        if n % k != 0:
            return 0

        mp = {}
        for i in range(0, n - k + 1, k):
            temp = s[i:i+k]
            mp[temp] = mp.get(temp, 0) + 1

        if len(mp) <= 2:
            if len(mp) == 1:
                return 1
            else:
                ans = 0
                for value in mp.values():
                    if value == 1:
                        ans += 1
                if ans == 1 or ans == 2:
                    return 1
        return 0



#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		n = int (input ())
		s = input()
		k = int(input())
		ob = Solution()
		print(ob.kSubstrConcat(n,s,k))

# } Driver Code Ends