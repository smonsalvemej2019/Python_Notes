# Documentation
### Introduction to Python Programming
### Assignment A2: Cryptography With Python
### Florida Atlantic University, Summer 2021

This program is an implementation of the the cesar cypher algorithm using the python file modules.
The program is based on homework a2. Before launching the program, create a .txt file with the message you would like to encrypt or decrypt.

When launched it will give you the following options:

    Encrypt(e)
    Decrypt(d)
    Exit(x)

Then ask you for the file name(***EXTENSION INCLUDED***). The program has a fixed key rotation of 3 so you do not have to worry about inputting a secret key. Your output should be a file in the same directory that follows the following naming conventions:

When encrypting, the filename will be 

    nameOfYourFile_enc.txt

When decrypting, the filename will be 

    nameOfYourFile_dec.txt

I recommend making a file called ***example.txt*** with the message ***!___HellOO from ||| my File??!!***. encrypting it, then decrypting the nameOfYourFile_enc.txt file afterwards. 

***ATTENTION:*** Due to its unique implementation, this program can only decrypt what it encrypts.

### Design Decisions
There is some details about the program that need to be clarified.

1. The program uses the basic ASCII alphabet a-z(65-90) and A-Z(97-122) and not all of UTF-8 nor special ASCII values. 

2. The program does not account for spaces. Any special value, number or space will be left untouched.
3. When encrypting. The ASCII values are visualized as a continuous sequence of letters a - Z; This means whenever there is something greater than Z(122), it will jump back to a(65). The program also takes care of the gap between values z(90) and A(97).

4. The program makes use of python Try-Except. While error handling might be out of the scope of this project, I felt like it was necessary to warn the user when a file cannot be found.

5. The wording used when asking for inputs is simplified. If you take a look, I do not use the word **cypher** in the program because I believe the word itself is a technical term the . I believe the words **Encrypt** and **Decrypt** are more user friendly.