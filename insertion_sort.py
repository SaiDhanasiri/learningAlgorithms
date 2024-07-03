import random


## this method does sorting by swapping values
def insertion_sort(values):
    ans = values
    for i in range(1, len(values)):
        j = i
        while j > 0 and ans[j - 1] > ans[j]:
            temp = ans[j]
            ans[j] = ans[j - 1]
            ans[j - 1] = temp
            j -= 1
    return ans

## this is for a 1-index array
## does insertion sort by remembering a key and placing it in the right order
def insertion_sort_new(values):
    for j in range(2, len(values) - 1):
        key = values[j]
        i = j - 1
        while i > 0 and values[i] > key:
            values[j + 1] > values[i]
            i -=1
        values[i + 1] = key
    
    return values

# same optimized algorithm for a zero index array

def insertion_sort_new_easy(values):
    for i in range(1, len(values)):
        key = values[i]
        j = i - 1 
        while j >= 0 and values[j] > key:
            values[j + 1] = values[j]
            j-=1
        values[j + 1] = key 

""" 
Key remembering method: 


algorithm would first remember the key element

7                   1 3 4 5 8 9 7
^                                        ^
key                                    j


then they would start shifting

7                   1 3 4 5 8 9 9
^                             ^
key                           i


7                   1 3 4 5 8 8 9
^                           ^
key                         i

7                   1 3 4 5 8 8 9
^                           ^
key                         i
A[i] is smaller than key, stop shifting

then it would put the key element back

7                   1 3 4 5 7 8 9
^                         ^
key                       i
conceptually, takes A[j] out, slide the elements over one at a time until they find a smaller element, 
and then put A[j] back in front of the first smaller element 
"""




""" 
Swapping method: 
1) Outer loop goes through all the elements starting at index 1 
2) inner loops also starts that index, and while it's greater than 0, it sees if the current element is smaller than the element before, 
and if it is then it swaps, and keeps on decreasing to see if it can until j reaches 0 or until the current element is greater than the element 
before

Time Complexity: 
Worst Case: O(n^2)
Best Case: O(n) // when the list is already sorted
 
Worst case comes from the fact that the sorting method employs 2 loops, one to go through all the elements and the other similar,
and in the worst case, the smallest element is at the end of the list and the while loops has to continue decreasing untill the smallest element 
at the beginning of the list resulting in a for loop going over once, and the while loop going back all the way.
 
 """

def main():
    randomlist = []
    for i in range(0,10):
        n = random.randint(1,30)
        randomlist.append(n)

    
    lis = [6, 1, 9, 21, 24, 6, 2, 6, 30, 5]
    
    ## test to see if it works: 
    print("original: ")
    print(lis)
    print("new: ")
    print(insertion_sort(lis))
    lis = [6, 1, 9, 21, 24, 6, 2, 6, 30, 5]
    print(lis)
    print("new2: ")
    print(insertion_sort_new(lis))

    
main()