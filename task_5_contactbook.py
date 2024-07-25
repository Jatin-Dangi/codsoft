import json

contacts = []

def save_contacts_to_file():
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file, indent=4)

def load_contacts_from_file():
    try:
        with open('contacts.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def add_new_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    
    new_contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    
    contacts.append(new_contact)
    save_contacts_to_file()
    print("Contact added successfully.")

def display_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        for index, contact in enumerate(contacts, start=1):
            print(f"{index}. {contact['name']} - {contact['phone']}")

def search_for_contacts():
    search_query = input("Enter name or phone number to search: ")
    found_contacts = [contact for contact in contacts if search_query.lower() in contact['name'].lower() or search_query in contact['phone']]
    
    if not found_contacts:
        print("No matching contacts found.")
    else:
        for contact in found_contacts:
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            print()

def modify_contact():
    search_query = input("Enter name or phone number to update: ")
    for contact in contacts:
        if search_query.lower() in contact['name'].lower() or search_query in contact['phone']:
            print("Contact found. Enter new details (leave blank to keep current value).")
            contact['name'] = input("Enter new name: ") or contact['name']
            contact['phone'] = input("Enter new phone number: ") or contact['phone']
            contact['email'] = input("Enter new email: ") or contact['email']
            contact['address'] = input("Enter new address: ") or contact['address']
            
            save_contacts_to_file()
            print("Contact updated successfully.")
            return
    
    print("No matching contacts found.")

def remove_contact():
    search_query = input("Enter name or phone number to delete: ")
    global contacts
    contacts = [contact for contact in contacts if search_query.lower() not in contact['name'].lower() and search_query not in contact['phone']]
    
    save_contacts_to_file()
    print("Contact deleted successfully.")

def main_menu():
    global contacts
    contacts = load_contacts_from_file()
    
    while True:
        print("\nContact Management System")
        print("1. Add New Contact")
        print("2. Display All Contacts")
        print("3. Search Contacts")
        print("4. Modify Contact")
        print("5. Remove Contact")
        print("6. Exit")
        
        user_choice = input("Enter your choice: ")
        
        if user_choice == '1':
            add_new_contact()
        elif user_choice == '2':
            display_contacts()
        elif user_choice == '3':
            search_for_contacts()
        elif user_choice == '4':
            modify_contact()
        elif user_choice == '5':
            remove_contact()
        elif user_choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
