"""
06/27/23

Implementation of an A* Algorithm or Uniform-Cost Search Algoritm 
to solve the pancake problem.
"""

import random
import astar
import ucs
import sys

#Create pancakes
pancakes = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(pancakes)

print(pancakes)
done = False

if sys.argv[1] == "astar":
    astar.astar(pancakes)
    done = True
elif sys.argv[1] == "ucs":
    ucs.ucs(pancakes)
    done = True
else:
    print("Usage: python3 main.py [ astar|ucs ]")


