
from .plus import multi


def calk(a: int, b: int) -> int:
    multi('=', 10)
    if a==0 or b==0:
        return 'ZeroDivisionError'
    elif type(a)==str or type(b)==str:
        return 'TypeError'
    else:
        c = a / b
        return int(c)


if __name__ == "__main__":
    print(calk(2, 2))
