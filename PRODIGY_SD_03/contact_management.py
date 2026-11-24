contacts = {}

while True:
    print("\n===== CONTACT MANAGEMENT SYSTEM =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Contact
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")

        contacts[name] = {
            "phone": phone,
            "email": email
        }

        print("Contact added successfully!")

    # View Contacts
    elif choice == "2":
        if not contacts:
            print("No contacts found!")
        else:
            print("\n===== CONTACT LIST =====")

            for name, details in contacts.items():
                print("\nName:", name)
                print("Phone:", details["phone"])
                print("Email:", details["email"])

    # Edit Contact
    elif choice == "3":
        name = input("Enter the name of contact to edit: ")

        if name in contacts:
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")

            contacts[name]["phone"] = phone
            contacts[name]["email"] = email

            print("Contact updated successfully!")
        else:
            print("Contact not found!")

    # Delete Contact
    elif choice == "4":
        name = input("Enter the name of contact to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    # Exit
    elif choice == "5":
        print("Thank you for using Contact Management System!")
        break

    else:
        print("Invalid choice! Please try again.")