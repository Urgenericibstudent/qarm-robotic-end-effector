"""
Author Mit Nargolwala
The purpose of this program is to create a secure user account system that allows new users to sign up with a unique user ID and a strong password. The program checks that the password meets specific security requirements, hashes the password using bcrypt for safe storage, and then saves the user ID and hashed password into a CSV file. This ensures that user credentials are stored securely and that duplicate user IDs cannot be created.

"""
# Function made by Mit Nargolwala

# Import modules
import bcrypt, os

def sign_up():
    """
    This function creates a new user account by collecting a unique user ID and a password and then hashing the password using bcrypt. There are no paremters or return values
    """

    # This list features the special characters that are allowed in the password
    accepted_symbols = ["!", ".", "@", "#", "$", "%", "^", "&", "*", "(", ")", "[", "_", "]"]

    # Create file users.csv if it doesn't exist
    if not os.path.exists("users.csv"):
        open("users.csv", "w").close()

    #Takes userid from usee
    userid = input("Input your userid here: ")

    # Opens user.csv in read mode
    with open("users.csv", "r") as file_1:
        # Load every line from users.csv so we can check existing user IDs
        lines = file_1.readlines()

    # This while loop will run in order to check every line if there is already a similar userid in the csv file

    while True:
        # Sets up condition
        exists = False
        # This for loop will iterate through each line
        for line in lines:
           # Extract the userid from the line (before the comma) and compare it to the new userid
            if line.strip().split(",")[0] == userid:

                # If it matches, mark that the userid already exists
                exists = True
                break
         # If the userid was found in the file, that being True then it will display error message and allow user to input another userid
        if exists:
            print("User ID already exists. Please choose another one.")
            userid = input("Input your userid here: ")
        else:
            break

    ## Password Creation

    # This will loopp until a valid password is entered
    while True:

        # Creates requirement counters to ensure password fits requirements, this in the while loop to reset the values for each new password attempt
        check_upper = 0
        check_lower = 0
        check_digit = 0
        check_symbol = 0

        # Asks user to enter password
        password = input("Input your password here: ")

        # If the length of the password string is less than 6, it will print an error message
        if len(password) < 6:
            print("Please try again, password should be at least 6 characters long.")

            # This code will still continue and go back to the password input code
            continue



        # This for loop iterates through each character in password to check each character to see if it meets the password requirement
        for character in password:
            # Count if character is an uppercase letter
            if character.isupper():
                check_upper += 1
            # Count if character is a lowercase letter
            elif character.islower():
                check_lower += 1
            # Count if character is a digit
            elif character.isdigit():
                check_digit += 1

            # Count if character is in the list of accepted symbols
            elif character in accepted_symbols:
                check_symbol += 1

        # If any of the requirements are missing and do not have at least 1 of each requirement, then it will notify the user and go  back to the beginning of the loop
        if check_upper == 0 or check_lower == 0 or check_digit == 0 or check_symbol == 0:
            print("Sorry, you must have at least one upper case, one lower case, one digit, and one symbol.")
        else:
            # password fits all requirements and therefore exits loop
            break

    ## Store User Information and Encryption
    #Encrypt password using bcrypt
    hash_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    # Opens user.csv in append mode
    with open("users.csv", "a") as file_1:
        # Writes the new userid and hashed password
        file_1.write(f"{userid},{hash_pw}\n")


    # Outputs that account has successfully been created
    print("Account successfully created and password securely stored!")

# Runs function
sign_up()
