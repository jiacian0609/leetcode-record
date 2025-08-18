class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
      count_p = defaultdict(int)
      for ch in p:
        count_p[ch] += 1
      print(count_p)

      count_s = defaultdict(int)
      for ch in s[:len(p)]:
        if ch in p:
          count_s[ch] += 1
      print(count_s)

      result = []
      idx = 0
      found = False
      while count_p != count_s and idx + len(p) < len(s):
        if s[idx] in p:
          count_s[s[idx]] -= 1
        if s[idx + len(p)] in p:
          count_s[s[idx + len(p)]] += 1
        idx += 1
      if count_p == count_s: found = True
      
      if found:
        result = [idx]
      else:
        return result

      for i in range(idx, len(s) - len(p)):
        if s[i] in p:
          count_s[s[i]] -= 1
        if s[i + len(p)] in p:
          count_s[s[i + len(p)]] += 1
        print(i, count_s)
        if count_p == count_s:
          result.append(i + 1)
      
      return result