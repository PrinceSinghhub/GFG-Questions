class Solution:
    def min_sprinklers(self, gallery, n):
        # code here
        range_list = [[0, 0] for _ in range(n)]

        for i in range(n):
            if gallery[i] == -1:
                continue
            range_list[i][0] = max(0, i - gallery[i])
            range_list[i][1] = min(n, i + gallery[i])

        range_list.sort(key=lambda x: x[0])

        start, i, res = 0, 0, 0
        curr_max = -1

        while start < n:
            while i < n:
                if range_list[i][0] > start:
                    break
                curr_max = max(curr_max, range_list[i][1])
                i += 1

            if curr_max < start:
                return -1

            res += 1
            start = curr_max + 1

        return res