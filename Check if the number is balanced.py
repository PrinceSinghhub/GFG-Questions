class Solution:
    def balancedNumber(self, N):
        a = N
        a = str(a)
        l = len(a) // 2
        lhs = []
        rhs = []
        for i in range(len(a)):
            if i > l:
                rhs.append(int(a[i]))
            if i < l:
                lhs.append(int(a[i]))
        if sum(lhs) == sum(rhs):
            return True


if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		N = input ()
		ob = Solution()
		if ob.balancedNumber(N):
			print (1)
		else:
			print (0)


