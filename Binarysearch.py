def binary_search(arr, x):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] < x:
            left = mid + 1

        else:
            right = mid - 1

    return -1

my_list = [1,2,3,4,5,6,7,8,9,10,12,14,17,19,45,55.34,27,36]
search_value = int(input("Enter the number you want to search: "))

result = binary_search(my_list, search_value)

if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")