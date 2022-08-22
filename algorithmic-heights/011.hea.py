# https://rosalind.info/problems/hea/
# Building a Heap

import sys
from utils import list_2_str


def load_data(filepath: str) -> (int, list):
    with open(filepath, 'r') as f:
        n_elems = int(f.readline().replace('\n', '').strip())
        elems = [int(item) for item in f.readline().replace('\n', '').strip().split()]
    return n_elems, elems


# Python3 implementation of Max Heap
# https://www.geeksforgeeks.org/max-heap-in-python
class MaxHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = sys.maxsize
        self.FRONT = 1

    # Function to return the position of
    # parent for the node currently
    # at pos
    @staticmethod
    def parent(pos):
        return pos // 2

    # Function to return the position of
    # the left child for the node currently
    # at pos
    @staticmethod
    def leftChild(pos):
        return 2 * pos

    # Function to return the position of
    # the right child for the node currently
    # at pos
    @staticmethod
    def rightChild(pos):
        return (2 * pos) + 1

    # Function that returns true if the passed
    # node is a leaf node
    def isLeaf(self, pos):
        if (self.size // 2) <= pos <= self.size:
            return True
        return False

    # Function to swap two nodes of the heap
    def __swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = (self.Heap[spos], self.Heap[fpos])

    # Function to heapify the node at pos
    def maxHeapify(self, pos):
        # If the node is a non-leaf node and smaller
        # than any of its child
        if not self.isLeaf(pos):
            if (self.Heap[pos] < self.Heap[self.leftChild(pos)] or
                    self.Heap[pos] < self.Heap[self.rightChild(pos)]):

                # Swap with the left child and heapify
                # the left child
                if (self.Heap[self.leftChild(pos)] >
                        self.Heap[self.rightChild(pos)]):
                    self.__swap(pos, self.leftChild(pos))
                    self.maxHeapify(self.leftChild(pos))

                # Swap with the right child and heapify
                # the right child
                else:
                    self.__swap(pos, self.rightChild(pos))
                    self.maxHeapify(self.rightChild(pos))

    # Function to insert a node into the heap
    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element

        current = self.size

        while (self.Heap[current] >
               self.Heap[self.parent(current)]):
            self.__swap(current, self.parent(current))
            current = self.parent(current)

    # Function to remove and return the maximum
    # element from the heap
    def extractMax(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.maxHeapify(self.FRONT)

        return popped


if __name__ == "__main__":
    inpath = "./datasets/011.hea.txt"
    outpath = "./datasets/011.hea.out"
    n, x = load_data(inpath)

    maxHeap = MaxHeap(n)
    for item in x:
        maxHeap.insert(item)
    outstr = list_2_str(maxHeap.Heap[1:])

    with open(outpath, 'w') as f:
        f.write(outstr + '\n')
    print(f"Save Results to {outpath}")
