class Solution:

    # Returns next palindrome of a given number num[].
    # This function is for input type 2 and 3
    def generateNextPalindromeUtil(self, num, n):

        # find the index of mid digit
        mid = int(n // 2)

        # A bool variable to check if copy of left
        # side to right is sufficient or not
        leftsmaller = False

        # end of left side is always 'mid -1'
        i = mid - 1

        # Beginning of right side depends
        # if n is odd or even
        j = mid + 1 if (n % 2) else mid

        # Initially, ignore the middle same digits
        while (i >= 0 and num[i] == num[j]):
            i -= 1
            j += 1

        # Find if the middle digit(s) need to be
        # incremented or not (or copying left
        # side is not sufficient)
        if (i < 0 or num[i] < num[j]):
            leftsmaller = True

        # Copy the mirror of left to tight
        while (i >= 0):
            num[j] = num[i]
            j += 1
            i -= 1

        # Handle the case where middle
        # digit(s) must be incremented.
        # This part of code is for CASE 1 and CASE 2.2
        if (leftsmaller == True):

            carry = 1
            i = mid - 1

            # If there are odd digits, then increment
            # the middle digit and store the carry
            if (n % 2 == 1):

                num[mid] += carry
                carry = int(num[mid] // 10)
                num[mid] %= 10
                j = mid + 1

            else:
                j = mid

            # Add 1 to the rightmost digit of the
            # left side, propagate the carry
            # towards MSB digit and simultaneously
            # copying mirror of the left side
            # to the right side.
            while (i >= 0):
                num[i] += carry
                carry = num[i] // 10
                num[i] %= 10
                num[j] = num[i]  # copy mirror to right
                j += 1
                i -= 1

    # The function that prints next
    # palindrome of a given number num[]
    # with n digits.
    def generateNextPalindrome(self, num, n):
        ans = []
        # Input type 1: All the digits are 9, simply o/p 1
        # followed by n-1 0's followed by 1.
        if (self.AreAll9s(num, n) == True):

            ans.append(1)
            for i in range(1, n):
                ans.append(0)
            ans.append(1)


        # Input type 2 and 3
        else:

            self.generateNextPalindromeUtil(num, n)

            # print the result
            ans = num
        return ans

    # A utility function to check if num has all 9s
    def AreAll9s(self, num, n):
        for i in range(0, n):
            if (num[i] != 9):
                return 0
        return 1