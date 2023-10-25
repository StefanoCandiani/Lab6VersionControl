def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def encode(input_string):
    output_string = ''.join(str(int(char) + 3) for char in input_string)
    return output_string


def main():
    if __name__ == '__main__':
        main()