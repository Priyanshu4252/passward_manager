
default_key = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c',
'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 
'D','E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
'Q','R','S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#',
'$','%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':',
';','<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{',
'|','}', '~']

encrypted_key = ['8', '1', '0', '?', '}', '[', '>', 'z', '/', 'W', 'i', 
'T', 'e', 'y', '-', 'R', 'o', '"', 'f', 'Y', '{', 'Q', 
'O', 'I', 'K', '=', 'S', 'U', '~', 'u', 'F', 'B', '$', 
'`', '|', '9', 'N', '+', '&', 'C', '#', 'H', '@', '_', 
'm', ']', '7', 'q', '<', 'X', 'E', 'x', 'a', 'r', '%', 
'D', '3', '\\', 'j', 'J', 'P', 'p', 'V', '!', 'Z','l', 
'c', 'A', 'M', 'k', ':', "'", '4', 'w', ',', '^', '2', 
'L', ';', 's', 'G', 'b', 'v', ')', '5', '6', 'g', '.', 
'(', 'd', 'h', 'n', 't', '*']

def add_password():
    username = input("Pls enter your username by which your passward should be stored: ")
    password = input("Pls enter the passward that you want to save: ")
    list_password = []
    for letter in password:
        a = default_key.index(letter)
        b = encrypted_key[a]  #change syntax
        list_password.append(b)
    q = "".join(list_password)

    database_dictionary = (f"{username} | {q}" + "\n")
    file_path = "database.txt" 
    with open(file_path, "a") as file : 
        file.write (database_dictionary)

def checkout_password():
    decrypting_password_list= []
    try:
        file_path = "database.txt"
        with open(file_path, "r") as file :
            database = file.read()
            print(database)
            decrypting_password = input("Pls copy and paste the password here that you want to see: ")
            for char in decrypting_password:
                x = encrypted_key.index(char)
                y= default_key[x]
                decrypting_password_list.append(y)
                q = "".join(decrypting_password_list)
            print(f"your password is {q}")


    except FileNotFoundError :
         print ("file location not found")

def main():
    chances = 0 
    key = "123"
    is_running = True
    
    while is_running:
        print ("WELCOME TO THE PYTHON PASS WARD MANAGER")
        human_key = input ("Enter the key to access the passward manager: ")
        chances += 1 
        if human_key == key :
            is_running = False
            print("welcome")
            print("What do you want to do?")
            print("press 1 to add new passward" )
            print("press 2 to see existing passward")
            human_option = input ("enter your option (1/2)")
            if human_option.isdigit():
                human_option = int(human_option)
                if human_option == 1  :
                    add_password()
                    
                elif human_option == 2:
                    checkout_password()
                    
                else :
                    print("ERROR")
                    print("invalid option")
                    
            else :
                print ("ERROR")
                print ("Pls enter a numarical value")
                
                
        elif chances == 3 :
            print ("you are LOCKED ")
            print ("try again later")
            is_running = False
        else :
            print ("your input does't match the key")
            print ("TRY AGAIN")
            print (f"you have {3 - chances} left")
            
    

    

if __name__ == "__main__":
    main()
