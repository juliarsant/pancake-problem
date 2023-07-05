# The Pancake Sorting Problem
The Pancake Problem is a mathematical sorting problem that ideally sorts a stack of different sized pancakes by flipping different points on the stack with a spatula. In this case, the pancake problem is solved with an A* sorting algorithm, and uniform-cost search. The A* sorting algorithm works better than the Uniform-Cost Search algorithm due to the heuristic function it uses to find goal states.

## Usage:
'''
python3 main.py [ astar | ucs ]
'''

## A* Search
A* Search algorithm uses a total cost that includes the calculation from a heuristic function and a backwards cost to choose the next node in the search. A min-heap Priority Queue was used to choose the node with the least total cost. The backwards cost was the number of flips taken, and the forward cost was a heuristic function that calculated the amount of gaps in the pancake stack. Gaps are the amount of adjacent pancakes that are more than one size greater than each other.

## Uniform-Cost Search Algorithm (UCS)
The UCS uses the same method of choosing a new node, however there is no heuristic function calculated. Therefore, A* performs better because this function moves the start state to the goal state faster and with a more optimal sequence.
