def Average(arr):
    l=len(arr)
    s=0
    for i in range(l):
        s=s+arr[i]
    av=s/l
    print(av)
if __name__ == "__main__":
    arr=[30,60,40]
    Average(arr)
