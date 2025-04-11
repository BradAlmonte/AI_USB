import sys
import subprocess
from install_tools import install_tools
from ai_library import search_library

def main():
    print("Welcome to the AI Command Line Interface!")
    
    while True:
        print("\nChoose an action:")
        print("1. Install Tools")
        print("2. Search AI Library")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            install_tools()
        elif choice == '2':
            query = input("Enter the tool or command to search for: ")
            response = search_library(query)
            print(f"AI Response: {response}")
        elif choice == '3':
            print("Exiting AI CLI...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

