def Rotate_By_One(arr,n):
    x = arr[0]
    for i in range(1,n):
        arr[i-1] = arr[i]
    arr[n-1] = x
    return arr

if __name__ == "__main__":
    arr =  [50,10,20,30,40] 
    print(Rotate_By_One(arr,len(arr)))