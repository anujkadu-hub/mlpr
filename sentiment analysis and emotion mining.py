from google.colab import files
uploaded = files.upload()

import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

df = pd.read_csv("reviews.csv")

df["Sentiment"] = df["Review"].apply(
    lambda x: "Positive" if TextBlob(x).sentiment.polarity > 0.2
    else "Negative" if TextBlob(x).sentiment.polarity < -0.2
    else "Neutral"
)

print(df)
