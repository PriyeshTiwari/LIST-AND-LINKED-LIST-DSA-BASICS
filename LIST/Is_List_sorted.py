def Is_Sorted(arr):
    # if len(arr) < 2:
    #     return "Yes"
    
    # else:
    #     for i in range(len(arr)):
    #         for j in range(i+1,len(arr)):
    #             if arr[i] <= arr[j]:
    #                 f = 1
    #             else:
    #                 f = 0
    #                 break
    #     if (f == 1):
    #         return "Yes"
    #     else:
    #         return "NO"
    if len(arr) < 2:
        return "Yes"
    
    else:
        i = 1
        while i < len(arr):
            if arr[i] >= arr[i-1]:
                f = 1
            else:
                f = 0
                break
            i = i + 1
    if (f == 1):
        return "Yes"
    else:
        return "NO"
if __name__ == "__main__":
    arr = [10,2]
    # arr = [15]
    ar = [10,2,3]
    ar.sort()
    print(Is_Sorted(arr))
    print(ar)



   
