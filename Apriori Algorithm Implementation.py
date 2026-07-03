Practical 6: Apriori Algorithm Implementation

command prompt : pip install pandas mlxtend
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

data = [["Milk","Bread"],["Milk","Butter"],["Bread","Butter"],["Milk","Bread","Butter"]]

te = TransactionEncoder()
df = pd.DataFrame(te.fit(data).transform(data), columns=te.columns_)

freq = apriori(df, min_support=0.5, use_colnames=True)

display = freq.copy()
display["itemsets"] = display["itemsets"].apply(lambda x: ", ".join(x))
print(display)

rules = association_rules(freq, metric="confidence", min_threshold=0.5)
print(rules[["antecedents","consequents","confidence"]])
