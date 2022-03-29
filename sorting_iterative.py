#!python


def is_sorted(items):
  """
  Return a boolean indicating whether given items are in sorted order.

  TODO: Running time: ??? Why and under what conditions?

  The runtime is o(n) in the worst case where the out of order number is 
  at the end of the array because you have to scan through the entire 
  array once to check every number.

  TODO: Memory usage: ??? Why and under what conditions?

  The memory usage is o(1) because you are only comparing one number to 
  another. You are not storing anything in any new array as you iterate 
  through and do the comparisons.
  """

  # TODO: Check that all adjacent items are in order, return early if so
  for i in range(len(items) - 1):
    if items[i + 1] < items[i]:
      return False
  
  return True


def bubble_sort(items):
  """
  Sort given items by swapping adjacent items that are out of order, and
  repeating until all items are in sorted order.

  TODO: Running time: ??? Why and under what conditions?

  The runtime is o(n^2) because for each number, the entire array needs 
  to be iterated through in order to perform the comparison and possible 
  left right swap. 

  TODO: Memory usage: ??? Why and under what conditions?

  The memory usage is o(1) because all you are doing is comparing the current 
  number to the next number. This requires the same amount of space no matter 
  how large or small the input array is.
  """
  # TODO: Repeat until all items are in sorted order
  # TODO: Swap adjacent items that are out of order

  for i in range(len(items) - 1):
    for j in range(len(items) - 1):
      if items[j + 1] < items[j]:
        items[j], items[j + 1] = items[j + 1], items[j]
  
  return items


def selection_sort(items):
  """
  Sort given items by finding minimum item, swapping it with first
  unsorted item, and repeating until all items are in sorted order.

  TODO: Running time: ??? Why and under what conditions?

  The runetime is o(n^2) because for each number in the array, we 
  need to scan through the entire array and search for a number 
  that is smaller than the current number. This requires a nested 
  for loop which makes the runtime exponential.

  TODO: Memory usage: ??? Why and under what conditions?

  The memory usage is o(1) because the amount of space we are using 
  is constant no matter the length of the array. All we are doing is 
  comparing two numbers and swapping if necessary. This will always 
  use the same amount of space no matter the size of the array.
  """
  # TODO: Repeat until all items are in sorted order
  # TODO: Find minimum item in unsorted items
  # TODO: Swap it with first unsorted item

  for i in range(len(items)):
    curr_min = i

    for j in range(i, len(items)):
      if items[j] < items[curr_min]:
        curr_min = j
    
    if items[curr_min] < items[i]:
      items[i], items[curr_min] = items[curr_min], items[i]
  
  return items


def insertion_sort(items):
  """
  Sort given items by taking first unsorted item, inserting it in sorted
  order in front of items, and repeating until all items are in order.

  TODO: Running time: ??? Why and under what conditions?

  The runtime is o(n^2) in the worst case because for each number in the 
  array, we need to move it backwards through the array one index at a 
  time. In the worst case, every number needs to be moved back through 
  the entire array up until the current index which results in an 
  exponential runtime.

  TODO: Memory usage: ??? Why and under what conditions?

  The memory usage is o(1) because no matter the size of the array, we 
  are always doing the same comparisons and not storing any extra 
  information into other variables.
  """
  # TODO: Repeat until all items are in sorted order
  # TODO: Take first unsorted item
  # TODO: Insert it in sorted order in front of items
  
  for i in range(1, len(items)):
    j = i

    while items[j] < items[j-1] and j > 0:
      items[j], items[j-1] = items[j-1], items[j]
      j -= 1

  return items

test_array = [1,4,3,6,7]
test_array2 = [1,3,5,7,8,9]
test_array3 = [64, 34, 25, 12, 22, 11, 90]
test_array4 = [2,8,5,3,9,4,1]
# print(is_sorted(test_array))
# print(is_sorted(test_array2))

# print(bubble_sort(test_array4))
# print(insertion_sort(test_array4))