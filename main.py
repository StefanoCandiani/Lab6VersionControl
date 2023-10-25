def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def encode(input_string):
    output_string = ''.join(str(int(char) + 3) for char in input_string)
    return output_string

def decode(input_string):
    output_string = ''.join(str(int(char) - 3) for char in input_string)
    return output_string

def main():
    encoded_message = ''
    while True:
        print_menu()
        option = input('\nPlease enter an option: ')
        if option == '1':
            message = input('Please enter a password to encode: ')
            encoded_message = encode(message)
            print('Your password has been encoded and stored!\n')
        elif option == '2':
            print(f'The encoded password is {encoded_message}, and the original password is {decode(encoded_message)}.\n')
        elif option == '3':
            break


if __name__ == '__main__':
    main()