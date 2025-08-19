class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key: value

        self.oldest = Node(-1, -1)
        self.latest = Node(-1, -1)
        self.oldest.next = self.latest
        self.latest.prev = self.oldest

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            to_remove = self.oldest.next
            self.remove(to_remove)
            del self.cache[to_remove.key]

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
    
    def insert(self, node):  # insert before latest
        prev, next = self.latest.prev, self.latest
        prev.next = node
        node.prev = prev
        node.next = self.latest
        next.prev = node

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)