dataset = ['Ali','ali@gmail.com', '1122']

def admin_sign_in():
    global dataset
    def sign_in():
        admin_name = input('Enter your name: ')
        admin_email = input('Enter your email address: ')
        admin_password = input('Enter your password: ')
        return  admin_name, admin_email, admin_password
    name, email, password = sign_in()
    if name == dataset[0] and email == dataset[1] and password == dataset[2]:
        print('Login successful')
    else:
        print('Invalid name, email or password')