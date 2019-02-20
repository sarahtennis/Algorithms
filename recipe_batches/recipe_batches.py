#!/usr/bin/python

'''
Input:  recipe, available ingredients (both dictionary, key=ingredient name, value=quantity)
Output: # of whole batches that can be made with available
'''

import math

# time complexity, O(n) where n = len(recipe)
def recipe_batches(recipe, ingredients):
  batches = float('inf')

  try:
    for key in recipe:
      if ingredients[key]:
        batches = min(batches, ingredients[key] // recipe[key])
    return int(batches)
  except:
    return 0



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 200, 'butter': 50, 'flour': 50 }
  print("{batches} batch(es) can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))