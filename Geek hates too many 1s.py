class Solution:

    def noConseBits(self, n: int) -> int:

        # code here

        list1 = list(bin(n)[2:])

        count = 0

        k = 0

        for i in list1:

            if i == '1' and count != 2:

                count = count + 1

            elif count == 2:

                list1[k] = '0'

                count = 0

            else:

                count = 0

            k = k + 1

        str1 = ""

        str1 = str1.join(list1)

        return int(str1, 2)


# {
# Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())

        obj = Solution()
        res = obj.noConseBits(n)

        print(res)

# } Driver Code Ends