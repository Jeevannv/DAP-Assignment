import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv("motorbikes.csv")
df = pd.DataFrame(data)
price = df["price"].head()
bikes = df["make_model"].head()
explode = (0.1, 0, 0, 0, 0)
plt.pie(price, labels=bikes, explode=explode, shadow=True, autopct='%1.1f%%')
plt.title("Bikes and their price")
plt.show()