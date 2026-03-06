import pandas as pd
import matplotlib.pyplot as plt

# cargar datos
data = pd.read_csv("sales_data.csv")

print("Dataset:")
print(data)

# agrupar ventas por producto
sales_by_product = data.groupby("product")["sales"].sum()

print("\nTotal sales by product:")
print(sales_by_product)

# grafica
sales_by_product.plot(kind="bar")

plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.show()