class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for l in magazine:
            if l in ransomNote:
                # print(l)
                ransomNote = ransomNote.replace(l, "", 1)
                # print(ransomNote)
        
        if len(ransomNote) == 0:
            return True
        else: return False
        