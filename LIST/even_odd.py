def Even_Odd(arr):
    n=len(arr)
    e = []
    o = []

    for i in range(n):
        if arr[i]%2==0:
              e.append(arr[i])
        else:
             o.append(arr[i])
    print("Even: ",e,end = " ")
    # for i in range(len(e)):
    #      print(e[i],end=" ")
    print("\n")
    print("odd: ",o,end=" ")
    # for i in range(len(o)):
    #     print(o[i],end=" ")
if __name__ == "__main__":
    arr = [10,41,30,15,50]
    Even_Odd(arr)
   