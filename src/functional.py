import random
random.seed(42)


def get_rnd(*args):
    return random.randint(args[0], args[1])


def add(num1, num2):
    try:
        return num1 + num2
    except Exception as e:
        return str(e)


def sub(num1, num2):
    try:
        return num1 - num2
    except Exception as e:
        return str(e)


def mul(num1, num2):
    try:
        return num1 * num2
    except Exception as e:
        return str(e)


def div(num1, num2):
    try:
        return int(round(num1 / num2))
    except Exception as e:
        return str(e)


def pow2(num1, num2):
    try:
        return num1 ** 2
    except Exception as e:
        return str(e)


def sqrt(num1, num2):
    try:
        return int(round(num1 ** 0.5))
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    
    for exp_r in range(5):
        random.seed(exp_r)
    
        func_list = [add, sub, mul, div, pow2, sqrt]
        rand_list = []
        for _ in range(100):
            rand_list.append(random.choice(func_list))

        num1 = get_rnd(-10, 10)
        for i in rand_list:
            num2 = get_rnd(-10, 10)
            print('input: ', num1, num2)
            num1 = i(num1, num2)
            print('function', i.__name__)
            if isinstance(num1, str):
                print(num1)
                break
            print('-' * 10)
