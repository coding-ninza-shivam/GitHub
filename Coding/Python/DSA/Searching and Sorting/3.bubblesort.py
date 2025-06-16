def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1): 
            if arr[j] > arr[j + 1]:
                # swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n - 1):
#         j = 0  # use a variable instead of range
#         while j < n - i - 1:
#             if arr[j] > arr[j + 1]:
#                 # swap
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#             j += 1
#     return arr

unsorted_list = [12, 25, 11, 34, 90]
sorted_list = bubble_sort(unsorted_list)
print("Sorted list:", sorted_list)