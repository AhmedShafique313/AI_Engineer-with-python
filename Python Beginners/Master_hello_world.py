def message():
    print('Hello World!')
    return

def output(n):
    try:
        for i in range(n):
            message()
    except Exception as e:
        print(f"An error occurred: {e}")
    return

tell = int(input('How many times: '))
output(tell)