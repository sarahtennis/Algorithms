#!/usr/bin/python

import sys
from itertools import product

'''
all possible plays in game of "Rock Paper Scissors"
INPUT: n, number of plays per round
OUTPUT: list of all combinations as a list

NOTES: number of possible plays --> 3 ^ n
permutation with replacement

n = 2
['rock'] --> ['rock', 'rock'], ['rock', 'paper'], ['rock', 'scissors']
['paper']
['scissors']

'''


def rock_paper_scissors(n):
  # returns list of tuples instead of list of lists
  # return list(product(['rock', 'paper', 'scissors'], repeat = 2)
  
  options = [['rock'], ['paper'], ['scissors']]
  output = [[]]

  while n > 0:
    replace = []
    for current in output:
      for j in range(3):
        replace.append(current + options[j])

    n -= 1
    
    output = replace
  
  return output

    

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')