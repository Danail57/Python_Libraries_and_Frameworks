import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv(
    'financial_data.csv',
    sep = ',',
    parse_dates=True,
    index_col= 0,)

df.plot(figsize=(12,6))
plt.title("Financial Data", fontsize = 16)
plt.xlabel("Date", fontsize = 14)
plt.ylabel("Price", fontsize = 14)
plt.grid(True, linestyle= '--', alpha=0.6)


plt.show()
