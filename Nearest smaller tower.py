#User function Template for python3

class Solution:
    def nearestSmallestTower(self,arr):
        stk = []
        stk2 = []
        size = len(arr)
        left = [0] * size
        right = [0] * size

        # find the nearest smaller tower on the left side
        for i in range(size):
            while stk and arr[stk[-1]] >= arr[i]:
                stk.pop()
            if stk:
                left[i] = stk[-1]
            else:
                left[i] = -1
            stk.append(i)

        # find the nearest smaller tower on the right side
        for i in range(size - 1, -1, -1):
            while stk2 and arr[stk2[-1]] >= arr[i]:
                stk2.pop()
            if stk2:
                right[i] = stk2[-1]
            else:
                right[i] = -1
            stk2.append(i)

        ans = [0] * size

        # compare the distances and heights of the left and right towers
        for i in range(size):
            if left[i] == -1 and right[i] == -1:
                ans[i] = -1
            elif left[i] == -1:
                ans[i] = right[i]
            elif right[i] == -1:
                ans[i] = left[i]
            else:
                diff_left = i - left[i]
                diff_right = right[i] - i
                if diff_left < diff_right:
                    ans[i] = left[i]
                elif diff_left > diff_right:
                    ans[i] = right[i]
                else:
                    if arr[left[i]] < arr[right[i]]:
                        ans[i] = left[i]
                    elif arr[left[i]] > arr[right[i]]:
                        ans[i] = right[i]
                    else:
                        ans[i] = left[i]

        return ans


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input().strip())):
        N=int(input())
        arr=[int(i) for i in input().strip().split()]
        obj=Solution()
        ans=obj.nearestSmallestTower(arr)
        for i in ans:
            print(i,end=" ")
        print()
# } Driver Code Ends