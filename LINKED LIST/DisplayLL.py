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
    def displayList(self,head):
        res = []
        curr = head
        while curr is not None:
            res.append(curr.data)
            curr = curr.next
        return res

if __name__ == "__main__": 
    llist = LinkedList()
    sol =  Solution()
    llist.append(5)
    llist.append(5)
    llist.append(6)
    llist.append(7)
    llist.append(2)
    # llist.append()
    # llist.append(40)
    # llist.append(50)
    llist.Print()
    print(sol.displayList(llist.head))