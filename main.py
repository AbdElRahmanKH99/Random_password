import random
import string
password = []

# Welcome to the Password Generator!
print("Welcome to the Password Generator!")

# Enter the total number of characters in the password: 
pass_len = int(input("Enter the total number of characters in the password: "))
# Enter the number of letters in the password: 
letters_len = int(input("Enter the number of letters in the password: "))
# Enter the number of numbers in the password: 
numbers_len = int(input("Enter the number of numbers in the password: "))
# Enter the number of symbols in the password: 
symbols_len = int(input("Enter the number of symbols in the password: "))

# Invalid input. The sum of letters, numbers, and symbols doesn't match the password length
if letters_len + numbers_len + symbols_len == pass_len:
    letters = random.choices(string.ascii_letters, k=letters_len)
    numbers = random.choices(string.digits, k=numbers_len)
    symbols = random.choices(string.punctuation, k=symbols_len)
    # password.extend(letters)
    # password.extend(numbers)
    # password.extend(symbols)
    password = (letters + numbers + symbols)
    random.shuffle(password)
# Generated Password:
    print(f"Generated Password: ", "".join(password))
else:
    print("Invalid input. The sum of letters, numbers, and symbols doesn't match the password length")
input("Press Enter to exit...")