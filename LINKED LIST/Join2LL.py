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
    def joinTheLists(self,head1, head2):
        curr1 = head1
        curr2 = head2
        while curr1.next != None:
            curr1 = curr1.next
        curr1.next = curr2
        return head1
if __name__ == "__main__": 
    llist1 = LinkedList()
    llist2 = LinkedList()
    sol =  Solution()
    # llist1.append(1)
    # llist1.append(2)
    # llist1.append(9)
    # llist1.append(6)
    # llist1.append(5)
    # llist1.append(7)
    # llist1.Print()
    # llist2.append(99)
    # llist2.append(8)
    # llist2.append(4)
    # llist2.Print()
    llist1.append(5)
    llist1.Print()
    llist2.append(1)
    llist2.append(2)
    llist2.Print()
    llist1.head = sol.joinTheLists(llist1.head,llist2.head)
    llist1.Print()
    