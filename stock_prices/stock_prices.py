#!/usr/bin/python

# buying and selling Amazon stock

import argparse

'''
Write a function `find_max_profit` that receives as input a list of stock prices.
Your function should return the maximum profit that can be made from a single buy and sell.
You must buy first before selling; no shorting is allowed here.

HINT: For this problem, we essentially want to find the difference between the smallest and 
largest prices in the list of prices.

EXAMPLE: Input: [1050, 270, 1540, 3800, 2]) --> Output: 3530
'''
def find_max_profit(prices):
  # set checkvalue at index i,  find max(self - arr[i + 1]) for all i range(0, len - 1)

  # initialize profit to have something to compare against
  profit = float("-inf")

  # run of for loops is n!/(2 * (n-2)!) = 2 * n * (n - 1) = O(n^2)
  for i in range(0, len(prices) - 1):
    for j in range(i + 1, len(prices)):
      if -(prices[i] - prices[j]) > profit:
        profit = -(prices[i] - prices[j])
  
  return profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))