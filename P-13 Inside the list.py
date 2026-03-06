# Write a function that takes an ordered list of numbers and another number. The function decides
# whether or not the given number is inside the list using binary search.

# Function to perform binary search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False


# Take input from user
numbers = list(map(int, input("Enter sorted numbers: ").split()))
search = int(input("Enter number to search: "))

# Call function
found = binary_search(numbers, search)

# Print result
if found:
    print("Number is present in the list.")
else:
    print("Number is NOT present in the list.")