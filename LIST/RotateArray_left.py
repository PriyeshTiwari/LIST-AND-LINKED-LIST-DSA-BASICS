class Solution:
    # Function to rotate an array in left direction
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        def RotatePart(start,end):
            while (start < end):
                nums[start],nums[end] = nums[end],nums[start]
                start += 1
                end -= 1
        RotatePart(k,n-1)
        RotatePart(0,k-1)
        RotatePart(0,n-1)
        return nums
if __name__ == "__main__":
    A =  [1,2,3,4,5,6,7] 
    D = 3
    N = len(A)
    Sol = Solution()
    print(Sol.rotate(A,D))