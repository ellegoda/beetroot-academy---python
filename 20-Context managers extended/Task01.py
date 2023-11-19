import logging
import os


class FileManager:
    def __init__(self, file_name, mode):

        if os.path.exists(file_name):
            self.filename = file_name
            self.mode = mode
            self.file = None
            self.counter = 0
        else:
            raise FileNotFoundError(f"An exception occured file not found {file_name}")

    def __enter__(self):
        self.counter += 1
        logging.info(f"Entering the file {self.filename}. Counter: {self.counter}")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.counter -= 1
        logging.info(f"Exiting the file {self.filename}. Counter: {self.counter}")
        if self.file:
            self.file.close()
        if exc_type is not None:
            logging.error(f"An exception of type {exc_type} occurred with value: {exc_value}")
            raise ValueError(f"An exception of type {exc_type} occurred with value: {exc_value}")


# Set up logging
logging.basicConfig(level=logging.INFO)

# Example usage:
filename = "example.txt"

# Writing to a file using the context manager
with FileManager(filename, "a") as file:
    file.write("Hello, this is a test.")

# Reading from a file using the context manager
with FileManager(filename, "r") as file:
    content = file.read()
    print(content)
