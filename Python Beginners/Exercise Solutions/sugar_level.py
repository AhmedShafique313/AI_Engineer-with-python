def user():
    print('Hi!, I am sugar level based precaution app')
    st = input('Enter your name: ')
    print(f'Welcome! {st}')
    level = input('Now, tell me your sugar level: ')
    level = float(level)
    return st, level

def level_checker(name, sugar_level):
    if (sugar_level < 80):
        print(f'Oh! {name}, Your sugar level is below than 80. Go and get some glucose.')
        print('By eating sweets, fruits and chocolates')
    elif (sugar_level < 100):
        if (sugar_level < 80):
              print(f'Oh! {name}, Your sugar level is below than 80. Go and get some glucose.')
              print('By eating sweets, fruits and chocolates')
        else:
            print("Relax man/woman, You have good health")
    elif (sugar_level > 100):
        print(f'Oh! {name}, Stop eating sweet things, go and use inculine or medicine to reduce your sugar level')
        
def main():
    try:
        name, sugar_level = user()
        level_checker(name, sugar_level)
    except Exception as e:
        print(f"An error occurred: {e}")
    return

if __name__ == "__main__":
    main()