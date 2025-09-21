def mask_password(password):
    return '*' * len(password)

if __name__ == "__main__":
    MIN_PASSWORD_LENGTH = 8
    while True:
        password = input("password: ")
        if len(password) >= MIN_PASSWORD_LENGTH:
            break
        print("The password length is insufficient, please re-enter it!")
    masked_pwd = mask_password(password)
    print("Pythonista ",masked_pwd)