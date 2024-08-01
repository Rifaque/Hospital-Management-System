def insert_patient_data(pat_no,fname, lname, phonenumber, email, address, age, dateofbirth, blood, doctor, t_of_appointment, symptoms):
    # Database connection settings
    username = 'the'
    password = 'password'
    hostname = 'localhost'
    database = 'hpms'
    import mysql.connector

    # Establish a connection to the database
    cnx = mysql.connector.connect(
        user=username,
        password=password,
        host=hostname,
        database=database
    )

    # Create a cursor object to execute queries
    cursor = cnx.cursor()

    # Insert data into the table
    query = """
        INSERT INTO appointment_details (
            pat_no,
            fname,
            lname,
            phonenumber,
            email,
            address,
            age,
            dateofbirth,
            blood,
            doctor,
            t_of_appointment,
            symptoms
        ) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        pat_no,
        fname,
        lname,
        phonenumber,
        email,
        address,
        age,
        dateofbirth,
        blood,
        doctor,
        t_of_appointment,
        symptoms
    )
    query_pat = """
            INSERT INTO patients_details (
                pat_no,
                fname,
                lname,
                phonenumber,
                email,
                address,
                age,
                dateofbirth,
                blood,
                doctor
            ) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s,%s)
        """
    values_pat = (
        pat_no,
        fname,
        lname,
        phonenumber,
        email,
        address,
        age,
        dateofbirth,
        blood,
        doctor

    )
    cursor.execute(query, values)
    cursor.execute(query_pat, values_pat)
    # Commit the changes
    cnx.commit()

    # Close the cursor and connection
    cursor.close()
    cnx.close()