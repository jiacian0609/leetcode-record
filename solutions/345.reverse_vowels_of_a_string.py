class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = "aeiouAEIOU"
        temp = []

        for ch in s:
            if ch in vowel:
                temp.append(ch)

        print(temp)

        if temp:
            result = ""
            for ch in s:
                if ch in vowel:
                    result += temp.pop()
                else:
                    result += ch
            return result
        else:
            return s