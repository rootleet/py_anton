import sqlite3

conn = sqlite3.connect('../test.db')


# validate username
def validate_username(user_name):
    cursor = conn.execute("SELECT * from `users` WHERE `username` = 'root'")
    user_exist = len(list(cursor))

    # if user exist

    if user_exist == 0:
        print(user_name + " Does Not Exist")
        return False
    else:
        print("Hello")
        return True


validate_username("root")
