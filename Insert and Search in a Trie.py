class Solution:
    def insert(self, root, key):
        curr_node = root
        for c in key:
            if curr_node.children[ord(c) - ord("a")] == None:
                new_node = TrieNode()
                curr_node.children[ord(c) - ord("a")] = new_node
            curr_node = curr_node.children[ord(c) - ord("a")]
        curr_node.isEndOfWord = True
    def search(self, root, key):
        curr_node = root
        for c in key:
            if curr_node.children[ord(c) - ord("a")] == None:
                return False
            curr_node = curr_node.children[ord(c) - ord("a")]
        return curr_node.isEndOfWord