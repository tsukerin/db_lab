import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

fig, ax = plt.subplots()
plt.title('Возраст покупателей')
df = pd.read_csv('Mall_Customers.csv', delimiter=',')
plt.plot(df['Age'], df['CustomerID'])
plt.xticks(df['Age'], df['CustomerID'])
plt.show()
fig.savefig('diagram.png')