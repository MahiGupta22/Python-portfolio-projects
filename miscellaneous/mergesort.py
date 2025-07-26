def merge(arr, low, mid, high):
    b = [0] * len(arr)
    h = low
    i = low
    j = mid + 1
    while h <= mid and j <= high:
        if arr[h] <= arr[j]:
            b[i] = arr[h]
            h += 1
        else:
            b[i] = arr[j]
            j += 1
        i += 1
    while h <= mid:
        b[i] = arr[h]
        h += 1
        i += 1
    while j <= high:
        b[i] = arr[j]
        j += 1
        i += 1
    for k in range(low, high + 1):
        arr[k] = b[k]

def iterative_merge_sort(arr):
    n = len(arr)
    curr_size = 1
    while curr_size < n:
        low = 0
        while low < n - 1:
            mid = min(low + curr_size - 1, n - 1)
            high = min(low + 2 * curr_size - 1, n - 1)
            merge(arr, low, mid, high)
            low += 2 * curr_size
        curr_size *= 2

    return arr

def recursive_merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        recursive_merge_sort(arr, low, mid)
        recursive_merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)

arr = list(map(int, input("Enter the elements of the array, separated by spaces: ").split()))
method = input("Choose the method (iterative/recursive): ").strip().lower()
if method == "iterative":
    sorted_arr = iterative_merge_sort(arr)
elif method == "recursive":
    recursive_merge_sort(arr, 0, len(arr) - 1)
    sorted_arr = arr
else:
    print("Invalid choice. Please enter 'iterative' or 'recursive'.")
    sorted_arr = None
if sorted_arr is not None:
    print(f"Sorted array: {' '.join(map(str, sorted_arr))}")
