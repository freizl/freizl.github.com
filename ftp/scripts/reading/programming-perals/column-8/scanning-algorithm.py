#!/usr/bin/python

""" Algorithm pseudocode
max_so_far = 0
max_ending_here = 0

for i in [0, n):
  max_ending_here = max(max_ending_here + x[i], 0)
  max_so_far = max(max_so_far, max_ending_here)
"""

def max_sum(x_vector):
  max_so_far = 0
  max_ending_here = 0
  for i in range(0, len(x_vector)):
    max_ending_here = max(max_ending_here + x_vector[i], 0)
    max_so_far = max(max_so_far, max_ending_here)
  return max_so_far

### Max sum close to given value
### TODO, set close_value to sorted_csum[0] before sort.
def max_close_sum(x_vector, close_value=0):
  csum = [0]
  for i in range(len(x_vector)):
    csum.append(csum[i] + x_vector[i])

  sorted_csum = sorted(csum)
  min_distance = min([sorted_csum[i]-sorted_csum[i-1] for i in range(1,len(sorted_csum))])
  return csum

if __name__ == '__main__':
  test_vector = (31, -41, 59, 26, -53, 58, 97, -93, -23, 84)
#  assertEquals result is 187
#  print max_sum(test_vector)
  print max_close_sum((5,4,-8,6))
  print max_close_sum(test_vector)
