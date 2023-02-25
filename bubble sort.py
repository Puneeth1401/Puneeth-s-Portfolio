def bubble_sort(numbers):
    n = len(numbers)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if numbers[j] > numbers[j+1] :
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

# Example usage
numbers = [5, 3, 9, 1, 7, 2, 6, 4, 8]
bubble_sort(numbers)
print("Sorted numbers in ascending order:", numbers)