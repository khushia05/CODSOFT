import time
contacts = []

def add_contact():
    name = input("Enter the name: ")
    phone_no = input("Enter the phone number: ")
    email_id = input("Enter the email ID: ")
    address = input("Enter the address: ")
    contact = {
        "Name": name, 
        "Phone_No": phone_no,
        "Email_ID": email_id,
        "Address": address
    }
    contacts.append(contact)
    print("Contact saved successfully!")

def view_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        print("\nContact List:")
        for contact in contacts:
            print(f"Name: {contact['Name']}, Phone: {contact['Phone_No']}")

def search_contact():
    search_term = input("Enter the name or phone number to search: ")
    found = False
    for contact in contacts:
        if search_term.lower() in contact['Name'].lower() or search_term in contact['Phone_No']:
            print(f"Name: {contact['Name']}, Phone: {contact['Phone_No']}, Email: {contact['Email_ID']}, Address: {contact['Address']}")
            found = True
    if not found:
        print("No matching contact found.")

def update_contact():
    search_name = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if contact['Name'].lower() == search_name.lower():
            print("Enter new details (leave blank to keep current value):")
            contact['Name'] = input(f"Name [{contact['Name']}]: ") or contact['Name']
            contact['Phone_No'] = input(f"Phone [{contact['Phone_No']}]: ") or contact['Phone_No']
            contact['Email_ID'] = input(f"Email [{contact['Email_ID']}]: ") or contact['Email_ID']
            contact['Address'] = input(f"Address [{contact['Address']}]: ") or contact['Address']
            print("Contact updated successfully!")
            return
    print("Contact not found.")

def delete_contact():
    search_name = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if contact['Name'].lower() == search_name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")

def main():
    while True:
        print("\nCONTACT MANAGEMENT SYSTEM")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        time.sleep(2)   

if __name__ == "__main__":
    main()
