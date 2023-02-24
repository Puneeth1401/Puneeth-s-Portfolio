def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1


my_list = [1,10,11,15,9,7,5,3,8,4,2,19,20,21,22,12,13,14]
target = int(input("Enter a number between 1 to 25 to find its position in my list"))
index = linear_search(my_list, target)
position= index+1
if index != -1:
    print(f"{target} found at index {index}")
else:
    print(f"{target} not found in list")

print(f"The position of the number you entered is {position}")

