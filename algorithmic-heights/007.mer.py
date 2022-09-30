# https://rosalind.info/problems/mer/

# Merge Two Sorted Arrays

"""
Get two sorted array merged as one sorted array
"""


def load_data(filepath: str) -> (list, list):
    with open(filepath, 'r') as f:
        f.readline()  # skip first line
        x1 = [int(item) for item in f.readline().replace('\n', '').strip().split()]
        f.readline()  # skip third line
        x2 = [int(item) for item in f.readline().replace('\n', '').strip().split()]
    return x1, x2


# https://www.geeksforgeeks.org/merge-two-sorted-linked-lists/
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def show(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print('\n', end='')

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def to_list(self):
        if self.head is None:
            return None
        x = []
        last = self.head
        while last.next:
            x.append(last.data)
            last = last.next
        return x


def list_2_linked_list(x: list):
    linked_list = LinkedList()
    if x is None or len(x) == 0:
        print(f"Empty list!")
    else:
        for item in x:
            linked_list.add(item)
    return linked_list


def merge_lists(x1: list, x2: list):
    head_a, head_b = list_2_linked_list(x1).head, list_2_linked_list(x2).head
    dummy_node = Node(0)

    tail = dummy_node
    while True:
        if head_a is None:
            tail.next = head_b
            break
        if head_b is None:
            tail.next = head_a
            break

        if head_a.data <= head_b.data:
            tail.next = head_a
            head_a = head_a.next
        else:
            tail.next = head_b
            head_b = head_b.next

        tail = tail.next

    res = LinkedList()
    res.head = dummy_node.next

    return res.to_list()


if __name__ == '__main__':
    inpath = "./datasets/007.mer.in"
    outpath = "./datasets/007.mer.out"
    x1, x2 = load_data(inpath)
    result = merge_lists(x1, x2)
    with open(outpath, 'w') as f:
        f.write(' '.join([str(item) for item in result]) + 'n')
    print(f"Save Result to {outpath}")
