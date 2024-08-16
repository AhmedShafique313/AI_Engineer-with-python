def user_login():
    try:
        print('Welcome to the online mart')
        select2 = input('Select from the following: \n 1.Sign up \n 2.Sign in \n >>> ').capitalize()
        if select2 == '1':
            sign_up()
        else:
            sign_in()
    except Exception as e:
        print(f"An error occurred: {e}")

def sign_up():
    print('---------- Please enter the sign up details ----------')
    user_name = input('Enter your name: ')
    user_number = input('Enter your number: +92 ')
    user_email = input('Enter your email address: ')
    user_password = input('Enter your password: ')
    print('---------- Account Created Successfully ----------')
    return user_name, user_email, user_number, user_password

def sign_in():
    print('---------- Please enter the login details ----------')
    user_email = input('Enter your email address: ')
    user_password = input('Enter your password: ')
    return user_email, user_password