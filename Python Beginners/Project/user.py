def user_login():
    try:
        print('Welcome to the online mart')
        select2 = input('Select from the following: \n 1.Sign up \n 2.Sign in \n >>> ').capitalize()
        if select2 == '1':
            a, b, c, d = sign_up()
            if checking(a, b, c, d):
                print('Account Created Successfully')
            else:
                print('Email already exist, please try login')
                sign_in()
        else:
            sign_in()
    except Exception as e:
        print(f"An error occurred: {e}")
    return database

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

def database(name, number, email, password):
    user_data = []
    user_data.append(name)
    user_data.append(number)
    user_data.append(email)
    user_data.append(password)
    return user_data

dataset = []

def checking(name, number, email, password):
    global dataset
    for data in dataset:
        if email == data[2]:
            return False
    dataset.append(database(name, number, email, password))
    return True
