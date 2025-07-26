def MaxMinRecursive(arr, i, j, max_min):
    if i == j:
        max_min[0] = max_min[1] = arr[i]
    elif i == j - 1:
        if arr[i] < arr[j]:
            max_min[0], max_min[1] = arr[j], arr[i]
        else:
            max_min[0], max_min[1] = arr[i], arr[j]
    else:
        mid = (i + j) // 2
        max_min_left = [float('-inf'), float('inf')]
        max_min_right = [float('-inf'), float('inf')]
        MaxMinRecursive(arr, i, mid, max_min_left)
        MaxMinRecursive(arr, mid + 1, j, max_min_right)
        max_min[0] = max(max_min_left[0], max_min_right[0])
        max_min[1] = min(max_min_left[1], max_min_right[1])

def MaxMinIterative(arr):
    max_val = min_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
        if arr[i] < min_val:
            min_val = arr[i]
    
    return max_val, min_val

arr = list(map(int, input("Enter the elements of the array, separated by spaces: ").split()))
method = input("Choose the method (iterative/recursive): ").strip().lower()
if method == "iterative":
    max_val, min_val = MaxMinIterative(arr)
elif method == "recursive":
    max_min = [float('-inf'), float('inf')]
    MaxMinRecursive(arr, 0, len(arr) - 1, max_min)
    max_val, min_val = max_min[0], max_min[1]
else:
    print("Invalid choice. Please enter 'iterative' or 'recursive'.")
    max_val, min_val = None, None
if max_val is not None and min_val is not None:
    print(f"Maximum element: {max_val}")
    print(f"Minimum element: {min_val}")
