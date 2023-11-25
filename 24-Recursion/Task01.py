from typing import Optional, Union


def to_power(x: Optional[Union[int, float]], exp: int) -> Optional[Union[int, float]]:
    if exp < 0:
        raise ValueError("This function works only with exp > 0.")
    if exp == 0:
        return 1
    else:
        return x * to_power(x, exp - 1)


print(to_power(2, 3) == 8)
print(to_power(3.5, 2) == 12.25)
print(to_power(2, -1))
