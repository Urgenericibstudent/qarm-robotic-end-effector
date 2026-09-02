
"""
Author Mit Nargolwala
"""
# Function made by Mit Nargolwala
import bcrypt,os

def sign_up():
    accepted_symbols=["!",".","@","#","$","%","^","&","*","(",")","[","_","]"]
    check_upper=0
    check_lower=0
    check_digit=0
    check_symbol=0
    condition=True

    if not os.path.exists("users.csv"):
        open("users.csv", "w").close()


    userid = input("Input your userid here: ")

    file_1 = open("users.csv", "r")
    lines = file_1.readlines()
    file_1.close()

    while True:
        exists = False
        for line in lines:
            if line.strip().split(",")[0] == userid:
                exists = True
                break

        if exists:
            print("User ID already exists. Please choose another one.")
            userid = input("Input your userid here: ")
        else:
            break


    while condition==True:
        password=input("Input your password here: ")
        if len(password) <6:
            print("Please try again, password should be at least 6 characters long.")
        elif len(password) >=6:
            for character in password:
                if character.isupper() == True:
                    check_upper+=1
                elif character.islower()==True:
                    check_lower+=1
                elif character.isdigit()==True:
                    check_digit+=1
                elif character in accepted_symbols:
                    check_symbol+=1
            if check_upper==0 or check_lower==0 or check_digit==0 or check_symbol==0:
                print("Sorry you must have at least one upper case, at least one lower case, at least one digit and at least one symbol. ")
            else:
                break

    hash_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    file_1 = open("users.csv", "a")
    file_1.write(f"{userid},{hash_pw}\n")
    file_1.close()

    print("Account successfully created and password securely stored!")
sign_up()