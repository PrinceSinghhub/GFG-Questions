import statistics


class Solution:
    def MedianOfArrays(self, array1, array2):
        # code here
        array1.extend(array2)
        med = float(statistics.median(array1))
        if med.is_integer():
            return int(med)
        else:
            return med


# {
#  Driver Code Starts
if __name__ == '__main__':
    tcs = int(input())

    for _ in range(tcs):
        m = input()
        arr1 = [int(x) for x in input().split()]
        n = input()
        arr2 = [int(x) for x in input().split()]

        ob = Solution()
        print(ob.MedianOfArrays(arr1, arr2))