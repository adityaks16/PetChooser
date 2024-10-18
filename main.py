# Aditya Kunapareddy
# Purpose: This is my Pet Chooser program
# It allows users to:
# - View a list of pets
# - Choose a pet to see more details
# - Quit the program
#
# See https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html

import mysql.connector
from pets import Pets

def connect_to_database():
    # Connect to the database
    try:
        connection = mysql.connector.connect(
            host="cbcradio.org",
            user="cbcradio_bds4",
            password="Cherry36Cat*",
            database="cbcradio_bds754_4"
        )
        return connection
    except mysql.connector.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

def fetch_pets(connection):
    # Fetch all pets from the database
    try:
        cursor = connection.cursor()
        query = """
        SELECT pets.name, pets.age, owners.name, types.animal_type
        FROM pets
        JOIN owners ON pets.owner_id = owners.id
        JOIN types ON pets.animal_type_id = types.id
        """
        cursor.execute(query)
        return cursor.fetchall()
    except mysql.connector.Error as e:
        print(f"Error fetching pets: {e}")
        return []

def display_pets(pets):
    # Display a list of pet names
    print("Please choose a pet from the list below:")
    for i, pet in enumerate(pets, 1):
        print(f"[{i}] {pet.get_name()}")
    print("[Q] Quit")

def get_user_choice(max_choice):
    # Get and validate user input
    while True:
        choice = input("Choice: ").strip().lower()
        if choice == 'q':
            return None
        try:
            choice = int(choice)
            if 1 <= choice <= max_choice:
                return choice
            else:
                print(f"Please enter a number between 1 and {max_choice}, or 'Q' to quit.")
        except ValueError:
            print("Invalid input. Please enter a number or 'Q' to quit.")

def main():
    # Main program loop
    connection = None
    try:
        connection = connect_to_database()
        if not connection:
            return

        pet_data = fetch_pets(connection)
        pets = [Pets(name, age, owner, animal_type) for name, age, owner, animal_type in pet_data]

        while True:
            try:
                display_pets(pets)
                choice = get_user_choice(len(pets))

                if choice is None:
                    print("Thank you for using the Pet Chooser. Goodbye!")
                    break

                selected_pet = pets[choice - 1]
                print(f"\nYou have chosen {selected_pet}")
                input("Press [ENTER] to continue.")
                print()
            except IndexError:
                print("Error: Invalid pet selection. Please try again.")
            except Exception as e:
                print(f"An unexpected error occurred: {str(e)}. Please try again.")

    except mysql.connector.Error as e:
        print(f"A database error occurred: {str(e)}. The program will now exit.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}. The program will now exit.")
    finally:
        if connection and connection.is_connected():
            connection.close()
            print("Database connection closed.")

if __name__ == "__main__":
    main()