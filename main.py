import sqlite3
from termcolor import colored
import getpass

conn = sqlite3.connect('test.db')
x = 0
# while x < 4:
#     y = x
#     print(colored("01" * 15, 'grey', 'on_red'), colored("                                      ", 'grey', 'on_red'),
#           colored("01" * 15, 'grey', 'on_red'))
#     x = y + 1
#
# print(colored("01" * 15, 'grey', 'on_yellow'), colored("                                      ", 'red', 'on_yellow'),
#       colored("01" * 15, 'grey', 'on_yellow'))
#
# print(colored("01" * 15, 'grey', 'on_yellow'), colored("                                      ", 'grey', 'on_yellow'),
#       colored("01" * 15, 'grey', 'on_yellow'))
#
# print(colored("01" * 15, 'grey', 'on_yellow'), colored("              ANTON V0.0              ", 'grey', 'on_yellow', attrs=['bold']),
#       colored("01" * 15, 'grey', 'on_yellow'))
#
# print(colored("01" * 15, 'grey', 'on_yellow'), colored("                                      ", 'grey', 'on_yellow'),
#       colored("01" * 15, 'grey', 'on_yellow'))
#
# print(colored("01" * 15, 'grey', 'on_yellow'), colored("                                      ", 'grey', 'on_yellow'),
#       colored("01" * 15, 'grey', 'on_yellow'))
#
# x = 0
# while x < 4:
#     y = x
#     print(colored("01" * 15, 'grey', 'on_green'), colored("                                      ", 'grey', 'on_green'),
#           colored("01" * 15, 'grey', 'on_green'))
#     x = y + 1

print()

login = False


# Validate Username


# validate username
def validate_user():
    user_name = input("Username : ")
    cursor = conn.execute("SELECT * from `users` WHERE `username` = " + "'" + str(user_name) + "'")
    user_exist = len(list(cursor))

    if user_exist == 0:
        print(colored('Wrong Username', 'red'))
        validate_user()
    else:
        # validate password
        password_input = getpass.getpass("Provide Token : ")
        cursor.execute("SELECT * FROM `users`")
        password_from_db = cursor.fetchone()[2]

        # compare token
        if str(password_input) == str(password_from_db):
            return True
        else:
            return False


if not validate_user():
    print(colored('Access Denied', 'red'))
else:
    from modules.tool import anton
    print(colored('Welcome Horse pick a tool', 'green'))
    anton()

# check if username exist in database

# qr_res = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_H,
#     box_size=10,
#     border=2,
# )
#
# qr_res.add_data('https://medium.com/@ngwaifoong92')
# qr_res.make(fit=True)
# img = qr_res.make_image(fill_color="black", back_color="white").convert('RGB')
#
# img.save("sample2.png")
