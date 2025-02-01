# class Solution:
#     def immediateSmaller(self,arr,n,x):
#         min_diff = -1
#         for i in range(n):
#             if ((x - arr[i]) > min_diff):
#                 min_diff = arr[i]
#             else:
#                 min_diff = -1

#         return min_diff

class Solution:
    def immediateSmaller(self, arr, n, x):
        min_diff = -1
        for i in range(n):
            if arr[i] < x:
                if (min_diff == -1) or (x - arr[i] < x - min_diff):
                    min_diff = arr[i]
        return min_diff
if __name__ == "__main__":
    sol = Solution()
    arr = [4,67]
    # arr = [4,67,13,12,15]
    x = 16
    n = len(arr)
    F = sol.immediateSmaller(arr,n,x)
    print(F)
    
       
        