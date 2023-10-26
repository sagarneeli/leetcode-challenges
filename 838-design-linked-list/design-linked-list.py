class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head      

    def get(self, index: int) -> int:
        curr = self.head.next
        while curr and index > 0:
            index -= 1
            curr = curr.next   
        if curr and curr != self.tail and index == 0:
            return curr.val
        return -1 

    def addAtHead(self, val: int) -> None:
        new_node, prev_node, next_node = ListNode(val), self.head, self.head.next
        new_node.prev, new_node.next = prev_node, next_node
        next_node.prev = new_node
        prev_node.next = new_node

    def addAtTail(self, val: int) -> None:
        new_node, prev_node, next_node = ListNode(val), self.tail.prev, self.tail
        new_node.prev = prev_node
        new_node.next = next_node
        next_node.prev = new_node
        prev_node.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and index == 0:
            new_node, prev_node = ListNode(val), curr.prev
            new_node.prev = prev_node
            new_node.next = curr
            curr.prev = new_node
            prev_node.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        node = self.head.next
        while node and index > 0:
            node = node.next
            index -= 1
        
        if node and node != self.tail and index == 0:
            node.prev.next = node.next
            node.next.prev = node.prev

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)