def product(numbers:list)->int:
    result = 1
    for n in numbers:
        result *= n
    return result