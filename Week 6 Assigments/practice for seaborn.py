import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

df = pd.read_csv('Week 6 Assigments/RealEstate-USA.csv', delimiter= ",", parse_dates=[4], date_format={'date_added': '%d-%m-%Y'})

print(df)



sns.set_theme(style='whitegrid')
sns.lineplot(x='city', y='state', data=df)
plt.show()

user = input("Wait------")

sns.set_theme(style= 'darkgrid')
sns.displot(x= 'city', y= 'state', data=df)
plt.show()


sns.set_theme(style= 'ticks')
sns.displot(x= 'city', y= 'state', data=df)
plt.show()


user = input("Wait------")

sns.set_theme(style= 'darkgrid')
sns.jointplot(x= 'city', y= 'state', data=df)
plt.show()