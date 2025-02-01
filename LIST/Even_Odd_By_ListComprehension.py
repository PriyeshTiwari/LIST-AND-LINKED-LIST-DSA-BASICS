def Even_Odd(arr):
    n=len(arr)
    e = [e for e in arr if e % 2 == 0]
    o = [o for o in arr if o % 2 != 0]
    print("Even: ",e,end = "\n")
    print("odd: ",o,end=" ")

if __name__ == "__main__":
    arr = [10,41,30,15,50]
    Even_Odd(arr)