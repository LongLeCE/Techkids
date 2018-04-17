def accept_login(acc, usr, psw):
    if usr in acc and acc[usr] == psw:
        return True
    return False


users = {"user1": "password1", "user2": "password2", "user3": "password3"}
if accept_login(users, input("Username: "), input("Password: ")):
    print("login successful!")
else:
    print("login failed...")
