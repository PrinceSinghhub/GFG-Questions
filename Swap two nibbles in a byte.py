class Solution:
    def swapNibbles(self, n: int) -> int:
        assert 0 <= n <= 255
        swapped = ((n & 0x0F) << 4) | ((n & 0xF0) >> 4)
        return swapped