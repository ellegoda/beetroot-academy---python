import json

contacts = []


def load_contacts(json_file):
    global contacts
    with open(json_file, "r") as f:
        contacts = json.load(f)


def add_contact(json_file):
    first_name = input("Enter first name : ")
    last_name = input("Enter last name : ")
    full_name = input("Enter full name : ")
    contact_no = input("Enter Contact No : ")
    city = input("Enter city : ")

    contacts.append({
        "FirstName": first_name,
        "LastName": last_name,
        "FullName": full_name,
        "ContactNo": contact_no,
        "City": city
    })

    with open(json_file, "w") as f:
        json.dump(contacts, f, indent=2)


def search_by(search_by):
    search_text = input("Enter the search Text: ")

    for contact in contacts:
        if search_by == "s1":
            if contact["FirstName"] == search_text:
                print(contact)
        elif search_by == "s2":
            if contact["LastName"] == search_text:
                print(contact)
        elif search_by == "s3":
            if contact["FullName"] == search_text:
                print(contact)
        elif search_by == "s4":
            if contact["ContactNo"] == search_text:
                print(contact)
        elif search_by == "s5":
            if contact["City"] == search_text:
                print(contact)


def delete_contact(json_file):
    search_text = input("Enter the telephone number : ")

    for contact in contacts:
        if contact["ContactNo"] == search_text:
            contacts.remove(contact)
            print("Record removed")

    with open(json_file, "w") as f:
        json.dump(contacts, f, indent=2)


def update_contact(json_file):
    search_text = input("Enter the telephone number : ")

    for contact in contacts:
        if contact["ContactNo"] == search_text:
            print("Record found, enter the changes")
            first_name = input("Enter first name : ")
            last_name = input("Enter last name : ")
            full_name = input("Enter full name : ")
            city = input("Enter city : ")

            contacts.remove(contact)

            contacts.append({
                "FirstName": first_name,
                "LastName": last_name,
                "FullName": full_name,
                "ContactNo": search_text,
                "City": city
            })

            with open(json_file, "w") as f:
                json.dump(contacts, f, indent=2)
            print("Record updated")


def main(json_file):
    try:
        load_contacts(json_file)

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
                add_contact(json_file)
            elif action == "s1":
                search_by("s1")
            elif action == "s2":
                search_by("s2")
            elif action == "s3":
                search_by("s3")
            elif action == "s4":
                search_by("s4")
            elif action == "s5":
                search_by("s5")
            elif action == "d":
                delete_contact(json_file)
            elif action == "u":
                update_contact(json_file)
    except FileNotFoundError:
        print("Error : json file not found")

main("phone_book.json")
