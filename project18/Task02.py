import logging
import unittest
import os
import io

from project18.Task01 import FileManager  # Replace with the actual module name


class TestFileManager(unittest.TestCase):
    def setUp(self):
        self.filename = "test_file.txt"
        with open(self.filename, "w") as file:
            file.write("Test content")

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_read_file(self):
        with FileManager(self.filename, "r") as file:
            content = file.read()
            self.assertEqual(content, "Test content")

    def test_write_file(self):
        with FileManager(self.filename, "w") as file:
            file.write("New test content")

        with FileManager(self.filename, "r") as file:
            content = file.read()
            self.assertEqual(content, "New test content")

    def test_exception_handling(self):
        with self.assertRaises(FileNotFoundError):
            with FileManager("non-existing-file.txt", "a") as file:
                file.write("Should not reach here")

    def test_logging(self):
        logging.basicConfig(level=logging.INFO)

        log_stream = io.StringIO()
        logging.getLogger().handlers = [logging.StreamHandler(log_stream)]

        with FileManager(self.filename, "r") as file:
            content = file.read()

        log_messages = log_stream.getvalue()
        self.assertIn("Entering the file", log_messages)
        self.assertIn("Exiting the file", log_messages)
        self.assertNotIn("An exception of type", log_messages)


if __name__ == "__main__":
    unittest.main()
