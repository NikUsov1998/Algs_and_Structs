class BinaryHeap:
    def __init__(self):
        self.elements=[]
        self.size=0

    def shift_up(self, i) -> None:
        while i>0:
            j=(i-1)//2
            if self.elements[i] < self.elements[j]:
                self.elements[i], self.elements[j] = self.elements[j], self.elements[i]
            else:
                break
            i=j

    def shift_down(self, i) -> None:
        n = len(self.elements)
        while True:
            left_j = 2*i+1
            right_j = 2*i+2
            smaller=i
            if left_j <= n - 1 and self.elements[left_j] < self.elements[smaller]:
                smaller = left_j
            if right_j <= n - 1 and self.elements[right_j] < self.elements[smaller]:
                smaller = right_j
            if smaller != i:
                self.elements[i], self.elements[smaller] = self.elements[smaller], self.elements[i]
                i = smaller
            else:
                break

    def add(self, element) -> None:
        self.elements.append(element)
        i = len(self.elements) - 1
        self.shift_up(i)
        self.size+=1

    def extract(self):
        if len(self.elements)==0:
            return None
        if len(self.elements)==1:
            self.size-=1
            return self.elements.pop()
        result=self.elements[0]
        self.elements[0]=self.elements.pop()
        self.shift_down(0)
        self.size-=1
        return result

    def insert_and_extract(self, element):
        if len(self.elements)==0:
            self.elements.append(element)
            self.size+=1
            return None
        result = self.elements[0]
        self.elements[0]=element
        self.shift_down(0)
        return result

    def get_root_element(self):
        if len(self.elements)==0:
            return None
        return self.elements[0]

    def clear(self):
        self.elements=[]
        self.size=0

def merge_list(list1: list, list2: list) -> list[int]:
    result = []
    i = 0
    j = 0
    while True:
        if i >= len(list1) and j >= len(list2):
            break
        if i < len(list1) and j < len(list2):
            if list1[i] < list2[i]:
                result.append(list1[i])
                i+=1
            else:
                result.append(list2[j])
                j+=1
        elif i < len(list1):
            result.append(list1[i])
            i+=1
        else:
            result.append(list2[j])
            j+=1
    return result

def tournament_sort(seq):
    MAX_HEAP_SIZE = 7
    heap = BinaryHeap()
    winners = []
    losers = []
    for element in seq:
        if heap.size <= MAX_HEAP_SIZE:
            heap.add(element)
        else:
            if element < heap.get_root_element():
                losers.append(element)
            else:
                winners.append(heap.insert_and_extract(element))

    while heap.size > 0:
        winners.append(heap.extract())
    if len(losers) == 0:
        seq[:] = winners
        return seq
    losers = tournament_sort(losers)
    seq[:] = merge_list(losers, winners)
    return seq
