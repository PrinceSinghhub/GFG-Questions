class Solution:
    def valueEqualToIndex(self,arr, n):
        a =""
        b =0
        for i in range(len(arr)):

            if arr[b] == i:
                a=a+ str(i)

                return a
            b+=1
            return ''
# 1 335 501 170 725 479 359 963 465 706 146 12 828 962 492 996 943 828 437 392 605 903 154 293 383 422 717 719 896 448 727 772 539 870 913 668 300 36 895 704 812 323

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.valueEqualToIndex(arr, n)

        if len(ans) == 0:
            print("Not Found")
        else:
            for x in ans:
                print(x, end=" ")
            print()
        tc -= 1