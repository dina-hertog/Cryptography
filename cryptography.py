"""
cryptography.py
Author: Dina
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

command = input("Enter e to encrypt, d to decrypt, or q to quit: ")
while command != 'e' and command != 'd' and command != 'q':
    print("Did not understand command, try again.")
    command = input("Enter e to encrypt, d to decrypt, or q to quit: ")