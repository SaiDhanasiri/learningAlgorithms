

## Prefix Sums! O(n)
## (Leetcode: 303, 525, 560) 
def prefixSums(arr):

    new_arr = [0] * len(arr)

    for i, x in enumerate(arr):
        if i == 0: 
            new_arr[0] = arr[0]
        
        new_arr[i] = x + new_arr[i-1]

    return new_arr


## Two pointers! Checks to see if a stirng is palindrome: O(n)
## 167, 15, 11
def twoPointers(str):
    i = 0
    j = len(str) - 1

    while i < j: 
        if str[i] == str[j]:
            i +=1 
            j -= 1
        else:
            return False 
    return True


## Sliding Window! Given arr and k find the subarry of length k with maxsum:  O(n)
## 643, 3, 76

## doesn't work i give up 


def slidingWindow(arr, k):
    n = len(arr)

    currSum = sum(arr[:k])
    maxSum = currSum
    max_start_index = 0 

    for i in range(n - k):
        currSum = currSum - arr[i] + arr[i + k]
        
        if currSum > maxSum: 
            maxSum = currSum
            max_start_index = i + 1 
        
        return arr[max_start_index: max_start_index + k], maxSum
    


## Fast and slow pointers: 141, 202, 287 
## Helps to find patterns in a linked list (when the slow and the fast pointer meet), or 
## finding the middle node of a linked list. (the slow pointer should be at the middle when the fast poitner is at the end)
    
## no impl do leetcode for thsi pattern 
    


## Linked list in-place reversal pattern
## Leetcode: 24, 206, 92
    
def inPlaceReverse(head):
    prev = None
    current = head
    
    while current is not None: 
        next = current.next
        current.next = prev
        prev = current
        current = next
    
    return prev

## Monotonic Stack: Used a stack to find the next greater or next smaller element in an array
## Leetcode; 496, 739, 84
## Stack is first in, last out. 


def findnextMaxArr(arr):
    n = len(arr)
    stack = []
    result = [-1] * n

    for i in range(n): 
        while stack and arr[i] > arr[stack[-1]]:
            result[stack.pop()] = arr[i]

        stack.append(i)
    
    return result

## K-frequent elements
## Uses the idea of a min-heap to keep of the k largest
## top 3 largest elements -> min-heap 
## top 3 smalleset elements -> min-heap 
## also an algorithm called quick-select 

def findLargestElements(arr, k):
    ...


##merged intervals. A range of over-lapping or non-overlapping intervals
## Leetcode: 56, 57, 435


## modified binary search
## Leetcode: 33, 153, 240 

## binary tree traversal 
## in_order, preorder, post_order, level by level 
## to retrieve the values of a binary tree in a sorted order, use  inorder traversal 
## to create a copy of the tree(serealization) use pre_order
## when you want to traverse thorugh the child nodes before the parent, use postorder 
## when you want to explore all nodes at the current level before the next, use level by level 
## Leetcode: 257(preorder), 230(inorder), 124(postorder), 107(levelorder)


## DFS. Can be done recurisvely or iteratively. Done using a queue
### Leetcode: 133, 113, 210 
    

## BFS. Done using a queue and going through the neighbors and adding them to a queue 
### Leetcode: 102, 994, 127 


## Matrix Traversal: can use most of the graph algorithms 
### Leetcode: 733, 200, 130
    
## Backtracking: exploring all potential solution paths and backtracking to those who do not lead to a potential solution
### Leetcode: 46, 78, 51 

## DP: solving optimazition problems by breaking them down into smaller problems 
## Should know fib, 0-1 knapsack, longest common subsequence, longest increasing subsequence, subset sum, matrix chain multiplication
## Leetcode: 70, 322, 1143, 300, 416, 312




print(prefixSums([1,2,3,4,5,6,7]))
print(twoPointers("racecar"))
print(twoPointers("hello"))
print(slidingWindow([3,2,7,5,9,6,2], 3))


