class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.log_to_file(msg)

    def log_to_file(self, msg):
        try:
            with open("logs.txt", "a") as log_file:
                log_file.write(f"Error: {msg}\n")
        except Exception as e:
            print(f"Error while logging to file: {e}")


try:
    raise CustomException("This is a custom exception.")
except CustomException as ce:
    print(f"Caught custom exception: {ce}")