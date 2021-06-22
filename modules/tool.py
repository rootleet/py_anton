import datetime

from termcolor import colored
import hashlib
from os import system, name
import qrcode
from PIL import Image
import re
import string


def home():
    x = 0
    while x < 4:
        y = x
        print(colored("01" * 9, 'grey', 'on_red'), colored("               ", 'grey', 'on_red'),
              colored("01" * 9, 'grey', 'on_red'))
        x = y + 1

    print(colored("01" * 9, 'grey', 'on_yellow'),
          colored("               ", 'red', 'on_yellow'),
          colored("01" * 9, 'grey', 'on_yellow'))

    print(colored("01" * 9, 'grey', 'on_yellow'),
          colored("               ", 'grey', 'on_yellow'),
          colored("01" * 9, 'grey', 'on_yellow'))

    print(colored("01" * 9, 'grey', 'on_yellow'),
          colored("  ANTON V0.0   ", 'grey', 'on_yellow', attrs=['bold']),
          colored("01" * 9, 'grey', 'on_yellow'))

    print(colored("01" * 9, 'grey', 'on_yellow'),
          colored("               ", 'grey', 'on_yellow'),
          colored("01" * 9, 'grey', 'on_yellow'))

    print(colored("01" * 9, 'grey', 'on_yellow'),
          colored("               ", 'grey', 'on_yellow'),
          colored("01" * 9, 'grey', 'on_yellow'))

    x = 0
    while x < 4:
        y = x
        print(colored("01" * 9, 'grey', 'on_green'),
              colored("               ", 'grey', 'on_green'),
              colored("01" * 9, 'grey', 'on_green'))
        x = y + 1
    print()
    print(('-' * 50))
    print()


def make_md5(my_string):
    m = hashlib.md5()
    m.update(my_string.encode('utf-8'))
    return m.hexdigest()


# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def anton(invoke='None'):
    if invoke == "None":
        home()
        print(colored("Trigger  Name                    Description", 'red', "on_blue", attrs=['bold']))
        print()
        print(colored("1        Make Qr Code             Make QR Code that contains data", 'red', attrs=['bold']))
        print(colored("2        vigenere cipher          A python code that performs a Vigenere cipher.", 'red',
                      attrs=['bold']))
        print(colored("0        Quite                    Exist tool", 'red', attrs=['bold']))
        print()
        tool = input(colored("Select an Option : ", 'blue'))
    else:
        clear()
        tool = invoke

    # exit
    if tool == '0':
        quit("Good By Horse....")
    # qr code
    elif tool == '1':
        clear()
        import qrcode
        import datetime
        print("1    Text Date ")
        print("2    Url Date")
        print("3    Go Back")
        qrcode_option = input("Option : ")
        if qrcode_option == '1':
            img = qrcode.make(input('Your input text : '))
        elif qrcode_option == '2':
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=1,
            )
            qr.add_data(input("url : "))
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

        elif qrcode_option == '3':
            anton()

        else:
            clear()
            anton("x")
        curr_time = make_md5(str(datetime.datetime.now()))
        img.save("assets/qr_images/" + str(curr_time) + ".png")
        print("image file saved as ", curr_time)
        anton()

    elif tool == 'x':
        clear()
        anton("None")
    # Vigenere cipher.
    elif tool == '2':
        vigenere_cipher()
    else:
        clear()
        print("Option Unknown")
        tool = input(colored("Select an Option : ", 'blue'))
        anton(tool)


# vizier cypher
def vigenere_cipher():
    alphabets = "abcdefghijklmnopqrstuvwxyz"  # this is the english letters

    def encrypt(p, k):
        c = ""
        kpos = []  # return the index of characters ex: if k='d' then kpos= 3
        for x in k:
            # kpos += alphabets.find(x) #change the int value to string
            kpos.append(alphabets.find(x))
        i = 0
        for x in p:
            if i == len(kpos):
                i = 0
            pos = alphabets.find(x) + kpos[
                i]  # find the number or index of the character and perform the shift with the key
            # print(pos)
            if pos > 25:
                pos = pos - 26  # check you exceed the limit
            c += alphabets[pos].capitalize()  # because the cipher text always capital letters
            i += 1
        func = "Encrypt"
        plain_text = p
        key = k
        encrypted = c
        print("#" * 10, "\nFunction : ", func, "\nMessage : ", plain_text, "\nKey : ", key, "\nEncryption : ",
              encrypted)
        result = "###### Function : " +str(func) + " Message : " + str(plain_text) + " Key : " + str(
            key) + " Encryption : " + str(encrypted) + "\n"
        print("#" * 10)
        f = open("assets/encryptions/encrypt.txt", "a+")
        f.write(str(result))
        f.close()
        return c

    def decrypt(c, k):
        p = ""
        kpos = []
        for x in k:
            kpos.append(alphabets.find(x))
        i = 0
        for x in c:
            if i == len(kpos):
                i = 0
            pos = alphabets.find(x.lower()) - kpos[i]
            if pos < 0:
                pos = pos + 26
            p += alphabets[pos].lower()
            i += 1
        return p

    try:
        print("Welcome to vigenere cipher.\n\n"
              "The text message should contain only characters and the key should be one character word \n"
              "Press 1 to Enrypt a message \npress 2 to Decrypt a message \npress 0 to return home")
        choose = input("Choice: ")
        if choose == '1':
            p = input("enter the plain text: ")
            p = p.replace(" ", "")  # this will make sure that there is no space in the message
            if p.isalpha():
                k = input("Enter the key: ")
                k = k.strip()  # remove the white spaces from both sides
                if k.isalpha():
                    # print(k)
                    c = encrypt(p, k)
                    vigenere_cipher()

                else:
                    print(k)
                    print("Enter valid key, key is only one character word!")
            else:
                print("only letters are allowed !!")

        elif choose == '2':
            c = input("enter the cipher text: ")
            c = c.replace(" ", "")
            if c.isalpha():
                k = input("Enter the key: ")
                if not k.isalpha():
                    print("Enter valid key, key is only one character word!")
                else:
                    p = decrypt(c, k)
                    print("The plain text is: ", p)
            else:
                print("only letters are allowed!")

        elif choose == '0':
            anton()
        else:
            print("Please enter a valid choice!")
    except Exception as e:
        print(e)
        exit("Enter a valid text please! ")


anton()
