def menu():
    print()
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Exit")

def encode(password):
    encode_password = ""
    for digits in password:
        encode_password = str(int(digits) + 3)

    return encode_password


def decode(password):
    decode_password = ""
    for digits in password:
        decode_password += str(int(digits) - 3)
    return decode_password

if __name__ == '__main__':
    encode_password = None
    while True:
        menu()
        choice = input("Please enter an option: ")
        if choice == "1":
            password = input("Please enter your password to encode: ")
            encode_password = encode(password)
            print("Your password has been encoded and stored!")
            print(encode_password)
        if choice == "2":
            print(f"The encoded password is {encode_password} and the original password is {decode}")
        if choice == "3":
            break
