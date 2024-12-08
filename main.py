import generator

print("Enter 1 to generate a password\nEnter 2 to store a password")
user_choice= int(input("Enter choice 1 or 2: "))
match user_choice:
    case 1:
        password= generator.password()
        print(f"{password}, length: {len(password)}")
    case 2:
        password= input("Enter a password to store: ")
        username= input("Enter the username associated with the password: ")
        generator.store(password,username)
    case default:
        print("Choice not valid")
