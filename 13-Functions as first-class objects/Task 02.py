def outer_function(x):

    def inner_function(y):

        return x + y

    return inner_function

add_five = outer_function(5)

result = add_five(10)

print(result)
