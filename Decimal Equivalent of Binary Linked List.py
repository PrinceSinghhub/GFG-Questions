class Solution:
    def decimalValue(self, head):
        MOD = 10 ** 9 + 7
        decimal_value = 0

        while head:
            decimal_value = (decimal_value * 2 + head.data) % MOD
            head = head.next

        return decimal_value