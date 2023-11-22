import json


class PhoneBook:
    def __init__(self, json_file):
        self.json_file = json_file
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.json_file, "r") as f:
                self.contacts = json.load(f)
                return "OK"
        except FileNotFoundError:
            return "Error: JSON file not found"

    def add_contact(self, first_name, last_name, full_name, contact_no, city):
        for contact in self.contacts:
            if contact["ContactNo"] == contact_no:
                return "Error: Contact No details already exist"

        self.contacts.append({
            "FirstName": first_name,
            "LastName": last_name,
            "FullName": full_name,
            "ContactNo": contact_no,
            "City": city
        })

        self.save_contacts()
        return "OK"

    def search_by(self, search_by, search_text):
        for contact in self.contacts:
            if contact[search_by] == search_text:
                return contact["ContactNo"]

        return "Not Found"

    def delete_contact(self, search_text):
        for contact in self.contacts:
            if contact["ContactNo"] == search_text:
                self.contacts.remove(contact)
                self.save_contacts()
                return "OK"

        return "Not Found"

    def update_contact(self, search_text, first_name, last_name, full_name, city):
        for contact in self.contacts:
            if contact["ContactNo"] == search_text:
                self.contacts.remove(contact)
                self.contacts.append({
                    "FirstName": first_name,
                    "LastName": last_name,
                    "FullName": full_name,
                    "ContactNo": search_text,
                    "City": city
                })

                self.save_contacts()
                print("Record updated")
                return "OK"

        return "Not found"

    def save_contacts(self):
        with open(self.json_file, "w") as f:
            json.dump(self.contacts, f, indent=2)

    def main(self):
        print("""
        Please select action.
        a - add a new contact
        s1 - search by first name
        s2 - search by last name
        s3 - search by full name
        s4 - search by telephone number
        s5 - search by city
        d - delete by telephone number
        u - update by telephone number
        q - to quit from application""")

        while True:
            action = input("\nYour action: ")
            if action == "q":
                break
            elif action == "a":
                first_name = input("\nEnter the First Name: ")
                last_name = input("\nEnter the Last Name: ")
                full_name = input("\nEnter the Full Name: ")
                contact_no = input("\nEnter the Contact No: ")
                city = input("\nEnter the City: ")
                self.add_contact(first_name, last_name, full_name, contact_no, city)
            elif action == "s1":
                search_text = input("\nEnter the search Text: ")
                print(self.search_by("FirstName", search_text))
            elif action == "s2":
                search_text = input("\nEnter the search Text: ")
                print(self.search_by("LastName", search_text))
            elif action == "s3":
                search_text = input("\nEnter the search Text: ")
                print(self.search_by("FullName", search_text))
            elif action == "s4":
                search_text = input("\nEnter the search Text: ")
                print(self.search_by("ContactNo", search_text))
            elif action == "s5":
                search_text = input("\nEnter the search Text: ")
                print(self.search_by("City", search_text))
            elif action == "d":
                search_text = input("\nEnter the search Text: ")
                self.delete_contact(search_text)
            elif action == "u":
                search_text = input("\nEnter the ContactNo Text: ")
                first_name = input("\nEnter the First Name: ")
                last_name = input("\nEnter the Last Name: ")
                full_name = input("\nEnter the Full Name: ")
                city = input("\nEnter the City: ")
                print(self.update_contact(search_text, first_name, last_name, full_name, city))


if __name__ == "__main__":
    phone_book = PhoneBook("phone_book.json")
    phone_book.main()
