import random
import string

def generate(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Hello,Welcome to the Password generator")
    length = int(input("Enter the length of the password you want to generate:"))
    password = generate(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
