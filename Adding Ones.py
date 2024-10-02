class Solution:
    def update(self, a, n, updates, k):
        for i in range(k):
            a[updates[i]-1] += 1
        for i in range(1,n):
            a[i] += a[i-1]