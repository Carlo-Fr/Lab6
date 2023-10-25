#Carlo Fraley Lab 6

def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()

#prints menu with options

def encode_password(password):
    encoded_password = [0,1]
    encoded_password[0:-1] = password
    for i in range(len(encoded_password)):
        encoded_password[i] = str(int(encoded_password[i]) + 3)
    del encoded_password[-1]
    correct_encoded_password = ''.join(encoded_password)
    return correct_encoded_password

#Takes in original password, turns into list, increases each element by 3,
#then rejoins together into variable for the encoded password

def main():
    menu()
    original_password = None
    encoded_password = None
    x = 1
    #original_password stores the original password, encoded_password stores the encoded
    #password, variable x is used to keep function running
    while x == 1:
        selection = int(input("Please enter an option: "))
        if selection == 1:
            original_password = input("Please enter your password to encode: ")
            encoded_password = encode_password(original_password)
            print("Your password has been encoded and stored!")
            print()
            #stores original password and uses other function to get encoded password
        elif selection == 2:
            pass
        elif selection == 3:
            x = 0
            #stops function


if __name__ == "__main__":
    main()
