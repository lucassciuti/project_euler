def is_multiple_of_3(i):
    return i % 3 == 0


def is_multiple_of_5(i):
    return i % 5 == 0


def get_multipliers(m, n, number):
    multiples = [] 
    
    for i in range(number):
        if i % m == 0 or i % n == 0:
            multiples.append(i)
    
    return sum(multiples)


if __name__ == "__main__":
    m = 3
    n = 5
    number = 1000
    print(get_multipliers(m, n, number))

