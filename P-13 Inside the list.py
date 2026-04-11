# Write a function that takes an ordered list of numbers and another number. The function decides
# whether or not the given number is inside the list using binary search.

def binary_search(list,item):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low + high)//2
        mid_value = list[mid]

        if mid_value < item :
            low = mid + 1 
                              
        elif mid_value > item :
            high = mid - 1

        else:
            return True

    return False

a = list(map(int ,input("Enter sorted numbers: ").split()))
b = int(input("Enter number to search: "))

found = binary_search(a,b)

if found:
    print("Number is present in the list.")
else:
    print("Number is NOT present in the list.")
