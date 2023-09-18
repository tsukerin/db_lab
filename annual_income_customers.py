import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Mall_Customers.csv')

plt.figure(figsize=(16, 8)) 

bar_width = 0.6 

xticks = df['CustomerID'][::6]
xtick_labels = [str(customer_id) for customer_id in xticks]

max_income_index = df['Annual Income (k$)'].idxmax()

colors = ['b' if i != max_income_index else 'r' for i in range(len(df))]
edgecolors = ['k' if i != max_income_index else 'r' for i in range(len(df))]

plt.bar(df['CustomerID'], df['Annual Income (k$)'], width=bar_width, color=colors, alpha=0.7, edgecolor=edgecolors)
plt.title('Годовой доход покупателей', fontsize=16)
plt.xlabel('ID Покупатель', fontsize=12)
plt.ylabel('Годовой доход (k$)', fontsize=12)

for i, row in df.iterrows():
    if row['CustomerID'] in xticks or i == max_income_index:
        plt.text(row['CustomerID'], row['Annual Income (k$)'] + 10, f'{row["Annual Income (k$)"]}k$', ha='center', fontsize=8)

plt.xticks(xticks, xtick_labels, rotation=45, fontsize=10)
plt.yticks(fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

max_income_label = df.loc[max_income_index, 'CustomerID']
max_income_value = df.loc[max_income_index, 'Annual Income (k$)']
plt.annotate(f'Max: {max_income_value}k$', (max_income_label, max_income_value + 10), fontsize=10, ha='center')

plt.savefig('diagram.png')
plt.show()

