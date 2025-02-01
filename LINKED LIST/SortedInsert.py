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
class Solution():
    def SortedInsert(self,head,data):
        new_node = Node(data)
        if head == None or head.data >= data:
            new_node.next = head
            return new_node
        curr = head
        while curr.next != None and curr.next.data < data:
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node
        return head
if __name__ == "__main__": 
    llist = LinkedList()
    sol =  Solution()
    llist.append(10)
    llist.append(20)
    # llist.append(30)
    # llist.append(40)
    # llist.append(50)
    llist.Print()
    sol.SortedInsert(llist.head,25)
    llist.Print()