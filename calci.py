# script.py - Python backend for Binary Calculator

def binary_to_decimal(binary):
    return int(binary, 2)

def decimal_to_binary(decimal):
    return bin(decimal)[2:]

def calculator():
    print("Welcome to Binary Calculator!")
    print("1: Binary to Decimal")
    print("2: Decimal to Binary")
    
    choice = input("Choose an option (1/2): ")
    
    if choice == '1':
        binary = input("Enter a binary number: ")
        print("Decimal:", binary_to_decimal(binary))
    elif choice == '2':
        decimal = int(input("Enter a decimal number: "))
        print("Binary:", decimal_to_binary(decimal))
    else:
        print("Invalid option")

if __name__ == "__main__":
    calculator()
