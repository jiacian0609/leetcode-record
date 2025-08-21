class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(' ')
        result = []
        for word in arr[::-1]:
            if word != '':
                result.append(word)
        # print(result)
        return " ".join(result)