from user import user_login
from superadmin import super_sign_in

try:
    while True:
        select1 = input('Select the following: \n 1.Start \n 2.Stop \n >>> ')
        if select1 == '2':
            break
        else:
            opt1 = input('Select from the following: \n 1.Admin \n 2.User \n >>> ')
            if opt1 == '1':
                opt2 = input('Select from the following: \n 1.Superadmin \n 2.Admin \n >>> ')
                if opt2 == '1':
                    super_sign_in()
                else:
                    print('Welcome Admin')
            else:
                user_login()
except Exception as e:
    print(f"An error occurred: {e}")
