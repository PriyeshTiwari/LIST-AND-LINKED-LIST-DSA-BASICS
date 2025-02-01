
# METHOD - 1 : 2 TRAVERSAL

# def Sec_Largest_element(arr):
#     if len(arr) < 2:
#         return None
#     max = arr[0]
#     sec_max = None
#     for i in arr:
#         if i >= max:
#             max = i
#     for i in arr:
#         if i != max:
#             if sec_max is None or i > sec_max:
#                 sec_max = i         
#     return max,sec_max

# METHOD - 2 : 1 TRAVERSAL
def Sec_Largest_element(arr):
    if len(arr) < 2:
        return None 
    max = arr[0]
    sec_max = None
    for i in arr[1:]:
        if i > max:
            sec_max = max
            max = i
        elif i != max:
            if sec_max == None or sec_max < i:
                sec_max = i
    return sec_max   
if __name__ == "__main__":
    arr = [15,10,18,20,8,12]
    # arr = [15]

    print(Sec_Largest_element(arr))