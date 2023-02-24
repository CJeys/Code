# input = [2,3,5,6,8,4,1]
# Expected result = [6, 8]

def top_two(input_list):
  sortedList = sorted(input_list)
  largest_int = int(sortedList[-1])
  second_int = int(sortedList[-2])
  a = second_int, largest_int
  return a
top_two([2,3,5,6,8,4,1])