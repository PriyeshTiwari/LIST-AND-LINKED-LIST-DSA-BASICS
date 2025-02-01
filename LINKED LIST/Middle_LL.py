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
    def Middle(self,head):
        if head == None:
            return
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow.data
        # if head.next == None:
        #     return head
        # curr = head
        # count = 0
        # while curr != None:
        #     curr = curr.next
        #     count += 1
        # curr = head
        # for i in range(count//2):
        #     curr = curr.next
        # return curr.data
if __name__ == "__main__": 
    llist = LinkedList()
    sol =  Solution()
    llist.append(10)
    llist.append(5)
    llist.append(20)
    llist.append(15)
    llist.append(25)
    llist.append(30)
    llist.Print()
    print(sol.Middle(llist.head))