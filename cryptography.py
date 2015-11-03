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
    while command != 'e' and command != 'd' and command != 'q':
        command = input("Did not understand command, try again. ")
    if command == 'e' or command == 'd':
        message = input("Message: ")
        key = input("Key: ")
        while len(key) < len(message):
            key = key+key
        km = list(zip(message, key))
        for a in km:
            mnum = associations.find(a[0])
            knum = associations.find(a[1])
            if command == 'e':
                b = mnum + knum
                if b > len(associations):
                    b = b-len(associations)
            else:
                b = mnum - knum
                if b < 0:
                    b = b + len(associations)
            print(associations[b], end = '')
    #print()
    if command != 'q':
        command = input("Enter e to encrypt, d to decrypt, or q to quit: ")
print("Goodbye!")