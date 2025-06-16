# def insertion_sort(arr):
#     l=len(arr)
#     for i in range(1,l):
#         for pos in range(i,0,-1):
#             if arr[pos-1]>arr[pos]:
#                 arr[pos],arr[pos-1]=arr[pos-1],arr[pos]
#             else:
#                 break
#     return arr

## We have to shift these cards and insert it once.

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         current = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] > current:
#             arr[j + 1] = arr[j]  
#             j -= 1
#         arr[j + 1] = current  
#     return arr


def insertion_sort(arr):
    n=len(arr)
    for current in range(1,n):
        current_card=arr[current]
        current_pos=current-1
        while current_pos>=0:
            if (arr[current_pos]<current_card):
                break
            else:
                arr[current_pos+1]=arr[current_pos]
                current_pos-=1
        arr[current_pos + 1] = current_card
    return arr



ary = [12, 25, 11, 34, 90, 22]
sorted_arr = insertion_sort(ary)
print("Sorted array:", sorted_arr)

