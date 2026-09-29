def using_control_once() -> str:
    if True:
        return "Success #1"


def using_control_again() -> str:
    if :
        return "Success #2"


print(using_control_once())
print(using_control_again())
