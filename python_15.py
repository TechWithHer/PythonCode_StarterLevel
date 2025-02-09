# Initialize an empty phonebook
phonebook = {}

def add_contact(name, phone):
    phonebook[name] = phone
    print(f"Contact '{name}' added.")

def retrieve_contact(name):
    return phonebook.get(name, "Contact not found.")

def update_contact(name, new_phone):
    if name in phonebook:
        phonebook[name] = new_phone
        print(f"Contact '{name}' updated.")
    else:
        print("Contact not found.")

def delete_contact(name):
    if name in phonebook:
        del phonebook[name]
        print(f"Contact '{name}' deleted.")
    else:
        print("Contact not found.")

def display_contacts():
    if phonebook:
        print("Phonebook Contacts:")
        for name, phone in phonebook.items():
            print(f"{name}: {phone}")
    else:
        print("Phonebook is empty.")

# Example Usage
add_contact("Alice", "123-456-7890")
add_contact("Bob", "987-654-3210")
print(retrieve_contact("Alice"))  # Output: 123-456-7890
update_contact("Alice", "111-222-3333")
delete_contact("Bob")
display_contacts()
