def Get_small_ListComprehension(arr,x):
    set = [set for set in arr if set < x]
    return set

if __name__ == "__main__":
    arr = [8,100,20,40,3,7]
    x = 10
    print(Get_small_ListComprehension(arr,x))