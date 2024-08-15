def user_login():
    try:
        print('Welcome to the online mart')
        select2 = input('Select from the following: \n 1.Sign up \n 2.Sign in \n >>> ')
    except Exception as e:
        print(f"An error occurred: {e}")
