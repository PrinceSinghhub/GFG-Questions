import collections
class Solution:
    def print_next_greater_freq(self, arr, n):
        res = [-1] * n
        mapp = collections.Counter(arr)
        temp = []

        for idx, val in enumerate(arr):
            if not temp:
                temp.append(idx)
            else:
                curr = mapp[val]
                while temp:
                    prev_idx = temp[-1]
                    prev_freq = mapp[arr[prev_idx]]
                    if prev_freq < curr:
                        res[prev_idx] = val
                        temp = temp[:len(temp) - 1]
                    else:
                        break

                temp.append(idx)

        return res

