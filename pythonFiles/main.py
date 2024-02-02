from customtkinter import *
from validation import emailValidation
from encryption import passwordEncryption
from database import createAccount, loginHandle, dataBase

window = CTk()
window.geometry("500x400")
window._set_appearance_mode("light")
set_default_color_theme("Oceanix.json") #json file from, https://github.com/avalon60/ctk_theme_builder
window.title("Python Password Encryption GUI with MySql")
window.iconbitmap("data-encryption-pic.ico")

loginFrame = CTkFrame(master=window, bg_color="black", border_width=2)
loginFrame.pack(pady=10, padx=30, fill="both", expand=True)

label = CTkLabel(master=loginFrame, text="Login", font=("New York Times", 40))
label.pack(pady=12, padx=10)

emailEntry = CTkEntry(master=loginFrame, placeholder_text="Email")
emailEntry.pack(pady=12, padx=10)

passwordEntry = CTkEntry(master=loginFrame, placeholder_text="Password", show="*")
passwordEntry.pack(pady=12, padx=10)

loginBtn = CTkButton(master=window, bg_color="#51667e", text="Login", command=lambda: loginHandle(emailEntry, passwordEntry))
loginBtn.place(relx=0.5, rely=0.5, anchor="center")

createAccontButton = CTkButton(master=window, bg_color="#51667e", text="Create Account", command=lambda: createAccount(emailEntry, passwordEntry))
createAccontButton.place(relx=0.5, rely=0.6, anchor="center")


if __name__ == "__main__":
    window.mainloop()
