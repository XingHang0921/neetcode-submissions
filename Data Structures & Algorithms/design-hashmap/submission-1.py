class Node:
    def __init__(self,key= -1,value= -1, next=None):
        self.val = value
        self.key = key
        self.next = next

class MyHashMap:

    def __init__(self):
        self.myHash = [Node() for i in range(1000)]

    def hash(self, key):
        return key % len(self.myHash)

    def put(self, key: int, value: int) -> None:
        cur = self.myHash[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = Node(key, value)
        
    def get(self, key: int) -> int:
        cur = self.myHash[self.hash(key)]
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        cur = self.myHash[self.hash(key)]
        while cur and cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)