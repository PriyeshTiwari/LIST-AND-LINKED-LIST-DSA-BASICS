def Count_small(arr,x):
    c = 0
    for i in arr:
        if (i < x):
            c = c + 1
    return c

if __name__ == "__main__":
    arr = [8,100,20,40,3,7]
    x = 10
    print(Count_small(arr,x))