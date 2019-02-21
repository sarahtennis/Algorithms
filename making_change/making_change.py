#!/usr/bin/python

import sys

'''
how many ways to make change money using only pennies, nickels, dimes, quarters, and half-dollars. 
INPUT: an amount of money in cents, list of coin denominations
OUTPUT: total number of ways to make change

NOTES:
x + 5y + 10z + 25a + 50b = amount
return size of solution set for a given amount

maximum number of coins for amount is amount (all pennies)

10: 10p --> 5p + 1n --> 1n + 1n --> 1d (4 ways)
20: 20 p --> 15p + 1n --> 10p + 2n --> 5p + 3n --> 4n --> 10p + 1d --> 5p + 1n + 1d --> 2n + 1d --> 2d 

1-4:    1
5:      2
6-9:    2
10:     4
11-14:  4
15:     6
16-19:  6
20:     9
21-24:  9
25:     13
26-29:  13
30:     18
31-34:  18
35:     24
'''

def making_change(amount, denominations = [5, 10, 25, 50]):
  # force at least one solution with pennies (handled if no penny in argument)

  # store how to make previous change, all guaranteed 1 way with pennies
  cache = [1] * (amount + 1)

  # remove 1 from denominations (already handled)
  denominations = list(filter(lambda x: x != 1, denominations))

  # loop through each coin
  for i, coin in enumerate(denominations):
    # only increases at new "coin level"
    for j in range(coin, len(cache)):
      cache[j] = cache[j] + cache[j-coin]

  return cache.pop()



if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")