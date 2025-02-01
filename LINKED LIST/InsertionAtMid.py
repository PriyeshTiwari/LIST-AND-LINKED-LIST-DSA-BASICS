class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    def Print(self):
        curr = self.head
        while curr is not None:
            print(curr.data,end = "->")
            curr = curr.next
        print("None")
class Solution:
    def insertAtPosition(self,head,pos,data):
        new_node = Node(data)
        curr = head
        len = 0
        while curr != None:
            len = len + 1
            curr = curr.next
        if pos > len :
            return
        curr = head 
        for i in range (1,pos):
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node
        
if __name__ == "__main__": 
    llist = LinkedList()
    sol =  Solution()
    # llist.append(1)
    # llist.append(2)
    # llist.append(4)
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append(5)
    llist.append(6)
    llist.Print()
    sol.insertAtPosition(llist.head,3,4)
    llist.Print()
    