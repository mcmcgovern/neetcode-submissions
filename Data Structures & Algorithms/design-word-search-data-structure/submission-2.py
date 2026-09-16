class TrieNode:
    def __init__(self):
        self.paths = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.trie
        for char in word:
            if char not in current.paths:
                current.paths[char] = TrieNode()
            current = current.paths[char]
        current.word = True

    def search(self, word: str) -> bool:
        
        def dfs(index, root):
            current = root
            for i in range(index, len(word)):
                char = word[i]
                if char == '.':
                    # need to perform recursion, searching all paths
                    for path in current.paths.values():
                        if dfs(i+1, path):
                            return True
                    return False
                else:
                    # do normal traversal
                    if char not in current.paths:
                        return False
                    current = current.paths[char]
            return current.word
        return dfs(0, self.trie)
