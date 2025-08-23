# Trie 節點
class TrieNode:
    def __init__(self):
        self.children = dict()  # 子節點
        self.words = list()     # 儲存當前 prefix 下最多 3 個產品
        self.n = 0              # 當前 prefix 下 products 數量

# Trie 樹
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    # 新增一個單字到 Trie
    def add_word(self, word):
        node = self.root
        for c in word:
            # 如果該字母還沒有子節點，建立新的 TrieNode
            if c not in node.children: 
                node.children[c] = TrieNode()
            node = node.children[c] 
            # 每個節點最多儲存三個產品
            if node.n < 3:
                node.words.append(word)
                node.n += 1
        
    # 根據 prefix 找出最多三個產品
    def find_word_by_prefix(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:  # 如果 prefix 不存在 → 回傳空列表
                return []
            node = node.children[c] 
        return node.words  # 回傳該 prefix 下的產品建議
            
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()           # 先排序，確保字典序
        trie = Trie()             # 建立 Trie
        for word in products:     
            trie.add_word(word)   # 將每個產品加入 Trie
        
        ans, cur = [], ''
        for c in searchWord:
            cur += c
            # 對當前 prefix 查詢建議
            ans.append(trie.find_word_by_prefix(cur))
        return ans