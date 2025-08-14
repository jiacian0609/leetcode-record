class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        count_t = defaultdict(int)
        for ch in t:
            count_t[ch] += 1
        
        t_remain = len(t)
        min_window = (0, float(inf))
        start = 0

        for end, ch in enumerate(s):
            if count_t[ch] > 0:  # 需要的字
                t_remain -= 1
            count_t[ch] -= 1  # 如果 < 0 表示有多包含不需要的字
            # 最後 count_t 應都 <= 0

            if t_remain == 0:  # 需要的字都包含
                while True:  # 移動起點，縮小視窗到不能再縮
                    start_ch = s[start]
                    if count_t[start_ch] == 0:  # 是需要的字
                        break
                    # 右移
                    count_t[start_ch] += 1
                    start += 1

                # 更新最小視窗
                if end - start < min_window[1] - min_window[0]:
                    min_window = (start, end)

                # for 下一輪，從現有起點往右一格
                count_t[s[start]] += 1
                t_remain += 1
                start += 1
        
        return "" if min_window[1] == float(inf) else s[min_window[0]:min_window[1] + 1]