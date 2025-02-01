class Solution:
    def immediateGreater(self,arr,n,x):
        min_diff = -1
        for i in arr:
            if i > x:
                if (min_diff == -1) or (x - i > x - min_diff):
                    min_diff = i
        return min_diff
if __name__ == "__main__":
    sol = Solution()
    # arr = [4,67]
    # arr = [4,67,13,12,15]
    arr = [1,2,3,4,5]
    x = 1
    n = len(arr)
    F = sol.immediateGreater(arr,n,x)
    print(F)       