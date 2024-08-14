import pandas as pd

colors = ['red', 'yellow', 'blue', 'green', 'orange']
fruits = ['apples', 'bananas', 'blueberries', 'watermelon', 'oranges']

df = pd.DataFrame(columns= ['Colors', 'Fruits'])
df['Colors'], df['Fruits'] = colors, fruits
print(df)