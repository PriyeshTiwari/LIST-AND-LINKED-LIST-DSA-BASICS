def Largest_element(arr):
    max = arr[0]
    for i in arr:
        if i >= max:
            max = i
    return max
if __name__ == "__main__":
    arr = [15,10,20,8,12]
    print(Largest_element(arr))