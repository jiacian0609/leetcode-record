class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []  # 用來存放所有合法的組合

        # backtrack: 遞迴搜尋組合
        # start: 下一個可選的數字起點 (避免重複使用前面的數字)
        # path: 當前已經選擇的數字組合
        # target: 目前剩下需要湊成的數字和
        def backtrack(start, path, target):
            # 🎯 base case 1: 已經選了 k 個數字
            if len(path) == k:
                if target == 0:   # 剛好和為 n
                    result.append(path[:])  # path[:] 複製一份加入結果
                return
            
            # 從 start 開始選數字，範圍是 [start, 9]
            for num in range(start, 10):
                # 剪枝：如果 num 已經比 target 大，就不用繼續
                if num > target:
                    break

                # 選擇 num，加入 path
                path.append(num)

                # 繼續遞迴，下一輪只能選比 num 大的數字 (避免重複)
                backtrack(num + 1, path, target - num)

                # 回溯：撤銷選擇 num，嘗試其他可能
                path.pop()

        # 從數字 1 開始嘗試，初始 path 為空，目標和是 n
        backtrack(1, [], n)
        return result

    def combinationSum3dp(self, k: int, n: int) -> List[List[int]]:
        if k > n:
            return []

        nums = [[] for _ in range(n + 1)]
        for target in range(1, n + 1):
            for candidate in range(1, 10):
                if candidate < target:
                    combinations = nums[target - candidate]
                    for combi in combinations:
                        if candidate not in combi:
                            nums[target].append(sorted(combi + [candidate]))
                elif candidate == target:
                    nums[target].append([candidate])
                else:
                    break

        result = []
        for combi in nums[-1]:
            if len(combi) == k and combi not in result:
                result.append(combi)

        return result