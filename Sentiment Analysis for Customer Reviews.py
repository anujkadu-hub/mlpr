practica 10: Sentiment Analysis for Customer Reviews and Visualization

command prompt: pip install textblob pandas matplotlib

from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt

reviews = ["Good Product","Bad Quality","Excellent Service","Excellent","Working fine","Poor Delivery","Decent Product"]

sentiment = [("Positive" if TextBlob(r).sentiment.polarity>0.2
              else "Negative" if TextBlob(r).sentiment.polarity<-0.2
              else "Neutral") for r in reviews]

df = pd.DataFrame({"Review":reviews,"Sentiment":sentiment})
print(df)

count = df["Sentiment"].value_counts().reindex(["Positive","Negative","Neutral"], fill_value=0)

plt.bar(count.index, count.values,
        color=["green","red","gray"],
        edgecolor="black")

plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.title("Customer Review Sentiment")
plt.show()
