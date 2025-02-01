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
    def NthFromEnd(self,head,n):
        # len = 0
        # curr = head
        # while curr != None:
        #     len += 1
        #     curr = curr.next
        # if len < n:
        #     return ""
        # curr = head
        # for i in range (1,len-n+1):
        #     curr = curr.next
        # return curr.data
        if head == None:
            return " "
        first = head
        for i in range(n):
            if first == None:
                return " "
            first = first.next
        second = head
        while first != None:
            second = second.next
            first = first.next
        return second.data
if __name__ == "__main__": 
    llist = LinkedList()
    sol =  Solution()
    llist.append(10)
    # llist.append(20)
    # llist.append(30)
    # llist.append(40)
    # llist.append(50)
    llist.Print()
    print(sol.NthFromEnd(llist.head,1))