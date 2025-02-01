class Solution:
    def isSorted(self,arr,n):
        
        n = len(arr)
    
        if n <= 1:
            return 1
    
        increasing = 1
        decreasing = 1
    
        for i in range(1, n):
            if arr[i] < arr[i - 1]:
                increasing = 0
            if arr[i] > arr[i - 1]:
                decreasing = 0
    
        return increasing or decreasing
        # if n < 2:
        #     return 1
    
        # else:
        #     i = 1
        #     while i < n:
        #         if arr[i] >= arr[i-1]:
        #             f = 1
        #         else:
        #             f = 0
        #             break
        #         i = i + 1
        # if (f == 1):
        #     return 1
        # else:
        #     return 0
            
if __name__ == "__main__":
    sol = Solution()
    arr =  [3,2,1]  
    n = 5
    print(sol.isSorted(arr,n))