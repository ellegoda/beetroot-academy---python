def oops():
    raise KeyError("Out of Index")

def call():
    try:
        oops()
    except IndexError:
        print("An Index error handle")
    except KeyError:
        print("An Key Error Handle")


call()
