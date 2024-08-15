try:
    while(1):
        select1 = input('Select the following: \n 1.Start \n 2.Stop \n >>> ')
        if (select1 == '2'):
            break
        else:
            opt1 = input('Select from the following: \n 1.Admin \n 2.User \n >>>')
            if (opt1 == 'Admin'):
                opt2 = input('Select from the following: \n 1.Superadmin \n 2.Admin \n >>> ')
                if(opt2 == '1'):
                    print('Welcome Superadmin')
                elif(opt2 == '2'):
                    print('Welcome Admin')
            elif(opt1 == '2'):
                print('Welcome User')
except Exception as e:
    print(f"An error occurred: {e}")
