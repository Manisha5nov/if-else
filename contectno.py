contacts = {}

while True:
    print("\n====== CONTACT BOOK ======")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Display All Contacts")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")

        contacts[name] = phone
        print("✅ Contact added successfully!")

    elif choice == "2":
        name = input("Enter Name to Search: ")

        if name in contacts:
            print(f"📞 {name} : {contacts[name]}")
        else:
            print("❌ Contact not found.")

    elif choice == "3":
        name = input("Enter Name to Delete: ")

        if name in contacts:
            del contacts[name]
            print("🗑️ Contact deleted successfully!")
        else:
            print("❌ Contact not found.")

    elif choice == "4":
        if len(contacts) == 0:
            print("📭 No contacts available.")
        else:
            print("\n📋 Contact List")
            print("-" * 30)

            for name, phone in contacts.items():
                print(f"Name : {name}")
                print(f"Phone: {phone}")
                print("-" * 30)

    elif choice == "5":
        print("👋 Thank you for using Contact Book!")
        break

    else:
        print("❌ Invalid choice. Please enter 1 to 5.")