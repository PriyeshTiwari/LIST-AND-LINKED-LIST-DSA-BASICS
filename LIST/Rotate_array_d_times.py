class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self,A,D,N):
        D = D % N
        A[:] = A[D:] + A[:D]
        return A
        #Your code here
if __name__ == "__main__":
    A =  [1,2,3,4,5,6,7] 
    D = 3
    N = len(A)
    Sol = Solution()
    print(Sol.rotateArr(A,D,N))