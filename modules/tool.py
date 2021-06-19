from termcolor import colored
import hashlib
from os import system, name
import qrcode
from PIL import Image
def home():
    x=0
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
        print(colored("0        Quite                    Exist tool", 'red', attrs=['bold']))
        print()
        tool = input(colored("Select an Option : ", 'blue'))
    else:
        clear()
        tool = invoke

    if tool == '0':
        quit("Good By Horse....")

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

    else:
        clear()
        print("Option Unknown")
        tool = input(colored("Select an Option : ", 'blue'))
        anton(tool)


anton()
