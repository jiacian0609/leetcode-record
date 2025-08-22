from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        # BFS
        q = deque([(beginWord, 1)])  # (目前單字, 目前步數)
        visited = set([beginWord])

        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps

            for nextWord in wordList:
                if nextWord not in visited and self.differOne(word, nextWord):
                    visited.add(nextWord)
                    q.append((nextWord, steps + 1))

        return 0  # 找不到路徑
    
    def differOne(self, a: str, b: str) -> bool:
        """回傳兩個字是否剛好差一個字母"""
        count = 0
        for wa, wb in zip(a, b):
            if wa != wb:
                count += 1
            if count > 1:
                return False
        return count == 1