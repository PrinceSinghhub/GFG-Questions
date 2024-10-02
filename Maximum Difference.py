from collections import deque


class Solution:
    def findMaxDiff(self, arr):
        # code here
        st1 = deque()
        st2 = deque()

        left = [0 for _ in range(len(arr))]
        right = [0 for _ in range(len(arr))]

        for i in range(len(arr)):
            while st1 and st1[-1] >= arr[i]:
                st1.pop()
            left[i] = st1[-1] if st1 else 0
            st1.append(arr[i])

        for j in range(len(arr) - 1, -1, -1):
            while st2 and st2[-1] >= arr[j]:
                st2.pop()
            right[j] = st2[-1] if st2 else 0
            st2.append(arr[j])
        mx = float('-inf')
        for k in range(len(arr)):
            mx = max(mx, abs(left[k] - right[k]))
        return mx