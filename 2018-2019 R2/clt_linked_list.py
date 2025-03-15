class Node():
    def __init__(self, val):
        self.value = val
        self.prev = None
        self.next = None

class LinkedList():
    def __init__(self, h, t):
        self.head = Node(h)
        self.tail = Node(t)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 2
    def pend(self, given, addon):
        addon = Node(addon)
        if self.head.value == given:
            addon.next = self.head
            self.head.prev = addon
            self.head = addon
        elif self.tail.value == given:
            addon.prev = self.tail
            self.tail.next = addon
            self.tail = addon
        self.length += 1
    def display(self):
        curr = self.head
        while curr.next != None:
            print(curr.value, end='-->')
            curr = curr.next

n = int(input())
cons = int(input())
linked_lists = []
for i in range(cons):
    n1, n2 = input().split()
    for j in range(len(linked_lists)):
        if n1 == linked_lists[j].head.value or n1 == linked_lists[j].tail.value:
            linked_lists[j].pend(n1, n2)
        if n2 == linked_lists[j].head.value or n2 == linked_lists[j].tail.value:
            linked_lists[j].pend(n2, n1)    
    linked_lists.append(LinkedList(n1, n2))

for i in range(len(linked_lists)):
    print(i)
    linked_lists[i].display()
