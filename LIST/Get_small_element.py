def Get_small(arr,x):
    set=[]
    for i in arr:
        if (i < x):
            set.append(i)
    return set

if __name__ == "__main__":
    arr = [8,100,20,40,3,7]
    x = 10
    print(Get_small(arr,x))


