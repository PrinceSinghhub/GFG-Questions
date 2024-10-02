def stockBuySell(price, n):
    # Prices must be given for at least two days
    if (n == 1):
        return

    flag = False
    # Traverse through given price array
    i = 0
    while (i < (n - 1)):

        # Find Local Minima
        # Note that the limit is (n-2) as we are
        # comparing present element to the next element
        while ((i < (n - 1)) and (price[i + 1] <= price[i])):
            i += 1

        # If we reached the end, break
        # as no further solution possible
        if (i == n - 1):
            break

        # Store the index of minima
        buy = i
        i += 1

        # Find Local Maxima
        # Note that the limit is (n-1) as we are
        # comparing to previous element
        while ((i < n) and (price[i] >= price[i - 1])):
            i += 1

        # Store the index of maxima
        sell = i - 1

        print("(" + str(buy) + " " + str(sell) + ")", end=" ")
        flag = True
    if flag == False:
        print("No Profit", end="")
    print()