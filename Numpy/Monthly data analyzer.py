import numpy as np
  #Monthly Sales Data Analyzer
#Creation of sales array
print('-------              Monthly Data Analyzer               -------')
sales = np.random.randint(49,501,size=(12,5))
print(sales)

#Array properties
print(f'Shape:{sales.shape}')
print(f'Shape:{sales.size}')
print(f'Shape:{sales.dtype}')

#Analysis
sales_per_product = np.sum(sales, axis=0)
sales_per_month = np.sum(sales, axis=1)

print(f'Sales per product is : {sales_per_product}')
print(f'Sales per month is : {sales_per_month}')

avg_sales_per_month = np.mean(sales, axis=1)
print(f'The average monthly sales are: {avg_sales_per_month}')

month_highest = np.max(sales_per_month)
product_highest = np.max(sales_per_product)

print(f'The month with highest sale is {month_highest}')
print(f'The product with highest sale is {product_highest}')

#Reshaping
sales_1D = sales.reshape(-1)
print(f'Sales in 1D is {sales_1D}')
