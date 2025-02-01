# METHOD 1 : SWAPPING CONCEPT

def Reverse(arr):
    s = 0
    e = len(arr)-1
    while s < e :
        arr[s],arr[e] = arr[e],arr[s]
        s = s + 1
        e = e - 1
    return(arr)

if __name__ == "__main__":
    arr =  [10,20,30,40,50] 
    print(Reverse(arr))

# METHOD 2 : USING LIBRARY
# arr =  [10,20,30,40,50]
# arr.reverse()
# print(arr)