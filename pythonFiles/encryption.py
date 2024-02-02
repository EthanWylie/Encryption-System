import bcrypt

def passwordEncryption(password):
    salt = bcrypt.gensalt()
    encryptedPassword = bcrypt.hashpw(password.encode('utf-8'), salt)
    return encryptedPassword
