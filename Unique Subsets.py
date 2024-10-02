class Solution:

    def subsetsHelper(self, arr, i, n, cur, res):

        # if all elements are iterated then we store current in result.
        if i >= n:
            res.append(cur[:])
            return

        curInd = i + 1
        # checking for duplicate elements.
        while curInd < n and arr[curInd] == arr[i]:
            curInd += 1

        count = curInd - i

        # inserting all the subsets in current.
        for j in range(0, count + 1):
            for k in range(j):
                cur.append(arr[i])

            # calling function recursively for adding further subsets.
            self.subsetsHelper(arr, curInd, n, cur, res)

            # backtracking to exclude current combinations and
            # include further combinations.
            for k in range(j):
                cur.pop()

    # Function to find all possible unique subsets.
    def AllSubsets(self, arr, n):

        res = []
        cur = []
        arr.sort()

        self.subsetsHelper(arr, 0, n, cur, res)

        # sorting for ascending output.
        res.sort()
        # returning the result.
        return res