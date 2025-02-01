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
    def isSorted(self,head):
        if head == None or head.next == None:
            return 1
        curr = head 
        inc = dec = True
        while curr.next != None:
            if curr.data > curr.next.data:
                dec = False
            if curr.data < curr.next.data:
                inc = False
            curr = curr.next
        return 1 if inc or dec else 0
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
    print(sol.isSorted(llist.head))
 