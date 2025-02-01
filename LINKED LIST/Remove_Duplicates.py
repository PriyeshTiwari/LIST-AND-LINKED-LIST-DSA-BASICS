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
    def RemoveDuplicates(self,head):
        curr = head
        while curr != None and curr.next != None:
            if curr.data == curr.next.data:
                curr.next = curr.next.next
            else:
                curr = curr.next
if __name__ == "__main__": 
    llist = LinkedList()
    sol =  Solution()
    llist.append(10)
    llist.append(20)
    llist.append(20)
    llist.append(30)
    llist.append(30)
    llist.append(30)
    # llist.append(40)
    # llist.append(50)
    llist.Print()
    sol.RemoveDuplicates(llist.head)
    llist.Print()