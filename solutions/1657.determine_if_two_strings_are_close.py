from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        c1, c2 = Counter(word1), Counter(word2)
        
        # 條件 1: 字母集合必須相同
        if set(c1.keys()) != set(c2.keys()):
            return False
        
        # 條件 2: 頻率集合必須相同
        if sorted(c1.values()) != sorted(c2.values()):
            return False
        
        return True