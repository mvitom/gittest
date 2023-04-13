from cryptography.fernet import Fernet


def write_key():
    key = Fernet.generate_key() # Generates the key
    with open("key.key", "wb") as key_file: # Opens the file the key is to be written to
        key_file.write(key) # Writes the key





# tady chci precist pouze jeden radek ne cely text

def load_key():
    return open("key.key", "rb").read() #Opens the file, reads and returns the key stored in the file

#message = input("Message: ").encode() # Takes the message as user input and encodes it


# key = load_key()
# fer = Fernet(key)
# encrypted_message = f.encrypt(message) #encrypt
# print(encrypted_message)
# decrypted_message = f.decrypt(encrypted_message) #decrypt
# print(decrypted_message)


def add():
    name = input("Uzivatelsle jmeno: ")
    password = input("Heslo: ").encode()
    key = load_key()
    fer = Fernet(key)
    e_passw = fer.encrypt(password)
    with open("passwords.txt", "a") as f:
        f.write(name + "#" + e_passw.decode() + "\n")
        #print(fer.decrypt(e_passw))

def view():
    with open("passwords.txt", "r") as f:
        #if len(f.read())<1:
            #return print("žádné uložené účty")
        #else:
            for line in f.readlines():
                data = line.rstrip()
                user, passw = data.split("#")
                key = load_key()
                fer = Fernet(key)
                print("User:",user,"Password:",
                    fer.decrypt(passw.encode()))
        
    
  
            
