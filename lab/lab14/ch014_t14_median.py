def median(numbers):
    s = sorted(numbers)
    n = len(s)
    if n % 2 == 1:
        return s[n // 2]
    else:
        mid1 = s[n // 2 - 1]
        mid2 = s[n // 2]
        return (mid1 + mid2) / 2.0