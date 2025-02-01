class Solution:  
    def majorityWins(self, arr, n, x, y):
        nox = 0
        noy = 0
        for i in arr:
            if i == x:
                nox += 1
            elif i == y:
                noy +=1
        if (nox == noy):
            major = x if x < y else y
        else:
            major = x if nox > noy else noy

        return major

if __name__ == "__main__":
    sol = Solution()
    # N = 11
    # arr = [1,1,2,2,3,3,4,4,4,4,5]
    # x = 4 
    # y = 5
    # N = 8
    # arr = [1,2,3,4,5,6,7,8]
    # x = 1
    # y = 7
    N = 8
    arr = [5,22,29,12,32,69,1,75]
    x = 29
    y = 96
    F = sol.majorityWins(arr,N,x,y)
    print(F)
        
    
