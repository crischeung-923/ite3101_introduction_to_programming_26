def remove_duplicates(items):
    result = []
    for x in items:
        if x not in result:
            result.append(x)
    return result