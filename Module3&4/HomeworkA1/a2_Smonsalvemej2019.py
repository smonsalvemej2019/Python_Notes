#Assignmen 2
#Introduction to Python programming
#Summer 2021


while 1:
    #options menu, input is converted to lowercase
    option = input("\nEncrypt(e)\nDecrypt(d)\nExit(x)\n")
    option = option.lower()

    #if else statements 

    #exiting the program
    if option == 'x': break 
    #encryption
    elif option == 'e':
        
        #try block is to prevent the user from inputing letters as key values
        try:
            #Input variables
            my_string = input("Insert a word or sentence to be encrypted: ")
            my_key = int(input("Insert your displacement value(must be an integer): "))
            my_secret = str()
            #check if input key is a negative number
            if my_key < 0: my_key *= -1 

            #turns the strings to ASCII values and moves those values to the my_ascii list
            my_ascii = []
            for letter in my_string:
                my_ascii.append(ord(letter))

            #this nested loops do the displacement of the values
            for x in range(my_key+1):
                i = 0
                for entry in my_ascii:
                    if entry == 126:
                        my_ascii[i] = 32
                        i += 1
                        continue
                    my_ascii[i] += 1
                    i += 1

            #this loop will turn the list into a string 
            #it will also check for empty spaces. An empty space will proc the warning message
            empty_spaces = 0
            for val in my_ascii:
                my_secret += str(chr(val))
                if str(chr(val)) == " ":
                    empty_spaces += 1

            #output and warning messages 
            if empty_spaces > 0: print("\n\x1b[0;30;41m" + " ATTENTION: SPACES IN THE ENCRYPTED STRING MUST BE CONSERVED " + "\x1b[0m\n")
            print("\nYour key is: " + "\x1b[0;30;42m"+"   "+ str(my_key) + "   "+ "\x1b[0m")
            print("Your encrypted string is: " + "\x1b[0;30;42m" + my_secret + "\x1b[0m")

        #the except block will watch the errors from the try block
        except ValueError:
            print("\n"+ "\x1b[0;30;41m" +"ERROR: Displacement value must be an integer" + "\x1b[0m")
            continue

    #decryption
    elif option == "d":
        #try block is to prevent the user from inputing letters as key values
        try:
            #Input variables
            my_string = input("Insert your encrypted word:\n")
            my_key = int(input("Insert your encryption key(must be an integer): "))
            my_secret = str()
            #check if input key is a negative number
            if my_key < 0: my_key *= -1 

            #turns the strings to ASCII values and moves those values to the my_ascii list
            my_ascii = []
            for letter in my_string:
                my_ascii.append(ord(letter))

            #this nested loops do the displacement of the values
            for x in range(my_key+1):
                i = 0
                for entry in my_ascii:
                    if entry == 32:
                        my_ascii[i] = 126
                        i += 1
                        continue
                    my_ascii[i] -= 1
                    i += 1

            #this loop will turn the list into a string 
            for val in my_ascii:
                my_secret += str(chr(val))

            #output
            print("\nYour key is: " + "\x1b[0;30;42m"+"   "+ str(my_key) + "   "+ "\x1b[0m")
            print("Your decrypted message is: " + "\x1b[0;30;42m" + my_secret + "\x1b[0m")

        #the except block will watch the errors from the try block
        except ValueError:
            print("\n"+ "\x1b[0;30;41m" +"ERROR: Key must be an integer" + "\x1b[0m")
            continue
    
    #notify the user if their menu option is invalid
    else:
        print("\n\x1b[0;30;41m" + " ATTENTION: INVALID OPTION " + "\x1b[0m\n")
