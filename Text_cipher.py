import string

def encryption(messages,chars,key):
 encrypted = ""
 for index in messages:
     postion = chars.index(index)
     encrypted += key[postion]
 return encrypted

def decryption(messages,chars,key):
 decrypted = ""
 for index in messages:
     postion = key.index(index)
     decrypted += chars[postion]
 return decrypted
    
def main():   
    
 chars = ' '+ string.punctuation + string.digits + string.ascii_letters
 chars = list(chars)
 key = ['G', 't', '+', '`', 'v', 'E', '=', '.', 'H', '@', 'b', 'X', ')', 'j', 'e', '6', '}', '7', 'r', 'L',
        'm', '4', '5', '3', 'J', ':', 'q', '&', '{', '(', 'd', ',', '$', 'g', '*', 'Z', 'T', 'o', 'l', 'C',
        '-', '"', 'V', 'M', 'D', 'i', '2', 'y', '1', 'p', 'z', '^', '~', 'N', '%', 'S', 'c', '!', 'K', 'R', 
        '<', '_', '9', 's', 'k', 'A', 'P', '0', "'", 'I', 'n', 'f', 'h', 'W', 'Y', '|', '>', '#', '?', ']', 
        'U', 'w', ' ', ';', 'B', '\\', 'x', '[', '/', 'O', 'F','a', '8', 'Q', 'u']
 
 print("🔥🔥🔥🔥🔥🔥🔥🔥Welcome to the encryption and decryption program!🔥🔥🔥🔥🔥🔥🔥🔥")
 print("------------------------------------------------------------------------------------------------")
 while True:
     print("What do you want to do?")
     print("1. encryption")
     print("2. decryption")
     print("3. exit")
     choice = input("Enter your choice: ")

     if choice == "1":
        messages = input("Enter the message you want to encrypt: ")
        encrypt = encryption(messages, chars, key)
        print(f"Encrypted message: {encrypt}")

     elif choice == "2":
        messages = input("Enter the message you want to decrypt: ")
        decrypt = decryption(messages, chars, key)
        print(f"Decrypted message: {decrypt}")

     elif choice == "3":
        break
     
     else:
        print("Enter a valid choice 🫵")
        
if __name__ == "__main__":
   main()