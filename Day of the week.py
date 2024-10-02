# User function Template for python3

class Solution:
    def getDayOfWeek(self, d, m, y):
        # code here

        # some considerations ->
        # Taking March as 1st month of year, and so on ..
        # for Jan and Feb, taking previous year
        # e.g. if 1/1/1990, Y = 1989

        if (m == 1 or m == 2):
            y = y - 1
            if (m == 1):
                m = 11
            else:
                m = 12
        else:
            m = m - 2

        C = int(y / 100)  # century e.g. 1990, C = 19
        Y = int(y % 100)  # last two digit of year, Y = 90

        weeks = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

        # Trick formula as per Gregorian calender
        w = int((d + (2.6 * m - 0.2) - 2 * C + (Y) + int(Y / 4) + int(C / 4)) % 7)
        return weeks[w]


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        d, m, y = map(int, input().split())

        ob = Solution()
        print(ob.getDayOfWeek(d, m, y))
# } Driver Code Ends