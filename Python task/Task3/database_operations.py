import mysql.connector

# Function to connect to MySQL and perform operations
def perform_database_operations():
    try:
        # Connect to MySQL server
        conn = mysql.connector.connect(
            host='localhost',
            user='root',  # Replace with your MySQL username
            password='Pulkit6397',  # Replace with your MySQL password
            database='school'  # Replace with your MySQL database name
        )
        
        if conn.is_connected():
            print("Connected to MySQL database")

            # Create a cursor object using cursor() method
            cursor = conn.cursor()

            # Create table if not exists
            create_table_query = """
            CREATE TABLE IF NOT EXISTS students (
                student_id INT AUTO_INCREMENT PRIMARY KEY,
                first_name VARCHAR(50),
                last_name VARCHAR(50),
                age INT,
                grade FLOAT
            )
            """
            cursor.execute(create_table_query)
            print("Students table created successfully")

            # Insert a new student record
            insert_query = """
            INSERT INTO students (first_name, last_name, age, grade)
            VALUES ('Alice', 'Smith', 18, 95.5)
            """
            cursor.execute(insert_query)
            conn.commit()
            print("Inserted a new student record")

            # Update the grade of the student with the first name "Alice"
            update_query = """
            UPDATE students
            SET grade = 97.0
            WHERE first_name = 'Alice'
            """
            cursor.execute(update_query)
            conn.commit()
            print("Updated the grade for Alice")

            # Delete the student with the last name "Smith"
            delete_query = """
            DELETE FROM students
            WHERE last_name = 'Smith'
            """
            cursor.execute(delete_query)
            conn.commit()
            print("Deleted the student with last name Smith")

            # Fetch and display all student records
            select_query = "SELECT * FROM students"
            cursor.execute(select_query)
            records = cursor.fetchall()

            if records:
                print("\nStudent records:")
                for record in records:
                    print(record)
            else:
                print("\nNo student records found")

            # Close cursor and connection
            cursor.close()
            conn.close()

    except mysql.connector.Error as error:
        print("Error while connecting to MySQL:", error)

# Call the function to perform database operations
perform_database_operations()
