items = {"apple" : 20, "banana" : 10, "orange" : 35, "peach" : 25, "tomato" : 14, "potato" : 30, "onion" : 6, "garlic" : 22, "soap" : 30, "shampoo" : 50, "conditioner" : 60, "surf" : 20, "sugar" : 12, "tea" : 10, "chili" : 4, "dals" : 17}

def price_estimate():
    global items
    x = input('Which item you want to buy? \n >>> ')
    print(f'The price of {x} is:', items.get(x))
    y = input('Do you want to buy something more? \n 1.Yes \n 2.No \n >>> ')
    if y == '2':
        print('Here is your receipt')
    else:
        receipt = []
        print('You can only buy 10 items only at each time')
        for i in range(10):
            x1 = input('Type item name here: ')
            val = items.get(x1)
            receipt.append(val)
        total = 0
        total = sum(receipt)
        print(f'Total bill: {total}')
    return
