try:
    print('Welcome to the online mart')
    dataset = ['ahmed313@gmail.com', '1324']
    def super_sign_in():
        global dataset
        def sign_in():
            super_email = input('Enter your email address: ')
            super_password = input('Enter your password: ')
            return super_email, super_password
        email, password = sign_in()
        if email in dataset:
            print('Email is correct')
        elif password in dataset:
            print('Password is correct')
except Exception as e:
    print(f"An error occurred: {e}")