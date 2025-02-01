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
    def insertAtEnd(self,head,x):
        new_node = Node(x)
        curr = head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node
        return head
if __name__ == "__main__": 
    llist = LinkedList()
    sol =  Solution()
    llist.Print()
    sol.insertAtEnd(llist.head,6)
    llist.Print()