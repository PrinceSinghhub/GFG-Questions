class Solution:
    def binaryPalin (self, N):
        Bin = bin(N)
        Str = str(Bin)
        orgbin = Str[2::]
        rev = orgbin[::-1]

        if orgbin == rev:
            return 1
        else:
            return 0


if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		n = int (input ())
		ob = Solution()
		print(ob.binaryPalin(n))