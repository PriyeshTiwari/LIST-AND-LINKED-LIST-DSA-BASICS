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
    def areIdentical(self,head1, head2):
        curr1 = head1 
        curr2 = head2
        while curr1 != None and curr2 != None:
            if curr1.data != curr2.data:
                return False
            curr1 = curr1.next
            curr2 = curr2.next
        return True if (curr1 == None and curr2 == None) else False
if __name__ == "__main__": 
    llist1 = LinkedList()
    llist2 = LinkedList()
    sol =  Solution()
    llist1.append(1)
    llist1.append(2)
    llist1.append(3)
    llist1.append(4)
    llist1.append(5)
    # llist2.append(1)
    # llist2.append(2)
    # llist2.append(3)
    # llist2.append(4)
    # llist2.append(5)
    llist2.append(99)
    llist2.append(59)
    llist2.append(42)
    llist2.append(20)
    llist1.Print()
    llist2.Print()
    print(sol.areIdentical(llist1.head,llist2.head))