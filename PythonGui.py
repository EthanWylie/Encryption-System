from customtkinter import *
import mysql.connector
import random

window = CTk()
window.geometry("500x400")
window._set_appearance_mode("dark")
set_default_color_theme("Oceanix.json") #json file from, https://github.com/avalon60/ctk_theme_builder

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Password",
    database = "encryption_website"
    )

def createAccount():
    # Create connection to database
    dataBase

    # Get users input
    email = emailEntry.get()
    password = passwordEntry.get()

    # Use the cursor to execute an SQL query to insert a new record
    mycursor = dataBase.cursor()
    try:
        sql = "INSERT INTO users(user_email, user_password) VALUES (%s, %s)"
        val = (email, password)
        mycursor.execute(sql, val)

        # Commit the changes to the database
        dataBase.commit()

        print("Account created successfully!")
    except mysql.connector.Error as err:
        if err.errno == 1062:
            print("Account has been created already")
        else:
            print("error {err}")
    



def loginHandle():
    # Create connection to database
    dataBase

    # Get users input
    email = emailEntry.get()
    password = passwordEntry.get()

    # Use the cursor to execute an SQL query to see if the  email and password exist
    mycursor = dataBase.cursor()
    sql = "SELECT * FROM users WHERE user_email = %s AND user_password = %s"
    val = (email, password)
    mycursor.execute(sql, val)

    result = mycursor.fetchone()

    # If login successful then print success, else print not successful
    if result:
        print("Login successful")
    else:
        print("Login not successful")



loginFrame = CTkFrame(master=window, bg_color="black", border_width=2)
loginFrame.pack(pady=10, padx=30, fill="both", expand=True)

label = CTkLabel(master=loginFrame, text="Login", font=("New York Times", 40))
label.pack(pady=12, padx=10)

emailEntry = CTkEntry(master=loginFrame, placeholder_text="Email")
emailEntry.pack(pady=12, padx=10)

passwordEntry = CTkEntry(master=loginFrame, placeholder_text="Password", show="*")
passwordEntry.pack(pady=12, padx=10)

loginBtn = CTkButton(master=window, bg_color="#51667e", text="Login", command=loginHandle)
loginBtn.place(relx=0.5, rely=0.5, anchor="center")

createAccontButton = CTkButton(master=window, bg_color="#51667e", text="Create Account", command=createAccount)
createAccontButton.place(relx=0.5, rely=0.6, anchor="center")

window.mainloop()

