class Node:
    def __init__(self, key: int = None, value: int = None):
        self.key, self.value = key, value
        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map key to node

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
    
    # remove node from list
    def remove(self, node: Node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        node.prev = node.next = None

    # remove node at right
    def insert(self, node: Node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        node.prev, node.next = prev, nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            # TODO: update most recent
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1                        

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return

        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.insert(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.insert(node)

            if len(self.cache) > self.cap:
                # remove from the list and delete the LRU from nthe hashmap
                lru = self.left.next
                self.remove(lru)
                del self.cache[lru.key]
                    


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)