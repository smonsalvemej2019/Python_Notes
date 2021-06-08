#Assignmen 2
#Introduction to Python programming
#Summer 2021

#function definitions


#encryption function
def encrypt():
    #try block is to prevent the user from inputing letters as key values
    try:
        #Input variables
        filename = input("Insert the name of the file you wish to encrypt(extension included): ")
        file = open(filename)
        my_string = file.read()
        file.close()
        my_key = 3
        my_secret = str()

        #turns the strings to ASCII values and moves those values to the my_ascii list
        my_ascii = []
        for letter in my_string:
            my_ascii.append(ord(letter))

        #this nested loops do the displacement of the values
        for x in range(my_key+1):
            i = 0
            for entry in my_ascii:
                if entry == 122:
                    my_ascii[i] = 65
                    i+=1
                    continue
                elif entry == 90:
                    my_ascii[i] = 97
                    i+=1
                    continue
                elif entry > 122 or entry < 65 or (entry > 90 and entry < 97):
                    i +=1
                    continue
                else:
                    my_ascii[i] += 1
                    i += 1

        #this loop will turn the list into a string 
        for val in my_ascii:
            my_secret += str(chr(val))

        #output
        filename = filename.replace(".txt","")
        filename = filename.replace("_dec","")
        filename = filename.replace("_enc","")
        file = open(filename + "_enc.txt", "w")
        file.write(my_secret)
        file.close()

        #output message
        print("\n" + "\x1b[0;30;42m" + "Your encrypted message has been added to " + filename + "_dec.txt" + "\x1b[0m")
    #the except block will watch the errors from the try block
    except OSError:
        print("\n"+ "\x1b[0;30;41m" +"ERROR: File to encrypt not found" + "\x1b[0m")
        return

def decrypt():
    #try block is to prevent the user from inputing letters as key values
    try:
        #Input file name
        filename = input("Insert the name of the file you wish to deccrypt(extension included): ")
        #open, read, close
        file = open(filename)
        my_string = file.read()
        file.close()
        #key variable and output variable
        my_key = 3
        my_secret = str()

        #turns the strings to ASCII values and moves those values to the my_ascii list
        my_ascii = []
        for letter in my_string:
            my_ascii.append(ord(letter))

        #this nested loops do the displacement of the values
        for x in range(my_key+1):
            i = 0
            for entry in my_ascii:
                if entry == 65:
                    my_ascii[i] = 122
                    i+=1
                    continue
                elif entry == 97:
                    my_ascii[i] = 90
                    i+=1
                    continue
                elif entry > 122 or entry < 65 or (entry > 90 and entry < 97):
                    i +=1
                    continue
                else:
                    my_ascii[i] -= 1
                    i += 1

        #this loop will turn the list into a string 
        for val in my_ascii:
            my_secret += str(chr(val))

        #output
        filename = filename.replace(".txt","")
        filename = filename.replace("_dec","")
        filename = filename.replace("_enc","")
        file = open(filename + "_dec.txt", "w")
        file.write(my_secret)
        file.close()



        print("\n" + "\x1b[0;30;42m" + "Your decrypted message has been added to " + filename + "_dec.txt" + "\x1b[0m")
    #the except block will watch the errors from the try block
    except OSError:
        print("\n"+ "\x1b[0;30;41m" +"ERROR: File to decrypt not found" + "\x1b[0m")
        return


#main while loop
while 1:
    #options menu, input is converted to lowercase
    option = input("\nEncrypt(e)\nDecrypt(d)\nExit(x)\n")
    option = option.lower()

    #if else statements 

    #exiting the program
    if option == 'x': break 
    #encryption
    elif option == 'e':
        encrypt()
    #decryption
    elif option == "d":
        decrypt()
        
    #notify the user if their menu option is invalid
    else:
        print("\n\x1b[0;30;41m" + " ATTENTION: INVALID OPTION " + "\x1b[0m\n")

