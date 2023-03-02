class Node:
    val: int
    next: "Node"

    def __init__(self, val=None, next=None):
        # type: (int, Node) -> None
        self.val = val
        self.next = next


class MyLinkedList:
    head: Node
    tail: Node
    last_index: int

    def __init__(self):
        self.head = None
        self.tail = None
        self.last_index = -1

    def length(self):
        return self.last_index + 1

    def toArray(self) -> list:
        res = []
        sentinel = self.head
        for _ in range(self.length()):
            res.append(sentinel.val)
            sentinel = sentinel.next
        return res

    def __str__(self) -> str:
        array = self.toArray()
        return f"{array}"

    def getNodeAtIndex(self, index: int):
        if index < 0:
            return
        if index > self.last_index:
            return
        sentinel = self.head
        for _ in range(index):
            sentinel = sentinel.next
        return sentinel

    def get(self, index: int):
        if index < 0:
            return -1
        if index > self.last_index:
            return -1
        node = self.getNodeAtIndex(index)
        return node.val if node is not None else -1

    def addAtHead(self, val: int):
        new_node = Node(val=val, next=self.head)
        self.head = new_node
        if self.length() == 0:
            self.tail = self.head
        self.last_index += 1

    def addAtTail(self, val: int):
        new_node = Node(val=val)
        if self.length() == 0:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.last_index += 1

    def addAtIndex(self, index: int, val: int):
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.length():
            self.addAtTail(val)
            return
        if index > self.length():
            return
        prev_node = self.getNodeAtIndex(index - 1)
        new_node = Node(val=val, next=prev_node.next)
        prev_node.next = new_node
        self.last_index += 1

    def deleteAtIndex(self, index: int):
        if self.length() == 0:
            return
        if index < 0 or index > self.last_index:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif index == 0:
            self.head = self.head.next
        else:
            prev_node: Node = self.getNodeAtIndex(index - 1)
            target_node: Node = prev_node.next
            prev_node.next = target_node.next
            if self.tail == target_node:
                self.tail = prev_node
        self.last_index += -1


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
    print(ll.head)
    ll.addAtHead(123)
    print(ll)
