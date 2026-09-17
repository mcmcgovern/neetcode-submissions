class TrieNode:
    def __init__(self):
        self.paths = {}
        self.word = False

    def add(self, word):
        current = self
        for char in word:
            if char not in current.paths:
                current.paths[char] = TrieNode()
            current = current.paths[char]
        current.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Use trie to record each word
        t = TrieNode()
        for w in words:
            t.add(w)

        # Next, define dfs function
        ROWS, COLS = len(board), len(board[0])
        matches, visited = set(), set()

        def dfs(r, c, node, word):
            # check boundaries
            if (r < 0 or c < 0 or
                r == ROWS or c == COLS or
                board[r][c] not in node.paths or (r,c) in visited):
                return

            visited.add((r,c))
            node = node.paths[board[r][c]]
            word += board[r][c]
            if node.word:
                matches.add(word)

            dfs(r+1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c-1,node,word)
            visited.remove((r,c))

        # lastly call dfs
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, t, "")

        return list(matches)



