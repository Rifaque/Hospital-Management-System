import mysql.connector


def fetch_doc_data():
    # Connect to MySQL database
    db = mysql.connector.connect(
        host="localhost",
        user="the",
        password="password",
        database="hpms"
    )

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute a query to fetch patient data
    query = ("SELECT * FROM Doctor")
    cursor.execute(query)

    # Fetch all the rows
    doc_data = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    db.close()

    return doc_data

