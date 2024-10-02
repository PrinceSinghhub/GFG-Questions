class Solution:

    def convert(self, arr, n):
        a = []
        for i in range(len(arr)):
            a.append((arr[i], i))
        a.sort(key=lambda x: x[0])

        for i in range(len(a)):
            ind = a[i][1]
            arr[ind] = i
        return arr