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
    def maximum(self,head):
        max = head
        curr = head
        while curr != None:
            if max.data <= curr.data:
                max = curr
            curr = curr.next
        return max.data
    def minimum(self,head):
        min = head
        curr = head
        while curr != None:
            if min.data >= curr.data:
                min = curr
            curr = curr.next
        return min.data   
if __name__ == "__main__": 
    llist = LinkedList()
    sol =  Solution()
    llist.append(2)
    llist.append(4)
    llist.append(6)
    llist.append(7)
    llist.append(5)
    llist.append(1)
    llist.append(0)
    # llist.append()
    # llist.append(40)
    # llist.append(50)
    llist.Print()
    min = sol.minimum(llist.head)
    max = sol.maximum(llist.head)
    print(max,min)