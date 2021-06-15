from functional import MathClassRoom1 as Room1
import random


method_list_1 = [f for f in dir(Room1()) if callable(getattr(Room1(), f)) and not f.startswith('_')]


def get_statistics(room):
    
    print('='*20)
    correct = set(room.list_of_correct)
    wrong = set(room.list_of_wrong)
    
    print('correct')
    print('count of results: ', len(correct))
    print('-'*20)
    
    print('wrong')
    print('count of results: ', len(wrong))
    for i in wrong:
        print(i)
    print('-'*20)
     
    print('Count of operation: ', room.count_of_operation)
    print('='*20)


def all_combination(n=30):
    
    random.seed(42)
    
    room = Room1(n)
    
    for i in method_list_1:
        for j in range(n + 1):
            
            room.diff = j
            met = getattr(Room1, i)
            met(room)

    return room


def all_at_random(n=30):
    
    random.seed(42)
    
    room = Room1(n)
    
    for i in method_list_1:
        for _ in range(n + 1):
            
            room.diff = random.choice(range(n + 1))
            met = getattr(Room1, i)
            met(room)

    return room


def random_walk(n=30):
    
    room = Room1(n)

    for exp_r in range(n + 1):
        random.seed(exp_r)

        rand_list = []
        for i in range(10):
            rand_list.append(random.choice(method_list_1))

        for i in rand_list:
            room.diff = exp_r #FIXME: 
            met = getattr(Room1, i)
            met(room)
            
    return room
    

if __name__ == '__main__':
    
    print('All combination')
    room = all_combination()
    get_statistics(room)
    
    print('All at random')
    room = all_at_random()
    get_statistics(room)
    
    print('Random walk')
    room = random_walk()
    get_statistics(room)
