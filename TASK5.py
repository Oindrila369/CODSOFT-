# Contact book dictionary to store contact information
contact_book = {}

# Function to add a new contact
def add_contact():
    name = input("Enter the name of the contact: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    address = input("Enter the address: ")
    contact_book[name] = {"phone": phone, "email": email, "address": address}
    print("Contact added successfully!")

# Function to view all contacts
def view_contacts():
    if not contact_book:
        print("Contact book is empty.")
    else:
        print("Contact List:")
        for name, contact_info in contact_book.items():
            print(f"Name: {name}")
            print(f"Phone: {contact_info['phone']}")
            print(f"Email: {contact_info['email']}")
            print(f"Address: {contact_info['address']}")
            print("---------------")

# Function to search for a contact
def search_contact():
    query = input("Enter the name or phone number to search for a contact: ")
    for name, contact_info in contact_book.items():
        if query in (name, contact_info["phone"]):
            print(f"Name: {name}")
            print(f"Phone: {contact_info['phone']}")
            print(f"Email: {contact_info['email']}")
            print(f"Address: {contact_info['address']}")
            return
    print("Contact not found.")

# Function to update a contact
def update_contact():
    name = input("Enter the name of the contact you want to update: ")
    if name in contact_book:
        print("Current Contact Information:")
        print(f"Name: {name}")
        print(f"Phone: {contact_book[name]['phone']}")
        print(f"Email: {contact_book[name]['email']}")
        print(f"Address: {contact_book[name]['address']}")
        print("---------------")
        phone = input("Enter the new phone number (leave empty to keep current): ")
        email = input("Enter the new email address (leave empty to keep current): ")
        address = input("Enter the new address (leave empty to keep current): ")
        if phone:
            contact_book[name]['phone'] = phone
        if email:
            contact_book[name]['email'] = email
        if address:
            contact_book[name]['address'] = address
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact you want to delete: ")
    if name in contact_book:
        del contact_book[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

# Main loop
while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option (1-6).")
