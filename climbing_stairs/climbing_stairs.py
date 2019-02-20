#!/usr/bin/python

'''
REQUIREMENT:
- counts the number of possible ways in which the child can ascend the staircase (1, 2, or 3 steps)

HINTS:
- a bunch of possible permutations, use recursion
- base cases (climb 0 stairs? negative number of stairs?)
- how recursively call such that we move towards one or more of these base cases?
- caching/memoization might be one avenue

EXAMPLES:
climbing_stairs(0) --> 1
climbing_stairs(1) --> 1
climbing_stairs(2) --> 2
climbing_stairs(3) --> 4 = climb(0) + climb(1) + climb(2)
climbing_stairs(4) --> 7 = climb(1) + climb(2) + climb(3)
climbing_stairs(5) --> 13
climbing_stairs(10) --> 274

NOTES:
Number of solutions to x + 2y + 3x = n where all are positive integers (including 0)
Sum of previous 3 climbs
'''

import sys

def climbing_stairs(n, cache=None):
  # invalid stairs
  if n < 0:
    return 0

  # base cases
  if n == 0:
    if cache:
      cache[n] = 1
    return 1
  if n == 1:
    if cache:
      cache[n] = 1
    return 1
  if n == 2:
    if cache:
      cache[n] = 2
    return 2

  # return if received cache argument
  if cache:
    if cache[n]:
      return cache[n]
  
    val = climbing_stairs(n - 3, cache) + climbing_stairs(n - 2, cache) + climbing_stairs(n - 1, cache)
    cache[n] = val

    return val
  # return if no cache argument
  else:
    return climbing_stairs(n - 3) + climbing_stairs(n - 2) + climbing_stairs(n - 1)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')