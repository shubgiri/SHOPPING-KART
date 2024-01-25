import random
import sys


def validate_user(email, password):
    return email == "sg@gmail.com" and password == "12345"


mail = input("Enter email id:")
pas = input("Enter password:")

if not validate_user(mail, pas):
    print("Invalid email or password\U0001F611")
    sys.exit()

product = input("Enter product:")
amt = int(input("Enter amount:"))
amazondis = 10
flipkartdis = 20
myntradis = 30
boi = 100500
sbi = 200500
bob = 500500
pe = input('''1.googlepay [BOI]
2.phonepe [SBI]
3.paytm [BOB]
select your payment method: ''')

if pe not in {"1", "2", "3"}:
    print("Invalid payment method")
    sys.exit()

if amt > boi and sbi and bob:
    print("Insufficient Balance\U0001F641")
    sys.exit()

#################otp generation#######################

def genrate_otp():
    otp = random.randint(1111, 9999)
    return otp

def validate_otp(user_input, genrated_otp):
    if user_input == genrated_otp:
        print("otp is valid")
        print("amount deducted:", amt)
        lowdis = max(amazondis, flipkartdis, myntradis)
        if lowdis == amazondis:
            print("you got discount from amazon", lowdis, "%")
        elif lowdis == flipkartdis:
            print("you got discount from flipkart", lowdis, "%")
        elif lowdis == myntradis:
            print("you got discount from myntra", lowdis, "%")
            if pe == "1":
                print("remaining balance is:", boi - amt - lowdis)
            if pe == "2":
                print("remaining balance is:", sbi - amt - lowdis)
            if pe == "3":
                print("remaining balance is:", bob - amt - lowdis)
    else:
        print("invalid otp")

genrated_otp = genrate_otp()
print("your otp is:", genrated_otp)

user_input = int(input("Enter otp:"))
validate_otp(user_input, genrated_otp)

if mail == "sg@gmail.com" and pas == "12345":
    if user_input == genrated_otp:
        print("thanks for shopping\U0001F603")
    else:
        print("purchase cancelled\U0001F641")
