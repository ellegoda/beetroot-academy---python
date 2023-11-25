def mult(a: int, n: int) -> int:
    if a < 0 or n < 0:
        ValueError("This function works only with positive integers")
    else:
        if n == 0:
            return 0
        else:
            return a + mult(a, n - 1)


print(mult(2, 4) == 8)
print(mult(2, 0) == 0)
