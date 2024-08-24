import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.preprocessing import LabelEncoder


data = pd.read_csv('news.csv')

# Check the distribution of the labels
print(data['label'].value_counts())

le = LabelEncoder()
data['fake'] = le.fit_transform(data['label'])
dataset = data.drop('label', axis=1)
x, y = dataset['text'], dataset['fake']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
vectorizor = TfidfVectorizer(stop_words='english', max_df=0.7)
x_train_vectorizor = vectorizor.fit_transform(x_train)
x_test_vectorizor = vectorizor.transform(x_test)


clf = LinearSVC()
clf.fit(x_train_vectorizor, y_train)
print(clf.score(x_test_vectorizor, y_test))

# Test the model on a single article
article_text = x_test.iloc[12]
vectorized_text = vectorizor.transform([article_text])
prediction = clf.predict(vectorized_text)
print("Predicted label:", le.inverse_transform(prediction))
print("Actual label:", y_test.iloc[12])