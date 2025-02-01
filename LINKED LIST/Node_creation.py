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

    def InsertionAtBeg(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    def InsertionAtEnd(self,data):
        if self.head == None:
            return Node(data)
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = Node(data)

    def InsertionAtPos(self,data,pos):
        new_node = Node(data)
        if pos == 1:
            new_node.next = self.head
            return new_node
        curr = self.head
        for i in range (pos-2):
            curr = curr.next
            if curr == None:
                return self.head
        new_node.next = curr.next
        curr.next = new_node
        return self.head
    
    def DelAtBeg(self):
        if self.head == None:
            return None
        else:
            self.head = self.head.next
            return self.head
        
    def DelAtEnd(self):
        if self.head == None:
            return None
        if self.head.next == None:
            return None
        curr = self.head
        while curr.next.next != None:
            curr = curr.next
        curr.next = None
        return self.head
    
    def DelAtPos(self,data):
        curr = self.head
        while curr.next.data != data:
            curr = curr.next

        curr.next = curr.next.next
        return self.head
                
class Solution():
    def count(self,head):
        curr = head
        c = 0
        while curr is not None:
                c = c + 1
                curr = curr.next
        return c
    def Search(self,head,x):
        curr = head
        pos = 1
        while curr is not None:
            if curr.data == x :
                return pos
            pos = pos + 1
            curr = curr.next
        return -1
    
       
if __name__ == "__main__": 
    llist = LinkedList()
    sol =  Solution()
    llist.append(10)
    llist.append(20)
    llist.append(30)
    llist.append(40)
    llist.append(50)
    # llist.Print()
    # print(sol.count(llist.head))
    # print(sol.Search(llist.head,40))
    # llist.InsertionAtBeg(60)
    # llist.Print()
    llist.InsertionAtEnd(10)
    llist.Print()
    llist.InsertionAtPos(45,5)
    llist.Print()
    llist.DelAtBeg()
    llist.Print()
    llist.DelAtEnd()
    llist.Print()
    llist.DelAtPos(45)
    llist.Print()
