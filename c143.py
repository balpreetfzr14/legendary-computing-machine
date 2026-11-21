def binary_search(arr, target):
    low , high = 0 ,len(arr) - 1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid - 1
    return -1
numbers = [1,2,4,5,7,9,11,12,15,17,23]
print(binary_search(numbers,15 ))
print(binary_search(numbers, 5))
