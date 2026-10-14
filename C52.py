def check_pwd(password):
    if password=="python123":
        return True
    else:
        return False

for i in range(1,4):
    pwd=input("Enter Password : ")
    if check_pwd(pwd):
        print("Access Granted")
        break
    else:
        print(f"Incorrect Password {3-i} attempts remaining")