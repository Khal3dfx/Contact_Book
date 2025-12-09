# To run the program: python3 Contact_Book.py

import json
import os
import getch

FILE_NAME = "contacts.json"
contacts = []


# ---------------- FILE HANDLING ----------------

def load_contacts():
    global contacts
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            try:
                contacts = json.load(file)
            except json.JSONDecodeError:
                contacts = []


def save_contacts():
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


# ---------------- MENU & FEATURES ----------------

def menu():
    print("📇 Contact Book")
    print("1) Show all contacts")
    print("2) Add a contact")
    print("3) Remove a contact")
    print("4) Search contacts by name")
    print("5) Update a contact")
    print("6) Quit")

    print("Press a number (1-6):")


def show_contacts():
    if not contacts:
        print("There are no contacts.")
        return

    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. Name: {contact[0]} | Phone: {contact[1]} | Email: {contact[2]}")


def add_contact():
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email: ")

    contacts.append([name, phone, email])
    contacts.sort(key=lambda c: c[0].lower()) 
    save_contacts()

    print("Contact added successfully.")
    input("Press Enter to continue....")


def remove_contact(index):
    contacts.pop(index)
    save_contacts()


def search(name):
    if not contacts:
        print("There are no contacts.")
        return

    for contact in contacts:
        if contact[0].lower() == name.lower():
            print("✅ Contact found:")
            print(f"Name: {contact[0]} | Phone: {contact[1]} | Email: {contact[2]}")
            return

    print("❌ The contact does not exist.")

def update_contact(index):
    contact = contacts[index]

    print("\nWhat do you want to update?")
    print("1) Name")
    print("2) Phone")
    print("3) Email")
    choice = input("Choose (1-3): ")

    if choice == "1":
        contact[0] = input("Enter new name: ")
        contacts.sort(key=lambda c: c[0].lower())
    elif choice == "2":
        contact[1] = input("Enter new phone number: ")
    elif choice == "3":
        contact[2] = input("Enter new email: ")
    else:
        print("Invalid choice.")
        return

    save_contacts()
    print("Contact updated successfully.")

# ---------------- MAIN LOOP ----------------

load_contacts()   # ✅ LOAD contacts on startup

while True:
    os.system('clear')
    menu()

    key = getch.getch()
    if isinstance(key, bytes):
        key = key.decode()

    if key == "1":
        os.system('clear')
        show_contacts()
        input("\nPress Enter to continue....")

    elif key == "2":
        os.system('clear')
        add_contact()

    elif key == "3":
        os.system('clear')
        show_contacts()

        if not contacts:
            input("\nPress Enter to continue....")
            continue

        r = input("Enter the number of the contact you want to remove: ")

        if not r.isdigit():
            print("Invalid input.")
            input("\nPress Enter to continue....")
            continue

        r = int(r) - 1

        if r < 0 or r >= len(contacts):
            print("Contact number does not exist.")
            input("\nPress Enter to continue....")
            continue

        remove_contact(r)
        print("Contact removed successfully.")
        input("\nPress Enter to continue....")

    elif key == "4":
        os.system('clear')
        name = input("Enter the name you want to search for: ")
        search(name)
        input("\nPress Enter to continue....")

    elif key == "5":
        os.system('clear')
        show_contacts()

        if not contacts:
            input("\nPress Enter to continue....")
            continue

        r = input("Enter the number of the contact to update: ")

        if not r.isdigit():
            print("Invalid input.")
            input("\nPress Enter to continue....")
            continue

        r = int(r) - 1

        if r < 0 or r >= len(contacts):
            print("Contact number does not exist.")
            input("\nPress Enter to continue....")
            continue

        update_contact(r)
        input("\nPress Enter to continue....")

    elif key == "6":
        save_contacts()   # ✅ SAVE before exiting
        print("\nThanks for using Contact Book App! Goodbye!\n")
        break
