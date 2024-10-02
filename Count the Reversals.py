def countRev(s):
    st = []
    ans = 0
    for i in s:
        if i == '{':
            st.append("{")
        elif len(st) == 0:
            ans += 1
            st.append("{")
        else:
            st.pop()
    if len(st) % 2 != 0:
        return -1
    return ans + len(st) // 2


# {
#  Driver Code Starts

t = int(input())
for tc in range(t):
    s = input()
    print(countRev(s))

# Contributed By: Pranay Bansal

# } Driver Code Ends