import mysql.connector


def fetch_appoint_data():
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
    query = ("SELECT pat_no, fname, lname, phonenumber, email, address, age, dateofbirth, doctor,"
             " t_of_appointment, symptoms,appointment_status FROM appointment_details")
    cursor.execute(query)

    # Fetch all the rows
    appoint_data = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    db.close()

    return appoint_data

