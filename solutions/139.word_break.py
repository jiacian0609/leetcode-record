class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        for word in wordDict:
            if word in s:
                temp = s.split(word)

                if all(len(t) == 0 for t in temp):
                    return True
                
                if all(t in wordDict if len(t) > 0 else True for t in temp):
                    return True

                flag = True
                for t in temp:
                    if len(t) > 0 and not self.wordBreak(t, wordDict):
                        flag = False
                if flag:
                    return True

        return False
        