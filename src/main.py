from functional import MathClassRoom as Room
import random


methods_list = [f for f in dir(Room()) if callable(getattr(Room(), f)) and not f.startswith('_')]


def all_combination(n=30):
    
    random.seed(42)
    correct_lean = set()
    correct_heap = set()
    wrong = set()
        
   
    for i in methods_list:
        for _ in range(n + 1):
            
            room = Room(num_of_items=n)
            room.heap1 = '# ???' # FIXME: no solution
            
            room.diff = random.choice(range(n + 1))
            met = getattr(Room, i)
            try:
                met(room)
                for k in room.result_heaps:
                    correct_heap.add(k)
                correct_lean.add(room.num_of_heaps)
            except Exception as e:
                wrong.add(str(e))

    return room



if __name__ == '__main__':
    
    print('All combination')
    # room = all_combination()
    print('\n')
    
    room = Room(num_of_items=30, heap1=3, heap2=27, coef=1)
    print(room)
    
