class TreeNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
class WordDictionary:
    def __init__(self):
        self.root = TreeNode()
    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TreeNode()
            cur = cur.children[c]
        cur.endOfWord = True
    def search(self, word: str) -> bool:
        def dfs(index, root):
            cur = root
            for i in range(index, len(word)):
                if word[i] == '.':
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                elif word[i] not in cur.children:
                    return False
                cur = cur.children[word[i]]
            return cur.endOfWord
        return dfs(0, self.root)
