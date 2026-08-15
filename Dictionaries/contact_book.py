contacts = {}
while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Display All Contacts")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added successfully!")
    elif choice == "2":
        name = input("Enter name to search: ")
        if name in contacts:
            print("Phone Number:", contacts[name])
        else:
            print("Contact not found.")
    elif choice == "3":
        if not contacts:
            print("No contacts available.")
        else:
            print("\nContacts:")
            for name, phone in contacts.items():
                print(name, ":", phone)
    elif choice == "4":
        print("Exiting Contact Book...")
        break
    else:
        print("Invalid choice. Please enter 1-4.")