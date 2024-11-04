import sys

class max_heap:
    def __init__(self, sizeLimit):
        self.sizeLimit = sizeLimit
        self.curr_size = 0
        self.Heap = [0] * (self.sizeLimit+1)
        self.Heap[0] = sys.maxsize
        self.root = 1

    def swapNodes(self, node1, node2):
        self.Heap[node1], self.Heap[node2] = self.Heap[node2], self.Heap[node1]

    def max_heapify(self, i):
        # If the node is a not a leaf node and is lesser than any of its child
        if not(i >=(self.curr_size//2) and i<= self.curr_size):
            if self.Heap[2*i] > self.Heap[(2*i) + 1]:
                self.swapNodes(i, 2*i)
                self.max_heapify(2*i)
            else:
                self.swapNodes(i, (2*i)+1)
                self.max_heapify((2*i)+1)

    def heappush(self, element):
        print(f"Pushing {element}" )
        if self.curr_size >= self.sizeLimit:
            return
        self.curr_size+=1
        self.Heap[self.curr_size] = element
        current = self.curr_size
        while self.Heap[current] > self.Heap[current // 2]:
            self.swapNodes(current, current//2)
            current = current//2
        self.print_heap()


    def heappop(self):
        last = self.Heap[self.root]
        self.Heap[self.root] = self.Heap[self.curr_size]
        self.curr_size -=1
        self.max_heapify(self.root)
        return last

    def build_heap(self):
        for i in range(self.curr_size // 2, 0, -1):
            self.max_heapify(i)

    # helper function to print the heap
    def print_heap(self):
        for i in range(1, (self.curr_size // 2) + 1):
            print(
                "Parent Node is " + str(self.Heap[i]) +
                " Left Child is " + str(
                self.Heap[2 * i]) +
                " Right Child is " + str(self.Heap[2 * i + 1])
            )


maxHeap = max_heap(10)
maxHeap.heappush(15)
maxHeap.heappush(7)
maxHeap.heappush(9)
maxHeap.heappush(4)
maxHeap.heappush(8)
print(maxHeap.heappop())