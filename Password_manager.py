import os
from cryptography.fernet import Fernet

# Generate and write key if not present
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    with open("key.key","rb") as key_file:
         return key_file.read()
    
# Check if key.key exists, if not, create one
if not os.path.exists("key.key"):
    write_key()
        
# Enter Your master password
# Optional master password check
MASTER_PWD = "mysecret123"
input_pwd = input("Enter master password: ")
if input_pwd != MASTER_PWD:
    print("Wrong password! Exiting.")
    exit()
key = load_key() 
fer = Fernet(key)
 

#User defined function for view and add
def add():
    name = input("Account Name : ")
    password = input("Enter your Password : ")
#with keyword automatically closes the file
    with open("passwords.txt ","a") as f :
        f.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")

def view():
   with open("passwords.txt","r") as f :
        for line in f.readlines():
            #strips the newline
            data = line.rstrip()
            user,pwd = data.split("|")
            print("User : ",user ,"| Password : ",fer.decrypt(pwd.encode()).decode())


#Options
while True :
    mode = input("Enter new Password Or View Previous Ones (view,add) Or q to quit: ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid Input")
        continue