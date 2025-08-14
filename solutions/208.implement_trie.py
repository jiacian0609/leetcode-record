class Trie:

    def __init__(self):
        self.root = {}
        

    def insert(self, word: str) -> None:
        cur = self.root

        for w in word:
            if w not in cur:
                cur[w] = {}
            cur = cur[w]
        
        cur['*'] = ''


    def search(self, word: str) -> bool:
        cur = self.root

        for w in word:
            if w not in cur:
                return False
            else:
                cur = cur[w]
        
        return '*' in cur
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for w in prefix:
            if w not in cur:
                return False
            else:
                cur = cur[w]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)