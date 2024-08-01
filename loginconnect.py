def checkpassword(username,password):
    import mysql.connector
    # Database connection settings
    db_host = 'localhost'
    db_user = 'the'
    db_password = 'password'
    db_name = 'hpms'
    # Establish a connection to the database
    cnx = mysql.connector.connect(
    user=db_user,
    password=db_password,
    host=db_host,
    database=db_name
    )

        # Create a cursor object to execute queries
    cursor = cnx.cursor()

    # Query to check if the username and password exist
    query = "SELECT 1 FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))

        # Fetch the result
    result = cursor.fetchone()

    # Close the cursor and connection
    cursor.close()
    cnx.close()

    # Return 1 if the username and password exist, 0 otherwise
    return 1 if result else 0
#import mysql.connector
#import tkinter as tk
#from PyQt6.QtWidgets import QMessageBox
#def checkpassword(password):
#   print(password)
#def LoginEvent(password1,username1):
#     username = username1
#     password = password1
#     msg = QMessageBox()
#     msg.setIcon(QMessageBox.Icon.Information)
#     msg.setWindowTitle("Login")
#     msg.setText("You are login with \n Username:" + str(username))
#     msg.exec()
#def loginEvent(passwordreal, usernamereal):
#    return None