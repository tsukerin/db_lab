import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Mall_Customers.csv')

plt.figure(figsize=(16, 8))

step = 4

plt.plot(df['CustomerID'][::step], df['Age'][::step], marker='o', linestyle='-', color='b', markersize=5, label='Возраст')
plt.fill_between(df['CustomerID'][::step], df['Age'][::step], color='b', alpha=0.3)

plt.title('Возраст покупателей', fontsize=16)
plt.xlabel('ID Покупатель', fontsize=12)
plt.ylabel('Возраст', fontsize=12)

plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

plt.legend(loc='upper left', fontsize=12)

for i, row in df[::step].iterrows():
    plt.text(row['CustomerID'], row['Age'] + 2, f'{row["Age"]} лет', ha='center', fontsize=10)

plt.savefig('lin_diagram.png')
plt.show()

