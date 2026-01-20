import numpy as np
                    #E-commerce sales analysis
order_id = np.array([100,101,102,103,104,105])
price = np.array([250,100,300,800,150,550])
quantity = np.array([1,2,5,3,7,8])
discount = np.array([0,10,20,30,40,70])
region = np.array([1,2,1,4,2,3])
order_status = np.array([1,0,0,1,0,1])

total_sales = price * quantity

            #Checking conditions
completed_orders = (order_status == 1) #Checking completed orders
print(order_status[completed_orders])

discount_granted =(discount > 0) #Checking discounted orders
print(discount[discount_granted])

print(total_sales[high_value_orders])
