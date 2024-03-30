import re

def get_user_choice():
    print("Menu:")
    print(" 1. Add a new contact")
    print(" 2. Edit an existing contact")        if contacts else  ""
    print(" 3. Delete a contact")                if contacts else  ""
    print(" 4. Search for a contact")            if contacts else  ""
    print(" 5. Display all contacts")            if contacts else  ""
    print(" 6. Export contacts to a text file")  if contacts else  ""
    print(" 7. Quit")

    while True:
        try:
            if not contacts:
                choice = int(input("\nEnter 1 to Add New Contact, or 7 to Quit: "))
                if choice != 1 and choice != 7:
                    print(f"\nSorry. Only valid choices at this point are 1 or 7!\n")
                else:
                    return choice
            else:
                choice = int(input("\nEnter your choice (1-7): "))
                if 1 <= choice <= 7:
                    return choice
                else:
                    print(f"\nInvalid choice. Please enter a number between 1 and 7\n")
        except ValueError:
                print("\nInvalid input. Please enter a number\n")

def is_valid_phone(phone):
    pattern = r"^\d{3}-\d{3}-\d{4}$"
    return bool(re.match(pattern, phone))

def is_valid_email(email):
    pattern = r"[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[a-z]{2,}"
    return bool(re.match(pattern, email))
    
def add_contact():
    name = input("\nEnter contact name: ")
    phone = input("\nEnter phone number (XXX-XXX-XXXX): ")
    while not is_valid_phone(phone) or phone in contacts:
        print("\nPhone # is already a key in the system for an existing contact...") if phone in contacts else ""
        phone = input("Please enter a valid number (XXX-XXX-XXXX): ")
    email = input("\nEnter email address: ")
    while not is_valid_email(email):
        email = input("Invalid Email Address. Please eneter a valid email address: ")
    info = input("\nEnter any additional information: ")
    contacts[phone] = {"name": name, "email": email, "info": info}
    print("\nContact", name, "added successfully!\n")

def edit_contact():
    phone = input("\nEnter phone number of the contact to edit: ")
    if phone not in contacts:
        print("\nContact phone # not found!")
    else:
        contact = contacts[phone]
        print(f"\nEditing: {contact}")
        name = input("\nEnter new name (or enter to not change): ")
        if name: contact["name"] = name
        email = input("\nEnter new email address (or enter to not change): ")
        while email and not is_valid_email(email):
            email = input("\nInvalid Email Address, Enter new one (or enter to not change): ")
        if email: contact["email"] = email
        info = input("\nEnter new additional information (or enter to not change): ")
        if info: contact["info"] = info
        print("\nContact updated successfully!\n")

def delete_contact():
    phone = input("\nEnter phone number of the contact to delete: ")
    if phone in contacts:
        del contacts[phone]
        print("\nContact deleted successfully!\n")
    else:
        print("\nContact not found!\n")

def print_contact(phone):
    print("-" * 30)
    print(" Name:\t", contacts[phone]['name'])
    print(" Phone:\t", phone)
    print(" Email:\t", contacts[phone]['email'])
    print(" Info:\t", contacts[phone]['info'])

def search_contact():
    phone = input("\nEnter phone number of the contact to search for: ")
    if phone in contacts:
        print_contact(phone)
        print("-" * 30)
    else:
        print("\nContact not found!\n")

def display_all_contacts():
    print("\nContact List: ")
    for phone in contacts:
        print_contact(phone)
    print("-" * 30)

def export_contacts():
    try:
        with open("contacts.txt", "w") as file:
            for phone, contact in contacts.items():
                file.write(f"Name:\t{contact['name']}\n")
                file.write(f"Phone:\t{phone}\n")
                file.write(f"Email:\t{contact['email']}\n")
                file.write(f"Info:\t{contact['info']}\n\n")
            print("\nContacts exported successfully to contacts.txt!\n")
    except IOError:
        print("\nAn error occurred while exporting contacts\n")

menu = {
    1: add_contact,
    2: edit_contact,
    3: delete_contact,
    4: search_contact,
    5: display_all_contacts,
    6: export_contacts
}

print("\nWelcome to the Contact Management System!\n")

contacts = {}  #Global Dictionary

while True:
    choice = get_user_choice()

    if choice == 7:  
        print("\nExiting the Contact Management System...\n")
        break 
    else:
        menu[choice]()
