!pip install pandas

import pandas as pd

sms = ["Win ₹100000 now","Your account is credited","Click here to claim prize","Salary credited"]

result = []

for i in sms:
    if "win" in i.lower() or "claim" in i.lower() or "prize" in i.lower():
        result.append("Fraud")
    else:
        result.append("Safe")

df = pd.DataFrame({"SMS":sms,"Status":result})
print(df)
