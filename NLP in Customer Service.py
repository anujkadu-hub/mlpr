!pi install pandas
import pandas as pd

data = ["Payment failed","Order not delivered","Need refund","Product is good"]

intent = []

for i in data:
    if "payment" in i.lower():
        intent.append("Payment")
    elif "order" in i.lower():
        intent.append("Delivery")
    elif "refund" in i.lower():
        intent.append("Refund")
    else:
        intent.append("Feedback")

df = pd.DataFrame({"Customer Query":data,"Intent":intent})
print(df)
