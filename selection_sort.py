import random
randomlist = []
for i in range(0,10):
    n = random.randint(1,30)
    randomlist.append(n)

def selection_sort(values):
    sorted_list = []
    for i in range(0, len(values)):
        index_to_move = index_of_min(values)
        sorted_list.append(values.pop(index_to_move))
    return sorted_list

def index_of_min(values):
    min_index = 0
    for i in range(1, len(values)):
        if values[i] < values[min_index]:
            min_index = i 
    return min_index

print(selection_sort(randomlist))


print("Hello daniel")

 
## works by switching the positions of the min value with the postiion 

def selectionSort(values):
    for i in range(values):
        minVal = min(values)