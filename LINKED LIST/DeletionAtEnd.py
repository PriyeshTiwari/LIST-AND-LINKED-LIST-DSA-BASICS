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
    def deleteTail(self,head):
        if head == None and head.next == None :
            return None
        curr = head 
        while curr.next.next != None:
            curr = curr.next
        curr.next = None
        return head
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
    llist.head = sol.deleteTail(llist.head)
    llist.Print()