Practical 4: Perform Spam Classifier

command prompt : pip install scikit-learn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

msg = ["Win money now", "Hello friend", "Claim your prize", "How are you"]
label = ["Spam", "Ham", "Spam", "Ham"]

cv = CountVectorizer()
x = cv.fit_transform(msg)

model = MultinomialNB()
model.fit(x, label)

test = "Claim your free reward now!"
result = model.predict(cv.transform([test]))

print(test, "is", result[0])
