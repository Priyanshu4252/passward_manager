

def add_password():
    username = input("Pls enter your username by which your passward should be stored: ")
    passward = input("Pls enter the passward that you want to save: ")
    database_dictionary = (f"username:{username} | passward:{passward}" + "\n")
    file_path = "C:/VS Code/Pythan/big projects/password_manager/database.txt" 
    with open(file_path, "a") as file : 
        file.write (database_dictionary)

def checkout_password():
    try:
        file_path = "C:/VS Code/Pythan/big projects/password_manager/database.txt"
        with open(file_path, "r") as file :
            database = file.read()
            print(database)
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