def count(sequence, item):
    total = 0
    for x in sequence:
        if x == item:
            total += 1
    return total
