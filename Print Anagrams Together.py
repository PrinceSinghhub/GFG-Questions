# todo copy past use java code
# a = ["act","god","cat","dog","tac"]
# a = ["no","on","is"]
# first = []
# second = []
# for i in a:
#     if sorted(a[0])==sorted(i):
#         first.append(i)
#     if sorted(a[1])==sorted(i):
#         second.append(i)
# print(first)
# print(second)
def groupAnagrams(words):
    # a list to store anagrams
    anagrams = []

    # base case
    if not words:
        return anagrams

    # sort each word on the list
    A = [''.join(sorted(word)) for word in words]

    # construct a dictionary where the key is each sorted word,
    # and value is a list of indices where it is present
    dict = {}
    for i, e in enumerate(A):
        dict.setdefault(e, []).append(i)

    # traverse the dictionary and read indices for each sorted key.
    # The anagrams are present in the actual list at those indices
    for index in dict.values():
        collection = tuple(words[i] for i in index)
        if len(collection) > 1:
            anagrams.append(collection)

    return anagrams


if __name__ == '__main__':
    # a list of words
    words = ["act","god","cat","dog","tac"]

    anagrams = groupAnagrams(words)
    for anagram in anagrams:
        print(anagram)




