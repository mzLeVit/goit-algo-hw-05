def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    if len(args) < 2:
        return "Please provide both name and phone."
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_phone(args, contacts):
    if len(args) < 2:
        return "Please provide both name and new phone."
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Phone number updated."
    else:
        return "Contact not found."

def show_phone(args, contacts):
    if len(args) < 1:
        return "Please provide a name."
    name = args[0]
    if name in contacts:
        return f"Phone number for {name}: {contacts[name]}"
    else:
        return "Contact not found."
def show_all_contacts(contacts):
    if contacts:
        print("All contacts:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts available.")

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_phone(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            show_all_contacts(contacts)
        else:
            print("Invalid command.")

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "KeyError: Contact not found."
        except ValueError:
            return "ValueError: Give me name and phone please."
        except IndexError:
            return "IndexError: Give me name and phone please."
    return inner

@input_error
def change_phone(args, contacts):
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Phone number updated."
    else:
        return "Contact not found."

@input_error
def show_phone(args, contacts):
    try:
        name = args[0]
        return f"Phone number for {name}: {contacts[name]}"
    except IndexError:
        return "IndexError: Give me name please."
    except KeyError:
        return "KeyError: Contact not found."

@input_error
def show_all_contacts(contacts):
    try:
        if contacts:
            print("All contacts:")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        else:
            print("No contacts available.")
    except AttributeError:
        return "AttributeError: Please provide valid contacts dictionary."




if __name__ == "__main__":
    main()
