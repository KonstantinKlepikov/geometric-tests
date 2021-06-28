class MathClassRoom:
    
    def __init__(self, num_of_items=30, heap1=1, heap2=0, coef=0):
        self.result_heaps = [num_of_items,]
        self.num_of_heaps = len(self.result_heaps)
        self.heap1 = heap1
        self.heap2 = heap2
        self.coef = coef
        
    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.result_heaps!r}, {self.num_of_heaps!r}, {self.heap1!r}, {self.heap2!r}')
        
    def add_(self):
        
        self.result_heap[self.heap1] += self.coef
        self.result_heap[self.heap2] -= self.coef

    def sub_(self):
        self.result_heap[self.heap1] -= self.coef
        self.result_heap.append(self.coef)

    def mul_(self):
        
        diff = self.result_heap[self.heap1] * self.coef - self.result_heap[self.heap1]
        self.result_heap[self.heap1] *= self.coef
        self.result_heap[self.heap2] -= diff

    def div_(self):
        
        self.result_heap[self.heap1] /= self.coef
        for _ in range(self.coef - 1):
            self.result_heap.append(self.result_heap[self.heap1])

    def pow_(self):
        diff = self.result_heap[self.heap1] ** self.coef - self.result_heap[self.heap1]
        self.result_heap[self.heap1] **= self.coef
        self.result_heap[self.heap2] -= diff

    def sqrt_(self):
        
        self.result_heap.append(self.result_heap[self.heap1] - self.result_heap[self.heap1] ** self.coef)
        self.result_heap[self.heap1] **= self.coef
    