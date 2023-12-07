def fibonacci_search(arr, x):
    fib_m_minus_2 = 0
    fib_m_minus_1 = 1
    fib_m = fib_m_minus_1 + fib_m_minus_2

    while fib_m < len(arr):
        fib_m_minus_2 = fib_m_minus_1
        fib_m_minus_1 = fib_m
        fib_m = fib_m_minus_1 + fib_m_minus_2

    offset = -1

    while fib_m > 1:
        i = min(offset + fib_m_minus_2, len(arr) - 1)

        if arr[i] < x:
            fib_m = fib_m_minus_1
            fib_m_minus_1 = fib_m_minus_2
            fib_m_minus_2 = fib_m - fib_m_minus_1
            offset = i

        elif arr[i] > x:
            fib_m = fib_m_minus_2
            fib_m_minus_1 = fib_m_minus_1 - fib_m_minus_2
            fib_m_minus_2 = fib_m - fib_m_minus_1

        else:
            return i

    if fib_m_minus_1 and arr[offset + 1] == x:
        return offset + 1

    return -1


arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
x = 10
result = fibonacci_search(arr, x)

if result != -1:
    print(f"Element {x} is present at index {result}")
else:
    print(f"Element {x} is not present in the array")
