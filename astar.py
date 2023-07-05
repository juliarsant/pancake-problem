"""
06/27/23

Implementation of an A* Algorithm to solve the pancake problem.
"""

import heapq as pq
import copy

"""
Implementation of the Node Class. Nodes are used to hold states, costs, 
parents and children of a particular state. 
"""
class Node():
    #Initialize
    def __init__(self, pancake_stack, parent, backward):
        self.stack = pancake_stack
        self.parent = parent
        self.children = []

        self.forward = self.gap_heuristic()
        self.backward = backward
        self.total = self.forward + self.backward

    #Less than operator
    def __lt__(self, other):
        return (self.total < other.total)
    
    #Equivalence operator
    def __eq__(self, other):
        return (self.total == other.total and self.stack == other.stack)

    #Heuristic function (Amount of Gaps)
    def gap_heuristic(self):
        gap = 0
        stack = self.stack

        for i in range(len(stack) - 1):
            if abs(stack[i] - stack[i+1]) > 1:
                gap += 1

        return gap

    #Total Cost
    def total_cost(self) -> int:
        return self.forward + self.backward

    #Bool: Did we reach a goal state?
    def goal_state(self) -> bool:
        stack = self.stack
        x = 0

        for i in range(len(stack) - 1):
            if stack[i] > stack[i+1]:
                x += 1

        if x == len(stack) - 1:
            return True
        
        return False
    

    #Flip the current pancake
    def flip(self, flip_idx):
        start_idx = flip_idx
        end_idx = len(self.stack) - 1
        stack = copy.deepcopy(self.stack)

        while start_idx < end_idx:
            temp = stack[start_idx]
            stack[start_idx] = stack[end_idx]
            stack[end_idx] = temp

            start_idx += 1
            end_idx -= 1

        return stack

    #Print the pancakes
    def print(self, done: bool):
        stack_print = copy.deepcopy(self.stack)
        stack_print.reverse()

        if done:
            print(f"Flip Number {self.backward}: ")

        for i in range(len(stack_print)):
            for _ in range(stack_print[i]):
                print("_", end = "")
            print(" ")


"""
Implementation of the PriorityQueue Class. PQs are used to create a 
queue in which the top of the heap is the node with the smallest cost. 
"""       
class PriorityQueue():
    
    #Initialize Queue and Queue Size
    def __init__(self):
        self.queue = []
        self.size = 0

    #Add to the frontier
    def push(self, node:Node):
        pq.heappush(self.queue, node)
        self.size += 1

    #Remove from the heap
    def remove(self) -> Node:
        priority_node = pq.heappop(self.queue)
        self.size -= 1
        
        return priority_node

    #Returns empty bool
    def isEmpty(self):
        return True if len(self.queue) == 0 else False
    
    #Prints nodes in the frontier
    def print_frontier(self):
        for i in range(len(self.queue)):
            print(self.queue[i].stack)
    
    #See if there is an identical child in the frontier
    def compare(self, child_tuple):
        for i in range(len(self.queue)):
            if self.queue[i].stack == child_tuple.stack and self.queue[i].total > child_tuple.total:
                del self.queue[i]
                return True
            

"""
Implementation of the A* Algorithm. It uses the total cost of the heuristic 
function and the forward cost to make a decision on the next node. 
"""
def astar(pancakes) -> bool:
    #Nodes that have been visited
    visited_nodes = []

    #Frontier implemented as a PQ
    frontier = PriorityQueue()

    #Root of the tree
    root = Node(pancakes, None, 0)

    #print first pancake
    print("Start: ")
    root.print(False)
    
    #Push Root to frontier
    frontier.push(root)

    while True:
        #If empty, return false
        if frontier.isEmpty():
            return False
        
        #Pop leaf based on cost and mark as visited
        root = frontier.remove()
        visited_nodes.append(root)

        #Did we reach a goal state?
        if root.goal_state():
            print_flips(root, root.backward, 0)
            return True
        
        #Add children of the current node to the children list of that node
        add_children(root)

        #For each child in this list:
        for child in root.children:
            if (child not in visited_nodes) and (child not in frontier.queue):
                frontier.push(child)
                
            elif child in frontier.queue:
                compare = frontier.compare(child) #Put lesser child
                if compare:
                    frontier.push(child)
    

def add_children(root: Node):
    for i in range(0, len(root.stack) - 1):
        #New flipped stack for new child node
        new_stack = root.flip(i)
        new_node = Node(new_stack, root, root.backward + 1) #Create node
        root.children.append(new_node) #Add to child list


def print_flips(root: Node, flips, flip_start):
    if flips == 0:
        return 0
    
    print_flips(root.parent, flips - 1, flip_start + 1)
    root.print(True)