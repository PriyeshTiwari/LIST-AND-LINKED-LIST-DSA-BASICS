# METHOD - 1 : NAIVE APPROACH

# def Remove_Duplicates(arr,n):
#     arr.sort()
#     temp = [0] * n
#     temp[0] = arr[0]
#     res = 1
#     for i in range(1,n):
#         if temp[res-1] != arr[i]:
#             temp[res] = arr[i]
#             res = res + 1
#     for i in range(0,res):
#         arr[i] = temp[i]
#     return arr[:res] , res
    
# if __name__ == "__main__":
#     arr = [10,20,30,30,30]
#     print(Remove_Duplicates(arr,len(arr)))


# METHOD - 2 : OPTIMIZED TECHNIQUE

def Remove_Duplicates(arr,n):
    arr.sort()
    res = 1
    for i in range(1,n):
        if arr[res-1] != arr[i]:
            arr[res] = arr[i]
            res = res + 1
    return arr[:res] , res
    
if __name__ == "__main__":
    arr = [40,20,30,30,30]
    print(Remove_Duplicates(arr,len(arr)))