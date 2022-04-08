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
        temp = merge(merge_sort(items[:midpoint]), merge_sort(items[midpoint:]), [])

    for i in range(len(temp)):
        items[i] = temp[i]
    return items

def partition(items, low, high):
    """
    Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.

    For simplicity, I have chosen the pivot point to be the last number within 
    the input array.

    TODO: Running time: ??? Why and under what conditions?

    The runtime is O(n) because we will always need to iterate through the entire 
    array and individually compare each and every number within the array to the 
    pivot point to determine if swapping is necessary.

    TODO: Memory usage: ??? Why and under what conditions?

    The memory usage is O(1) because all of the swapping being done is done in 
    place so no copy of the input array is ever made and the memory usage stays 
    the same no matter the size of the input array.
    """
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p
    pointer = low #the pointer is a number larger than the pivot
    
    for i in range(low, high): #iterate through array from specified low to high index
        if items[i] <= items[high]: #compare each number against the pivot (last number)
            items[i], items[pointer] = items[pointer], items[i] #if number is smaller than pivot, move it to the left of pointer
            pointer += 1
    
    #swap pivot with pointer so all numbers less than pivot are to the left and all numbers larger are to the right
    items[high], items[pointer] = items[pointer], items[high] 
    return pointer 


def quick_sort(items, low=None, high=None):
    """
    Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.

    TODO: Best case running time: ??? Why and under what conditions?

    The best case time complexity is O(nlogn). This occurs when the partitions 
    being passed into the function recursively are evenly balanced and thus, 
    the amount of operations being done every time is halved.

    TODO: Worst case running time: ??? Why and under what conditions?

    The worst case time complexity is O(n^2). This occurs when the partitions 
    being passed into the function recursively are not even balanced which causes 
    the algorithm to need to be run n*n number of times.

    TODO: Memory usage: ??? Why and under what conditions?

    The memory usage is O(logn) where the memory being used is by the call stack 
    each time quick sort is called.
    """
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort
    if low == None:
        low = 0
    if high == None:
        high = len(items) - 1

    if low < high:
        pivotIndex = partition(items, low, high)

        quick_sort(items, low, pivotIndex - 1)
        quick_sort(items, pivotIndex + 1, high)

def partition2(items):
    low_array, high_array, pivot = [], [], items.pop(0)
    [low_array.append(item) if item < pivot else high_array.append(item) for item in items]
    return pivot, low_array, high_array

def quick_sort2(items):
    if len(items) <= 1: return items
    partition = partition2(items)
    return quick_sort2(partition[1]) + [partition[0]] + quick_sort2(partition[2])

arr = [42,65,27,50,96,11,83]
print(quick_sort2(arr))