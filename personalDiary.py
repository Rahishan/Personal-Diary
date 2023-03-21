import os
import datetime

# This function prompts the user to add a new diary entry.
def add_entry():
    entry = input("Enter your diary entry:\n")
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("diary.txt", "a") as f:
        f.write(f"{date}\n{entry}\n\n")
    print("Entry added successfully.")

# This function displays all diary entries in the diary file.
def view_entries():
    try:
        with open("diary.txt", "r") as f:
            entries = f.read()
        if entries:
            print(entries)
        else:
            print("No entries found.")
    except FileNotFoundError:
        print("No entries found.")

#  This function deletes all diary entries from the diary file.
def delete_entries():
    try:
        os.remove("diary.txt")
        print("All entries deleted successfully.")
    except FileNotFoundError:
        print("No entries found.")

# This function displays the menu options and prompts the user for input
def menu():
    while True:
        print("\nSelect an option:")
        print("1. Add diary entry")
        print("2. View diary entries")
        print("3. Delete all diary entries")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            delete_entries()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    menu()
