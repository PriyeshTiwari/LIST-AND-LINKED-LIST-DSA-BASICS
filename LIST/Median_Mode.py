import math
class Solution:
    ##Complete the below codes
    #Function to find median of the array elements.
    def median(self,A,N):
        A.sort()
        n=len(A)
        if n%2==0:
            middle1=A[n//2-1]
            middle2=A[n//2]
            median=math.floor((middle1+middle2)/2)
        else:
            median=A[n//2]
        return int(median)
        
        ##Your code here
        #If median is fraction then convert the median to integer and return
     
    #Function to find mean of the array elements.   
    def mean(self,A,N):
        return int(sum(A)/len(A))
        ##Your code here


if __name__ == "__main__":
    sol = Solution()
    arr = [10,20,30,40,60]
    F = sol.mean(arr,len(arr))
    G = sol.median(arr,len(arr))
    print(F)
    print(G)