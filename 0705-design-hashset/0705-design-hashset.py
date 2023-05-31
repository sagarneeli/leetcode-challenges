class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyHashSet:

    def __init__(self):
        self.set = [ListNode(0) for i in range(10 ** 4)]

    def add(self, key: int) -> None:
        index = key % len(self.set)
        cur = self.set[index]
        
        while cur.next:
            if key == cur.next.val:
                return
            cur = cur.next
        
        cur.next = ListNode(key)
        return

    def remove(self, key: int) -> None:
        index = key % len(self.set)
        cur = self.set[index]
        
        while cur.next:
            if key == cur.next.val:
                cur.next = cur.next.next
                return
            
            cur = cur.next

    def contains(self, key: int) -> bool:
        index = key % len(self.set)
        cur = self.set[index]
        
        while cur.next:
            if key == cur.next.val:
                return True
            cur = cur.next
        
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)