import sqlite3
import csv

def create_contacts_from_csv(db_path, csv_file):
    """
    Create new contacts in the SQLite database from a CSV file.

    Parameters:
        db_path (str): Path to the SQLite database file.
        csv_file (str): Path to the CSV file containing new contacts.
    """
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Open the CSV file and read the data
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)  # Assumes the CSV has headers: name, email, phone
        for row in reader:
            name = row['name']
            email = row['email']
            phone = row['phone']

            # Insert query to add a new contact
            cursor.execute("""
                INSERT INTO contact (name, email, phone)
                VALUES (?, ?, ?)
            """, (name, email, phone))

    # Commit changes and close connection
    conn.commit()
    conn.close()

    print("Contacts created successfully!")


if __name__ == "__main__":
    # Define paths to the database and CSV file
    db_path = 'instance/contacts.db'  # Replace with your database file path
    csv_file = 'csv/contacts.csv'  # Replace with your CSV file path

    # Call the function to create contacts
    create_contacts_from_csv(db_path, csv_file)