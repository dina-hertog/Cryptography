"""
cryptography.py
Author: Dina
Credit: none

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
command = input("Enter e to encrypt, d to decrypt, or q to quit: ")

while command != 'q':
    while command != 'e' and command != 'd':
        command = input("Did not understand command, try again. ")
    if command == 'e':
        message = input("Message: ")
        key = input("Key: ")
        while len(key) < len(message):
            key = key+key
        km = list(zip(message, key))
        for a in km:
            mnum = associations.find(a[0])
            knum = associations.find(a[1])
            b = mnum+knum
            print(associations[b], end = '')
    else:
        message = input("Message: ")
        key = input("Key: ")
        while len(key) < len(message):
            key = key+key
        km = list(zip(message, key))
        for a in km:
            mnum = associations.find(a[0])
            knum = associations.find(a[1])
            b = mnum-knum
            print(associations[b], end = '')
    print()
    command = input("Enter e to encrypt, d to decrypt, or q to quit: ")
print("Goodbye! ")
"""
message = input("Message: ")
        key = input("Key: ")
        for x in message:
            mnum = associations.find(x)
            for y in key:
                knum = associations.find(y)
            lnum = mnum-knum
            print(associations[lnum], end = '')
"""