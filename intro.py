import math


def linear_search(list, target):
    """
    Returns the index of the position, none if nun found 
    """
    for x in range(0, len(list)):
        if list[x] == target: 
            return x
        
	
    return None
	
def binary_search(list, target):
    ## FOR BINARY SEARCH TO WORK PROPERLY MAKE SURE THE LIST IS SORTED!
    first = 0
    last = len(list) - 1
    while first <= last:
        midpoint = (first + last) // 2
        if list[midpoint] == target: 
            return midpoint 
        elif list[midpoint] < target: 
            first = midpoint + 1
        else:
            last = midpoint - 1 
    return None
        
	
	
def main(): 
	print(linear_search([1,2,3,4,5], 3))
	print(binary_search([1,2,3,4,5], 3))
    
