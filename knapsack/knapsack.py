#!/usr/bin/python

'''
maximizing the value of a set of items you select that are constrained by total size/weight
---INPUT---
first:  row number
second: weight/size of item (cost to place in knapsack)
third:  value of item (benefit of picking up, nothing to do with knapsack size)

---OUTPUT---
Items to select: 2, 8, 10
Total cost: 98
Total value: 117

1 42 81
2 42 42
3 68 56


'''

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
  pass
  

if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')