def arg_rules(type_: type, max_length: int, contains: list):
    def inner_func(func):
        def inner_args(args_01):
            result = "False"
            if type(args_01) == type_ and len(args_01) < max_length and all(contain in args_01 for contain in contains):
                result = func(args_01)

            return result

        return inner_args

    return inner_func


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan('johndoe05@gmail.com'))
print(create_slogan('S@SH05'))
