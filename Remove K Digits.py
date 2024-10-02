#User function Template for python3

class Solution:

    def removeKdigits(self, S, K):
        # code here
        length = len(S)
        if K == length:
            return "0"

        result = []
        i = 0
        while i < length:
            while K > 0 and result and result[-1] > S[i]:
                result.pop()
                K -= 1
            result.append(S[i])
            i += 1

        while K > 0:
            result.pop()
            K -= 1

        ptr = 0
        while ptr < len(result) and result[ptr] == '0':
            ptr += 1

        result = result[ptr:]
        return "0" if not result else "".join(result)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()
        K = int(input())

        obj = Solution()

        ans = obj.removeKdigits(S, K)

        print(ans)


# } Driver Code Ends