def getByIndex(arr,n,idx):
    if idx<0 or idx>=n:
        return -1
    else:
        return arr[idx] 
    
if __name__ == "__main__":
    n = 6
    arr = [1, 2, 3, 4, 5, 6]
    idx = 7
    print(getByIndex(arr,n,idx))