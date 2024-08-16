dataset = ['ahmed313@gmail.com', '1324']

def super_sign_in():
    global dataset
    def sign_in():
        super_email = input('Enter your email address: ')
        super_password = input('Enter your password: ')
        return super_email, super_password
    email, password = sign_in()
    if email == dataset[0] and password == dataset[1]:
        print('Login successful')
    else:
        print('Invalid email or password')