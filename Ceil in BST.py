class Solution:

    def inOrder(self, root):

        if root == None:
            return []
        arr = []

        arr += self.inOrder(root.left)
        if root != None:
            arr.append(root.key)
        arr += self.inOrder(root.right)

        arr.sort()
        return arr

    def findCeil(self, root, inp):

        ans = self.inOrder(root)

        if inp in ans:
            return inp

        first = 0
        last = len(ans)

        while first <= last:
            mid = (first + last) // 2

            if ans[mid] < inp:
                first = mid + 1
            if ans[mid] > inp:
                for i in ans[first:last]:
                    if i > inp:
                        return i


# optimize code
class Solution:
    def findCeil(self, root, inp):
        # code here
        ans = 0
        while root:
            if inp < root.key:
                ans = root.key
                root = root.left
            elif inp == root.key:
                ans = inp
                break
            else:
                root = root.right
        return ans