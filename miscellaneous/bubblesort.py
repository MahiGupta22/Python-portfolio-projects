def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    for i in range(n):
        # Flag to check if any swaps happened
        swapped = False
        for j in range(0, n - i - 1):
            # Increment comparison count
            comparisons += 1
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True
        # If no swaps occurred, the list is sorted
        if not swapped:
            break
    return arr, comparisons, swaps

# Example usage:
if __name__ == "__main__":
    # Take input from the user
    user_input = input("Enter the elements of the array separated by spaces: ")
    arr = list(map(int, user_input.split()))
    
    print("Unsorted array:", arr)
    sorted_arr, comparisons, swaps = bubble_sort(arr)
    print("Sorted array:", sorted_arr)
    print("Total comparisons:", comparisons)
    print("Total swaps:", swaps)


