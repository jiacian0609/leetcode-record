class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 1:
            if target % candidates[0] != 0:
                return []
            else:
                return [[candidates[0]] * (target // candidates[0])]
        
        candidates.sort()
        dp = defaultdict(list)

        for cur in range(1, target + 1):
            for c in candidates:
                print(f"can: {c}")
                if cur == c:
                    dp[cur].append([c] * (cur // c))
                elif c < cur and (cur - c) in dp:
                    print(f"check {cur - c}")
                    pre = dp[cur - c]
                    print(f"pre: {pre}")
                    for combi in pre:
                        temp = combi.copy()
                        print(f"combi: {temp}")
                        temp.append(c)
                        print(f"new combi: {combi}")
                        temp.sort()
                        if temp not in dp[cur]: # avoid duplicate
                            dp[cur].append(temp)
                elif c > cur:
                    break
                # print(f"{cur}: {dp[cur]}")
            print(dp)
            print("=====")

        return dp[target]