import mysql.connector
import bcrypt
from validation import emailValidation
from encryption import passwordEncryption

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Password",
    database = "encryption_website"
    )

def createAccount(emailEntry, passwordEntry):
    # Get users input
    email = emailEntry.get()
    password = passwordEntry.get()

    if len(password) <8:
        print("Passwords has to be at least 8 characters long")
        return
    
    hashed_password = passwordEncryption(password)

    if emailValidation(email):

        # Use the cursor to execute an SQL query to insert a new record
        mycursor = dataBase.cursor()
        
        try:
            sql = "INSERT INTO users(user_email, user_password) VALUES (%s, %s)"
            val = (email, hashed_password)
            mycursor.execute(sql, val)

            # Commit the changes to the database
            dataBase.commit()

            print("Account created successfully!")
        except mysql.connector.Error as err:
            if err.errno == 1062:
                print("Account has been created already")
            else:
                print("error {err}")
    else:
        print("Invalid Email")

def loginHandle(emailEntry, passwordEntry):
    # Get users input
    email = emailEntry.get()
    password = passwordEntry.get()

    # Use the cursor to execute an SQL query to see if the  email and password exist
    mycursor = dataBase.cursor()
    sql = "SELECT * FROM users WHERE user_email = %s"
    # Need comma at the end to make a tuple
    val = (email,)
    mycursor.execute(sql, val)

    result = mycursor.fetchone()

    # If login successful then print success, else print not successful
    if result:
        hashed_password = result[2].encode('utf-8')
        if bcrypt.checkpw(password.encode("utf-8"), hashed_password):
            print("Login successful")
        else:
            print("Login not successful")
    else:
        print("Login not successful")
