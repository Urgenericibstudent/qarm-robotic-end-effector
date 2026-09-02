# ============================================================
#  TEAM PROJECT – MAIN WAREHOUSE ORDERING SYSTEM
#  All functions integrated exactly as student provided,
#  with minimal fixes only where required.
# ============================================================

import bcrypt, os, random
from time import sleep

# ============================================================
##  Q-ARM INTERFACE SETUP
# ============================================================

from Common.qarm_interface_wrapper import *
GRIPPER_IMPLEMENTATION = 1
arm = QArmInterface(GRIPPER_IMPLEMENTATION)
scan_barcode = BarcodeScanner.scan_barcode


# ============================================================
##  Sign_Up Function (By Mit Nargolwala)
# ============================================================

def sign_up():

    accepted_symbols=["!",".","@","#","$","%","^","&","*","(",")","[","_","]"]

    if not os.path.exists("users.csv"):
        open("users.csv", "w").close()

    userid = input("Input your userid here: ")

    file_1 = open("users.csv", "r")
    lines = file_1.readlines()
    file_1.close()

    # ensure unique userid
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

    # password creation
    while True:
        check_upper = 0
        check_lower = 0
        check_digit = 0
        check_symbol = 0

        password = input("Input your password here: ")

        if len(password) <6:
            print("Please try again, password should be at least 6 characters long.")
            continue

        for character in password:
            if character.isupper():
                check_upper+=1
            elif character.islower():
                check_lower+=1
            elif character.isdigit():
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


# ============================================================
## Authenticate Function (By Andy Zhang)
# ============================================================

def authenticate():

    while True:

        loggin_approve = 0
        Re_user_id = None

        account = input("Do you have an account please enter yes or no: ")

        if account.lower() == "yes":

            users_id = input("Enter user id: ")
            password = input("Enter user password: ")

            users_file = open("users.csv")

            for line in users_file:

                hash = line.split(",")[1].rstrip("\n")

                if line.split(",")[0] == users_id and bcrypt.checkpw(password.encode('utf-8'), hash.encode('utf-8')):

                    print("Successfully logged in.")
                    Re_user_id = users_id
                    loggin_approve = 1
                    break

            users_file.close()

            if not Re_user_id:
                print("your id or password is missmatched.")

        elif account.lower() == "no":
            sign_up()

        elif account.lower() == "exit":
            return ""

        else:
            print("Invalid input, please try again.")

        if loggin_approve:
            break

    return Re_user_id


# ============================================================
## LookUp Products by Ryan Alaskari
# ============================================================

def lookup_products(products):

    matched_products = []

    product_names = products.split(",")
    for i in range(len(product_names)):
        product_names[i] = product_names[i].strip()

    try:
        file = open("products.csv", "r")
    except FileNotFoundError:
        print("Error: products.csv file not found.")
        return matched_products

    lines = file.readlines()
    file.close()

    for name in product_names:
        if name == "":
            continue

        found = False

        for line in lines:
            line = line.strip()
            if line == "":
                continue

            parts = line.split(",")
            if len(parts) < 2:
                continue

            csv_name = parts[0].strip()
            price_str = parts[1].strip()

            if name == csv_name:
                price = float(price_str)
                matched_products.append([csv_name, price])
                found = True
                break

        if not found:
            print("Warning:", name, "not found in products.csv")

    return matched_products


# ============================================================
##  Complete Order by Zaid Din
# ============================================================

def complete_order(userid, product_list):
    if not product_list:
        print("No products in the order.")
        return

    tax_rate = 0.13
    discount = random.randint(5, 50)

    subtotal = 0
    for item in product_list:
        subtotal += float(item[1])
    discount_amount = subtotal * discount / 100
    tax_amount = (subtotal - discount_amount) * tax_rate
    total = subtotal - discount_amount + tax_amount

    print("\n====================================")
    print("          STORE RECEIPT")
    print("====================================")
    print(f"Customer: {userid}")
    print("------------------------------------")
    for item in product_list:
        name = item[0]
        price = float(item[1])
        print(f"{name:<25} ${price:>7.2f}")
    print("------------------------------------")
    print(f"{'Subtotal:':<25} ${subtotal:>7.2f}")
    print(f"Discount ({discount}%):".ljust(25) + f"-${discount_amount:>7.2f}")
    print(f"{'Tax (13%):':<25} +${tax_amount:>7.2f}")
    print("------------------------------------")
    print(f"{'TOTAL:':<25} ${total:>7.2f}")
    print("====================================\n")

    row = userid + "," + f"{total:.2f}"
    for item in product_list:
        row += "," + item[0]

    file = open("orders.csv", "a")
    file.write(row + "\n")
    file.close()

    order_count = 0
    file = open("orders.csv", "r")
    for line in file:
        parts = line.strip().split(",")
        if parts[0] == userid:
            order_count += 1
    file.close()

    print(f"You have placed {order_count} order(s) so far.")


# ============================================================
## Customer Summary by Darshan Daxini
# ============================================================

def customer_summary(user_id):

    if not os.path.exists("orders.csv"):
        print("No order history found.")
        return

    product_counts = {}
    total_orders = 0
    total_cost = 0.0

    f = open("orders.csv", "r")

    for line in f:
        parts = line.strip().split(",")

        if len(parts) < 2:
            continue
        if parts[0] != user_id:
            continue

        try:
            cost = float(parts[1])
        except ValueError:
            continue

        total_orders += 1
        total_cost += cost

        # count real product names
        for item in parts[2:]:
            product_counts[item] = product_counts.get(item, 0) + 1

    f.close()

    print("=" * 36)
    print(f"Customer Summary for User: {user_id}")
    print("-" * 36)
    print(f"Total Orders: {total_orders:20.0f}")
    print(f"Total Spent: ${total_cost:18.2f}")
    print("-" * 36)
    print("Product Summary")

    for product, count in product_counts.items():
        print(f"{product}: {count}")

    print("=" * 36)


# ============================================================
#  Pack Products by Team
# ============================================================

def pack_products(product_list):

    for item in product_list:
        name = item[0]

        # your exact movement code preserved
        if name == "Sponge":
            arm.home()
            arm.rotate_base(20)
            arm.rotate_elbow(-12)
            arm.rotate_shoulder(45)
            arm.home()
            arm.rotate_base(-55)
            arm.rotate_elbow(20)

        elif name == "Bottle":
            arm.home()
            arm.rotate_base(14)
            arm.rotate_elbow(-12)
            arm.rotate_shoulder(45)
            arm.home()
            arm.rotate_base(-55)
            arm.rotate_elbow(20)

        elif name == "Rook":
            arm.home()
            arm.rotate_elbow(-12)
            arm.rotate_base(7)
            arm.rotate_shoulder(50)
            sleep(5)
            arm.home()
            arm.rotate_base(-55)
            arm.rotate_elbow(20)

        elif name == "D12":
            arm.home()
            arm.rotate_elbow(-12)
            arm.rotate_base(-5)
            arm.rotate_shoulder(50)
            sleep(5)
            arm.home()
            arm.rotate_base(-55)
            arm.rotate_elbow(20)

        elif name == "WitchHat":
            arm.home()
            arm.rotate_elbow(-12)
            arm.rotate_base(-9)
            arm.rotate_shoulder(50)
            sleep(5)
            arm.home()
            arm.rotate_base(-55)
            arm.rotate_elbow(20)

        elif name == "Bowl":
            arm.home()
            arm.rotate_elbow(-15)
            arm.rotate_base(-16)
            arm.rotate_shoulder(51)
            sleep(5)
            arm.home()
            arm.rotate_base(-55)
            arm.rotate_elbow(20)

    arm.home()  # reset when done


# ============================================================
#  MAIN FUNCTION by Team
# ============================================================

def main():

    print("=========================================")
    print("   WELCOME TO THE WAREHOUSE SYSTEM")
    print("=========================================")

    user = authenticate()
    if user == "":
        print("Exiting system.")
        return

    while True:

        print("\nScan items now (use barcode scanner).")
        scanned = scan_barcode()  # returns one string

        print("Scanned:", scanned)

        product_list = lookup_products(scanned)

        if not product_list:
            print("No valid products scanned.")
            continue

        print("\nPacking products...")
        pack_products(product_list)

        print("\nCompleting order...")
        complete_order(user, product_list)

        again = input("Process another order? (yes/no): ").lower()
        if again != "yes":
            break

    print("\nFINAL CUSTOMER SUMMARY:")
    customer_summary(user)

    arm.end_arm_connection()
    print("System closed. Goodbye!")




if __name__ == "__main__":
    main()
