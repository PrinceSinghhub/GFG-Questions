import bisect


class Solution:
    def numOfSubsets(self, arr, n, k):
        # declare four vector for dividing
        # array into two halves and storing
        # product value of possible subsets
        # for them
        vect1, vect2, subset1, subset2 = [], [], [], []

        # ignore element greater than k and
        # divide array into 2 halves
        for i in range(0, n):

            # ignore element if greater than k
            if arr[i] > k:
                continue
            if i <= n // 2:
                vect1.append(arr[i])
            else:
                vect2.append(arr[i])

                # generate all subsets for 1st half (vect1)
        for i in range(0, (1 << len(vect1))):
            value = 1
            for j in range(0, len(vect1)):
                if i & (1 << j):
                    value *= vect1[j]
                if value > k:
                    break

            # push only in case subset product
            # is less than equal to k
            if value <= k:
                subset1.append(value)

                # generate all subsets for 2nd half (vect2)
        for i in range(0, (1 << len(vect2))):
            value = 1
            for j in range(0, len(vect2)):
                if i & (1 << j):
                    value *= vect2[j]
                if value > k:
                    break

            # push only in case subset product
            # is less than equal to k
            if value <= k:
                subset2.append(value)

                # sort subset2
        subset2.sort()

        count = 0
        for i in range(0, len(subset1)):
            count += bisect.bisect(subset2, (k // subset1[i]))

        # for null subset decrement the
        # value of count
        count -= 1

        # return count
        return count 