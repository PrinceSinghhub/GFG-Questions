class Solution:
    def maxSubstring(self, S):
        once = -1
        zeros = 0
        for i in S:
            if i == "0":
                zeros += 1
            else:
                zeros -= 1
            once = max(once, zeros)

            if zeros < 0:
                zeros = 0

        return once


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()

		ob = Solution()
		answer = ob.maxSubstring(s)
		print(answer)
