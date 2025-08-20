class RecentCounter:

    def __init__(self):
        self.current = []
        

    def ping(self, t: int) -> int:
        temp = self.current
        self.current = []
        for time in temp:
            if time >= t - 3000:
                self.current.append(time)
        self.current.append(t)
        return len(self.current)



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)