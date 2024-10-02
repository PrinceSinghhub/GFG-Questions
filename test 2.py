class Solution:
    # Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W, Items, n):

        profit = []
        weight = []
        for i in range(n):
            profit.append(Items[i].value)
            weight.append((Items[i].weight))

        ratio_data = {}
        maxP = 0
        for i in range(n):
            r = profit[i] / weight[i]

            ratio_data[r] = profit[i], weight[i]

        ratio = []
        for key,value in ratio_data.items():
            ratio.append(key)

        ratio.sort()
        dic_data = {}
        for i in range(len(ratio)-1,-1,-1):
            for key, value in ratio_data.items():
                if ratio[i] == key:
                    dic_data[key] = value
        for key, value in dic_data.items():
            if W > 0 and dic_data[key][1]<=W:
                maxP = maxP+dic_data[key][0]
                W = int(W - dic_data[key][1])

            else:
                if W > 0 and dic_data[key][1] > W:
                    div = W/dic_data[key][1]
                    Pi = dic_data[key][0]
                    maxP = maxP+(div*Pi)
                    W = int(W - (div*Pi))

        return maxP

class Item:
    def __init__(self, val, w):
        self.value = val
        self.weight = w


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n, W = map(int, input().strip().split())
        info = list(map(int, input().strip().split()))
        Items = [Item(0, 0) for i in range(n)]
        for i in range(n):
            Items[i].value = info[2 * i]
            Items[i].weight = info[2 * i + 1]

        ob = Solution()
        print("%.2f" % ob.fractionalknapsack(W, Items, n))