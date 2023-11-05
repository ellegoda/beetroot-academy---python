def stop_words(words: list):
    def inner(func):
        def inner_args(*args):
            result = func(*args)
            censored_result = result
            for word in words:
                censored_result = censored_result.replace(word, '*')
            return censored_result

        return inner_args
    return inner


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return (f"{name} drinks pepsi in his brand new BMW!")

print(create_slogan ("Steve"))