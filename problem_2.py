def get_even_fib(threshold):
    fib = [1, 2]
    evens = [2]
    while fib[-1] < threshold:
        new = fib[-1] + fib[-2]
        fib.append(fib[-1] + fib[-2])
        if new % 2 == 0:
            evens.append(new)
    print(sum(evens))


if __name__ == "__main__":
    get_even_fib(4000000)

