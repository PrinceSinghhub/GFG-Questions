from bisect import bisect_left as bl


class Solution:

    def binPartition(self, a, value):
        return bl(a, value) - 1

    def countArray(self, a, n):
        if n < 3:
            return [-1]
        left = [-1, a[0]]
        result = [-1]
        right = max(a[1:])
        maxproduct = -1
        for i in range(1, n - 1):
            current = a[i]
            if current >= right:
                right = max(a[i + 1:])
            # print(current)
            j = self.binPartition(left, current)

            leftValue = left[j]
            left.insert(j + 1, current)  # =left[:j+1] + [current] + left[j+1:]
            # left.append(current)
            # left.sort()
            rightValue = right
            # print([leftValue,current,rightValue])
            if not (leftValue < current and current < rightValue):
                continue
            currentprod = leftValue * rightValue * current
            if currentprod > maxproduct:
                maxproduct = currentprod
                result = [leftValue, current, rightValue]

        return result