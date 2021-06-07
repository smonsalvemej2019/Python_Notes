# Documentation
### Introduction to Python Programming
### Assignment A2: Cryptography With Python
### Florida Atlantic University, Summer 2021

This program is an implementation of the the cesar cypher algorithm.
The program asks the user for an input message and a key (an integer), and will
output a encrypted message(cypher). The program will also decrypt the message if the key
and the cypher are provided. 
When launched, the program will give you the following options:

    Encrypt(e)
    Decrypt(d)
    Exit(x)

These options are pretty self explanatory. I recommend starting by encrypting **Hello World** using the 
key **54** to get the full output of the program (more on this under the Design Decisions section) then decrypting the given cypher afterwards.

***Important:*** All implementations of the cesar cypher are different. This program can only
decrypt what it encrypts.

### Design Decisions
There is some details about the program that need to be clarified.

1. The program uses some ASCII(32 - 126) and not all of UTF-8. This is was a conscious design decision that I made to keep the program simple.
2. The program accounts for spaces in the input and output. The outputs are highlighted to better see these spaces and will give a warning whenever there is a space present in the output cypher.
3. The program makes use of python Try-Except. While error handling might be out of the scope of this project, I felt like it was necessary.
4. The wording used when asking for inputs is simplified. If you take a look, I do not use the word **cypher** in the program because I believe the word itself is a technical term the . I believe the words **Encrypt** and **Decrypt** are more user friendly.