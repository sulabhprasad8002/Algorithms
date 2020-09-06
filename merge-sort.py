import math

nums = [1, 9, 3, 5, 8, 0]

def mergesort(nums):
  if len(nums) == 1:
    return nums

  length = len(nums)
  middle = math.floor(length/2)
  left = nums[0 : middle]
  right = nums[middle: length]

  return merge(mergesort(left), mergesort(right))

def merge(left, right):
  result = []
  leftindex = 0
  rightindex = 0

  while leftindex < len(left) and rightindex < len(right):
    if left[leftindex] < right[rightindex]:
      result.append(left[leftindex])
      leftindex = leftindex + 1
    else:
      result.append(right[rightindex])
      rightindex = rightindex + 1
    
  result.extend(left[leftindex:])
  result.extend(right[rightindex:])

  return result


print(mergesort(nums))