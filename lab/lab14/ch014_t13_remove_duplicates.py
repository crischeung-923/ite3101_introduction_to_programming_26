def remove_duplicates(items:list)->list:
    result = []
    for x in items:
        if x not in result:
            result.append(x)
    return result