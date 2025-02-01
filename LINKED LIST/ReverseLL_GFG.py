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
    #Function to reverse a linked list.
    def reverseList(self, head):
        curr = head 
        prev = None
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr 
            curr = next
        return prev
if __name__ == "__main__": 
    llist = LinkedList()
    sol =  Solution()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append(5)
    llist.append(6)
    llist.Print()
    llist.head = sol.reverseList(llist.head)
    llist.Print()