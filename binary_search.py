def binary_search(list,target,low=None,high=None):
    if low is None :
        low = 0
    if high is None :
        high = len(list)-1
    if high < low :
        return -1

    mid_point =(low + high)// 2
    if list[mid_point] == target:
        return mid_point
    elif target < list[mid_point]:
        return binary_search(list,target,low,mid_point-1)
    else:
        return binary_search(list,target,mid_point+1,high)

list = [1,3,5,6,8,9,12,20]
target = 8
print(binary_search(list,target))