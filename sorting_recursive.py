#!python


def merge(items1, items2, new_array = []):
    """
    Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.

    TODO: Running time: ??? Why and under what conditions?

    The runtime is O(n+m) with n being the first array and m being the second 
    array. This can be simplified to O(n) overall. The runtime will always be 
    linear with respect to the length of array 1 and arry 2 combined.

    TODO: Memory usage: ??? Why and under what conditions?

    The memory usage is O(n+m) with n and m being the length of array 1 and 
    array 2. Each time we recursively call the function, we pass in the entire 
    first and second array with modifications so the memory usage is the size 
    of the input arrays.  
    """
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list

    if not items1 and not items2:
        return new_array

    if not items1:
        new_array += items2
        return merge([], [], new_array)
    if not items2:
        new_array += items1
        return merge([], [], new_array)
    
    if items1[0] > items2[0]:
        new_array.append(items2.pop(0))
        return merge(items1, items2, new_array)
    else:
        new_array.append(items1.pop(0))
        return merge(items1, items2, new_array)

def merge_sort(items):
    """
    Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.

    TODO: Running time: ??? Why and under what conditions?

    The runtime is O(nlogn). The process of dividing the array in half at every 
    step is a logn operation, and the process of merging all the subarrays back 
    into a single array is an O(n) operation which makes this a O(nlogn) 
    operation overall.

    TODO: Memory usage: ??? Why and under what conditions?

    The memory usage is O(n). The total memory usage is equal to the size of 
    the input array and never differs no matter the conditions of the input.
    """
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order
    if len(items) == 1:
        return items
    else:
        midpoint = len(items) // 2
        return merge(merge_sort(items[:midpoint]), merge_sort(items[midpoint:]), [])

def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort

# arr1 = [1,3,5,6]
# arr2 = [2,3,4,7,8]
arr3 = [4,67,2,4,6,8,4,2,56,8,534,5,45]
print(arr3)
merge_sort(arr3)
print(arr3)