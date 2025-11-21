def sort_items_by_risk_level(arr):
    low = 0
    high = len(arr)-1
    mid = 0

    while mid<=high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]  # Swap arr[mid] with arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[high], arr[mid] = arr[mid], arr[high]  # Swap arr[mid] with arr[high]
            high -= 1
            # mid is not incremented here; the new arr[mid] needs checking
    return arr
# Example usage:
arr = [2, 7, 0, 1, 2, 1, 0, 0, 2, 1, 0, 2, 2, 2, 1]
sorted_arr = sort_items_by_risk_level(arr)
print("Sorted items by risk level:", sorted_arr)