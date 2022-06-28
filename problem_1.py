import numpy as np

def is_multiple_of_3(i):
    return i % 3 == 0


def is_multiple_of_5(i):
    return i % 5 == 0


def get_multipliers(number):
    multiples = [] 
    
    for i in range(number):
        if is_multiple_of_3(i) or is_multiple_of_5(i):
            multiples.append(i)
    
    return sum(multiples)


if __name__ == "__main__":
    i = 1000
    print(get_multipliers(i))

