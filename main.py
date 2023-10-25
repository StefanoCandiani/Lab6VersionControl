
# Lab 6 - Version Control
# Lab Partners: Henry Harborne, Stefano Candiani

def print_menu():
    # Prints menu
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def encode(input_string):
    # Accepts input string. Iterates through it and adds 3 to each character. Returns output string
    output_string = ''.join(str(int(char) + 3) for char in input_string)
    return output_string

def decode(input_string):
    # Accepts input string. Iterates through it and subtracts 3 to each character. Returns output string
    output_string = ''.join(str(int(char) - 3) for char in input_string)
    return output_string

def main():
    encoded_message = ''
    # Runs until break
    while True:
        # Prints menu and requests user input
        print_menu()
        option = input('\nPlease enter an option: ')
        if option == '1':
            # Stores the new encoded message
            message = input('Please enter a password to encode: ')
            encoded_message = encode(message)
            print('Your password has been encoded and stored!\n')
        elif option == '2':
            # Prints both the encoded and original messages
            print(f'The encoded password is {encoded_message}, and the original password is {decode(encoded_message)}.\n')
        elif option == '3':
            # Breaks out of the loop to finish code run
            break


if __name__ == '__main__':
    main()