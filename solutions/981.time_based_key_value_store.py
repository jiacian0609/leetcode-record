class TimeMap:

    def __init__(self):
        self.map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = {"times": [], "values": []}
        self.map[key]["times"].append(timestamp)
        self.map[key]["values"].append(value)
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        cur = self.map[key]
        times = cur["times"]
        values = cur["values"]

        left = 0
        right = len(times)

        while left <= right:
            mid = (left + right) // 2
            # print(times[mid], timestamp)
            if mid == 0 and times[mid] > timestamp:
                break

            if times[mid] == timestamp:
                # print(cur_dict[times[mid]])
                return values[mid]
            elif times[mid] < timestamp:
                if (mid + 1 >= len(times)
                    or (mid + 1 < len(times) and times[mid] < timestamp < times[mid + 1])):
                    # print(cur_dict[times[mid]])
                    return values[mid]
                
            if times[mid] < timestamp:
                left = mid + 1
            elif times[mid] > timestamp:
                right = mid - 1
        return ""

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)