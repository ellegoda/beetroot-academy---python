import unittest
from Task04 import PhoneBook


class Test_PhoneBook(unittest.TestCase):
    def test_search_by_first_name(self):
        phone_book = PhoneBook("phone_book.json")
        self.assertEqual(phone_book.search_by("FirstName", "Prasad"), "0738202773", "Error : Contact Not found")

    def test_search_by_last_name(self):
        phone_book = PhoneBook("phone_book.json")
        self.assertEqual(phone_book.search_by("LastName", "Peiris"), "0738202773", "Error : Contact Not found")

    def test_search_by_full_name(self):
        phone_book = PhoneBook("phone_book.json")
        self.assertEqual(phone_book.search_by("FullName", "Geethanjali"), "Not Found", "Error : Contact Not found")

    def test_1_delete_contact(self):
        phone_book = PhoneBook("phone_book.json")
        self.assertEqual(phone_book.delete_contact("074345234"), "OK", "Error Occurred ")

    def test_2_add_contact(self):
        phone_book = PhoneBook("phone_book.json")
        self.assertEqual(phone_book.add_contact
                         ("Therese",
                          "Peiris",
                          "Therese Lavon Peiris",
                          "074345234",
                          "Taby"), "OK", "Error Occurred ")

    def test_3_update_contact(self):
        phone_book = PhoneBook("phone_book.json")
        self.assertEqual(phone_book.update_contact(
                        "074345234",
                        "Therese",
                        "Peiris",
                        "Werage Therese Lavon Shehara Peiris",
                        "Stockholm"), "OK", "Error Occurred ")