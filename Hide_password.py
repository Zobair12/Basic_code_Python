import getpass

username = input("Enter your username: ") 
password = getpass.getpass("Enter your password: ")

print("\nLogging in...")
print("Usernam:", username)
print("Password: [Hidden for security ]")