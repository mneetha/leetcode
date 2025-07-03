#Build Min heap (heapify) T=O(n), S=O(1)

A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]

import heapq
heapq.heapify(A)
print(A)

#Heap push (insert element) T=O(log n)
heapq.heappush(A, 4)
print(A)

# heap pop extract min T=O(log n)
minn = heapq.heappop(A)
print(A, minn)

#heap sort
#t=O(nlog n), S= O(n)
#O(1) is possible via swapping but this is complex
def heapsort(arr):
    heapq.heapify(arr)
    n=len(arr)
    new_list = [0]* n
    for i in range(n):
        minn = heapq.heappop(arr)
        new_list[i] = minn

    return  new_list

print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))

#heap push pop: T=O(log n)
heapq.heappushpop(A, 99)
print(A)

#peak at min T=O(1)
A[0]

#max heap
B = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
n = len(B)

for i in range(n):
    B[i]=-B[i]

heapq.heapify(B)
print(B)
print('largest', -heapq.heappop(B))

heapq.heappush(B, -7)

print(B)

#build heap from scratch T=O(nlog n)
C = [-5, 4, 2, 1, 7, 0, 3]
heap = []

for x in C:
    heapq.heappush(heap, x)
    print(heap, len(heap)) #check size of heap

# putting tuples of items on the heap

D=[5,4,3,5,4,3,5,5,4]
from collections import Counter
counter = Counter(D)
print(counter)

heap = []
for k,v in counter.items():
    heapq.heappush(heap, (v,k))

print(heap)