numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def quicksort(array, left, right):
  pivot = None
  partionindex = None

  if left < right:
    pivot = right
    partionindex = partion(array, pivot, left, right)

    quicksort(array, left, partionindex - 1)
    quicksort(array, partionindex + 1, right)
    
  return array


def partion(array, pivot, left, right):
  pivotValue = array[pivot]
  partionindex = left

  for i in range(left, right):
    if array[i] < pivotValue:
      swap(array, i, partionindex)
      partionindex = partionindex + 1

  swap(array, right, partionindex)
  return partionindex

def swap(array, firstIndex, secondIndex):
    temp = array[firstIndex]
    array[firstIndex] = array[secondIndex]
    array[secondIndex] = temp

quicksort(numbers, 0, len(numbers) - 1)
print(numbers)