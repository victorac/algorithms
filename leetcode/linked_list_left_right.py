class Node:
    va: int
    prev: "Node"
    next: "Node"

    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:
    '''Doubly linked list with left and right pointers'''
    left: Node
    right: Node

    def __init__(self):
        self.left = Node(0)
        self.right = Node(0)
        self.left.next = self.right
        self.right.prev = self.left

    def __str__(self) -> str:
        array = []
        current = self.left.next
        while current is not None:
            array.append(current.val)
            current = current.next
        array.pop()
        return f'{array}'

    def get(self, index: int) -> int:
        current = self.left.next
        while current is not None and index > 0:
            current = current.next
            index += -1
        return current.val if (current is not None) and (index == 0) else -1

    def addNode(self, val: int, prev: Node, next: Node):
        new_node = Node(val)
        prev.next = new_node
        next.prev = new_node
        new_node.prev = prev
        new_node.next = next

    def addAtHead(self, val: int):
        self.addNode(val, self.left, self.left.next)

    def addAtTail(self, val: int):
        self.addNode(val, self.right.prev, self.right)

    def addAtIndex(self, index: int, val: int):
        current = self.left.next
        while current is not None and index > 0:
            current = current.next
            index += -1
        if current is not None and index == 0:
            self.addNode(val, current.prev, current)

    def deleteAtIndex(self, index:int):
        current = self.left.next
        while current is not None and index > 0:
            current = current.next
            index += -1
        if current is not None and index == 0:
            prev = current.prev
            next = current.next
            prev.next = next
            next.prev = prev

if __name__ == "__main__":
    ll = MyLinkedList()
    ll.addAtIndex(0, 1)
    ll.addAtIndex(0, 2)
    ll.addAtIndex(0, 3)
    ll.addAtTail(4)
    ll.addAtHead(9)
    ll.addAtIndex(1, 12)
    ll.addAtIndex(5, 13)
    ll.addAtIndex(7, 16)
    ll.addAtIndex(9, 17) # should not add
    print(ll)
    ll.deleteAtIndex(7) # deletes last node
    print(ll)
    ll.addAtTail(45)
    print(ll)
    ll.deleteAtIndex(0)
    ll.addAtHead(123)
    print(ll)