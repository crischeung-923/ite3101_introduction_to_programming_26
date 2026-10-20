from typing import List


def my_function(x: range) -> List[int]:
    result = []
    for i in range(3):
        result.append(x[i])
    return result


print(my_function(range(3)))
#   # Add your range between the parentheses!
