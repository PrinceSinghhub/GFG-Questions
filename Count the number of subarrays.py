class Solution:
    def countSubarray(self, n, a, l, r):
        def sumlessthanequalto(x):
            start = 0
            end = 0
            sum_ = 0
            count = 0
            while end < n:
                sum_ += a[end]
                while sum_ > x and start <= end:
                    sum_ -= a[start]
                    start += 1
                if start <= end:
                    # as L can be 1 also so L-1 will become 0, thats why for including no element,
                    # start may become end + 1
                    count += end - start + 1
                end += 1
            return count
        return sumlessthanequalto(r) - sumlessthanequalto(l-1)