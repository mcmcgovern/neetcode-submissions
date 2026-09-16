class TrieNode:
    def __init__(self, new_word=False):
        self.paths = {}
        self.word = new_word

class PrefixTree:

    def __init__(self):
        self.tree = TrieNode()

    def insert(self, word: str) -> None:
        current = self.tree
        for char in word:
            if char not in current.paths: # we are continuing down existing tree
                current.paths[char] = TrieNode() # we are building new path    
            current = current.paths[char] # advance down path
        current.word = True


    def search(self, word: str) -> bool:
        current = self.tree
        for char in word:
            if char not in current.paths:
                return False # we have reached a dead end
            current = current.paths[char]
        return current.word
        

    def startsWith(self, prefix: str) -> bool:
        current = self.tree
        for char in prefix:
            if char not in current.paths:
                return False
            current = current.paths[char]
        return True
        
        