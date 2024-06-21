import mysql.connector

# Connect to MySQL server
conn = mysql.connector.connect(
    host='localhost',
    user='root',  # Replace with your MySQL username
    password='Pulkit6397'  # Replace with your MySQL password
)
cursor = conn.cursor()

# Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS school")

# Connect to the newly created database
conn.database = 'school'

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    grade FLOAT
)
""")

# Close the connection
cursor.close()
conn.close()

print("Database and table created successfully.")
