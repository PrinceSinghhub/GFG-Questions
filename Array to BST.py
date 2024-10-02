class TreeNode:
    def __init__(self, d):
        self.val = d
        self.left = None
        self.right = None


def preOrder(root, ans):
    if (not root):
        return
    ans.append(root.val)
    preOrder(root.left, ans)
    preOrder(root.right, ans)


def insert(root, val):
    if (not root):
        root = TreeNode(val)
        return root
    if root.val > val: return insert(root.left, val)
    return insert(root.right, val)


def fun(root, nums, l, r):
    mid = (l + r) // 2
    root = insert(root, nums[mid])
    if mid != l:
        root.left = fun(root, nums, l, mid - 1)
    if mid != r:
        root.right = fun(root, nums, mid + 1, r)
    return root


class Solution:
    def sortedArrayToBST(self, nums):
        # Code here
        ans = []
        if len(nums) == 0:
            return ans
        root = fun(None, nums, 0, len(nums) - 1)
        preOrder(root, ans)
        return ans


# {
#  Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        nums = list(map(int, input().split()))
        obj = Solution()
        ans = obj.sortedArrayToBST(nums)
        for _ in ans:
            print(_, end=" ")
        print()