import pandas as pd

categories = {"fruits", "vegetables", "detergents", "grocery"}
fruits = {"apple", "banana", "orange", "peach"}
vegetables = {"tomato", "potato", "onion", "garlic"}
detergents = {"soap", "shampoo", "conditioner", "surf"}
grocery = {"sugar", "tea", "chili", "dals"}

def search():
    global categories, fruits, vegetables, detergents, grocery
    see1 = input('Enter the category which your find in the grocery store? \n >>> ')
    if see1 in categories:
        print(see1, 'found')
    see2 = input('Enter the fruit which your search? \n >>> ')
    if see2 in fruits:
        print(see2, 'found')
    see3 = input('Enter the vegetable which your search? \n >>> ')
    if see3 in vegetables:
        print(see3, 'found')
    see4 = input('Enter the detergent which your search? \n >>> ')
    if see4 in detergents:
        print(see4, 'found')
    see5 = input('Enter the grocery item which your find? \n >>> ')
    if see5 in grocery:
        print(see5, 'found')
    else:
        print('Not available X')
    return

def priting_items():
    categories = ["fruits", "vegetables", "detergents", "grocery"]
    fruits = ["apple", "banana", "orange", "peach"]
    vegetables = ["tomato", "potato", "onion", "garlic"]
    detergents = ["soap", "shampoo", "conditioner", "surf"]
    grocery = ["sugar", "tea", "chili", "dals"]
    df = pd.DataFrame(columns= ["fruits", "vegetables", "detergents", "grocery"])
    df['fruits'], df['vegetables'], df['detergents'], df['grocery'] = fruits, vegetables, detergents, grocery
    print(df.head())
    return