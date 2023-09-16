import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
plt.title('Пол покупателей')
df = pd.read_csv('Mall_Customers.csv', delimiter=',')
values = ['Женский', 'Мужской']
plt.pie(df.groupby('Genre')['CustomerID'].count(), labels = values, autopct='%1.1f%%', shadow=True, wedgeprops={'lw':1, 'ls':'--','edgecolor':"k"})
fig.savefig('pie.png')
plt.show()
