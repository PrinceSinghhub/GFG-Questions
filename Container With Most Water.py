def maxArea(height):
    low = 0
    highe = len(height) - 1

    Max = -1

    while low <= highe:

        temp = min(height[low], height[highe]) * (highe - low)
        Max = max(temp, Max)

        if height[low] < height[highe]:
            low += 1
        else:
            highe -= 1

    return Max


print(maxArea([3,1,2,4,5]))
