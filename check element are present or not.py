# def number_present(num_list, Q):
#     if Q in num_list:
#         return True
#
#
#
# # {
# # Driver Code Starts.
# def main():
#     testcases = int(input())
#     while testcases:
#         num_list = input()
#         num_list = num_list.split()
#         for i in range(len(num_list)):
#             num_list[i] = int(num_list[i])
#
#         q = input()
#         q = q.split()
#         for i in range(len(q)):
#             q[i] = int(q[i])
#
#         for i in range(len(q)):
#             if number_present(num_list, q[i]):
#                 print("True")
#             else:
#                 print("False")
#         testcases -= 1
#
#
# if __name__ == '__main__':
#     main()
#
x = ["apple", "banana","codex"]

y=["apple", "banana",50,"banana"]

# def pr(x,y):
#     if y in x:
#         return y
# def g(x,y):
#     c=pr(x,y)
#     for i in x:
#         if i == c:
#             print("True")
# pr(x,y)
for i in y:
    if i not in x:
        print(False)
    else:
        print(True)