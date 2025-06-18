'''
https://leetcode.com/problems/implement-trie-prefix-tree/submissions/1668787484/
'''
class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
            else:
                curr = curr[char]
        curr[''] = None

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr:
                return False
            curr = curr[char]
        return '' in curr

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr:
                return False
            curr = curr[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)