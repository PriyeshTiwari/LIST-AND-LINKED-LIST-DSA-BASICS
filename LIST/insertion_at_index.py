class Solution:
    '''You need to insert the given element at the given index. 
    After inserting the elements at index, elements
    from index onward should be shifted one position ahead
     You may assume that the array already has sizeOfArray - 1
    elements.'''
    
    def insertAtIndex(self, arr, sizeOfArray, index, element):
        arr.insert(index,element)
        return





if __name__ == "__main__":
    sol = Solution()
    F = sol.factorial(4)
    print(F)