# def Count_greater(arr,x):
#     c = 0
#     for i in arr:
#         if (i > x):
#             c = c + 1
#     return c

# if __name__ == "__main__":
#     arr = [4, 5, 3, 1, 2]    
#     x = 3
#     print(Count_greater(arr,x))

class Solution:
    def greaterThanX(self,arr,n,x):
        c = 0
        for i in arr:
            if (i > x):
                c += 1
        return c
    
if __name__ == "__main__":
    sol = Solution()
    arr = [4, 5, 3, 1, 2]    
    x = 3
    print(sol.greaterThanX(arr,len(arr),x))