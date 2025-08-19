class UF:
    def __init__(self, N):
        # 初始化，每個節點的父節點先指向自己
        self.parents = list(range(N))

    def union(self, child, parent):
        # 把 child 所屬集合的 root，連到 parent 的 root
        self.parents[self.find(child)] = self.find(parent)

    def find(self, x):
        # 找到 x 所屬集合的 root，並做 path compression
        if x != self.parents[x]:
            # 壓縮路徑：讓 x 直接連到 root，加速後續查找
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UF(len(accounts))  # 每個帳號是一個節點

        owner = {}  # 記錄每個 email 對應到哪個帳號 index
        for idx, (name, *emails) in enumerate(accounts):
            for e in emails:
                if e in owner:
                    # 如果這個 email 已經出現過，代表兩個帳號應該屬於同一個人
                    # 把目前帳號 idx 和之前出現的帳號 owner[e] 合併
                    uf.union(idx, owner[e])
                # 更新 email 的擁有者為當前帳號
                owner[e] = idx
        
        # 建立新的集合：root_index -> emails
        new_accounts = defaultdict(list)
        for e, o in owner.items():
            # 找到 email 所屬帳號的 root，把 email 放進該集合
            new_accounts[uf.find(o)].append(e)
        
        # 輸出格式：[name] + [sorted emails]
        return [[accounts[i][0]] + sorted(new_accounts[i]) for i in new_accounts.keys()]