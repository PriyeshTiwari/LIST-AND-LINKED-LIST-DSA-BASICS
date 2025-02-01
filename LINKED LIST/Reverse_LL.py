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
    def ReverseLL(self,head):
        curr = head
        prev = None
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

        # if head == None:
        #     return head
        # if head.next == None:
        #     return head
        # rest_head = self.ReverseLL(head.next)
        # rest_tail = head.next
        # rest_tail.next = head
        # head.next = None
        # return rest_head

if __name__ == "__main__": 
    llist = LinkedList()
    sol =  Solution()
    llist.append(10)
    llist.append(20)
    llist.append(30)
    # llist.append(40)
    # llist.append(50)
    llist.Print()
    llist.head = sol.ReverseLL(llist.head)
    llist.Print()