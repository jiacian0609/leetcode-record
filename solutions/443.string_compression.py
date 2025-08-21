class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        result = []
        while i < len(chars):
            j = i + 1
            count = 1
            while j < len(chars) and chars[j] == chars[i]:
                count += 1
                j += 1
            result.append(chars[i])
            if count > 1:
                count = str(count)
                for c in count:
                    result.append(c)
            i = j
        chars[:] = result
        # print(chars)
        return len(chars)