def count(sequence:list, item)->int:
    total = 0
    for x in sequence:
        if x == item:
            total += 1
    return total
