#binarysearch
def BinSrchRecursive(a, i, l, x):
    if i > l:
        return 0
    mid = (i + l) // 2
    if x == a[mid]:
        return mid
    elif x < a[mid]:
        return BinSrchRecursive(a, i, mid - 1, x)
    else:
        return BinSrchRecursive(a, mid + 1, l, x)

def BinSrchIterative(a, n, x):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == x:
            return mid
        elif x < a[mid]:
            high = mid - 1       
        else:
            low = mid + 1    
    return 0

arr = list(map(int, input("Enter the elements of the array in non-decreasing order, separated by spaces: ").split()))
x = int(input("Enter the element to search for: "))
method = input("Choose the search method (iterative/recursive): ").strip().lower()

if method == "iterative":
    result = BinSrchIterative(arr, len(arr), x)
elif method == "recursive":
    result = BinSrchRecursive(arr, 0, len(arr) - 1, x)
else:
    print("Invalid choice. Please enter 'iterative' or 'recursive'.")
    result = None

if result is not None:
    if result != 0:
        print(f"Element {x} is present at index {result}.")
    else:
        print("Element not found in the array.")
