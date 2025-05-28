#TASK2
#password generator
import random 
import string
def generate_password(length):
    if length < 4:
        print("Password Length should ber at least 4 characters.")
        return None

    lower=string.ascii_lowercase
    upper=string.ascii_uppercase
    digits=string.digits
    symbols=string.punctuation
    password=[
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    all_chars=lower+ upper + digits + symbols
    password +=random.choices(all_chars,k=length-4)
    random.shuffle(password)
    return ''.join(password)

def display_password(password):
    if password :
        print(f"Generated Password :{password}")
try:
    user_input= int(input("Enter the desired password length: "))
    pwd= generate_password(user_input)
    display_password(pwd)
except ValueError:
    print("Please enter a valid number.")
	
	
OUTPUT(PassWord Manager)
Enter the desired password length: 4
Generated Password :3B\l
