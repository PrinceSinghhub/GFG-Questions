class Solution:
    def find_height(self, tree, n, k):
        # code here
        tree.sort(reverse=True)

        temp_k = 0
        index = 0

        for i in range(max(tree) - 1, 0, -1):
            # set the index of where tree[index]>i
            while index < n and i < tree[index]:
                index += 1
            temp_k += index
            if temp_k == k:
                return i
            elif temp_k > k:
                return -1

        return -1


# {
#  Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        tree = [int(x) for x in input().strip().split()]
        k = int(input())
        ob = Solution()
        print(ob.find_height(tree, n, k))