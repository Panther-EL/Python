import numpy as np
                    #E-commerce sales analysis
# north=1
# south=2
# west=3
# east=4

order_id = np.array([100,101,102,103,104,105])
print(f'Order ids:{order_id}')

price = np.array([250,100,300,800,150,550])
print(f'Prices:{price}')

quantity = np.array([1,2,5,3,7,8])
print(f'Quantities:{quantity}')

discount = np.array([0,10,20,30,40,70])
print(f'Discounts:{discount}')

region = np.array([1,2,1,4,2,3])
print(f'Regions:{region}')

order_status = np.array([1,0,0,1,0,1])
print(f'Order status:{order_status}')

total_sales = price * quantity

            #Checking conditions
completed_orders = (order_status == 1) #Checking completed orders
print(order_status[completed_orders])

discount_granted =(discount > 0) #Checking discounted orders
print(discount[discount_granted])

high_value_orders = (total_sales > 500) #Checking high value orders
print(total_sales[high_value_orders])

        #Combining conditions
#Completed orders only       
completed_order_ids = order_id[completed_orders]
completed_sales = total_sales[completed_orders]

print(f'Completed order ids: {completed_order_ids}')
print(f'Total sales for completed orders {completed_sales}')

#Cancelled orders only
cancelled_orders = (order_status == 0) #Checking cancelled orders
cancelled_order_ids = order_id[cancelled_orders]
cancelled_sales = total_sales[cancelled_orders]

print(f'Cancelled order ids: {cancelled_order_ids}')
print(f'Total sales for cancelled orders: {cancelled_sales}')

#Orders with discount
discount_on_total_sales = total_sales[discount_granted]
discount_on_quantity = quantity[discount_granted]

print(f'Discount on total sales: {discount_on_total_sales}')
print(f'Discount on quantity: {discount_on_quantity}')

#High value orders
high_value_order_id = order_id[high_value_orders]
high_value_total_sales = total_sales[high_value_orders]

print(f'High value order ids: {high_value_order_id}')
print(f'High value total sales: {high_value_total_sales}')

#Completed + no discount
completed_no_discount = (order_status == 1) & (discount == 0)
completed_orders_total_sales = total_sales[completed_no_discount]
completed_order_id = order_id[completed_no_discount]

print(f'Completed total sales with no discount: {completed_orders_total_sales}')
print(f'Completed order id with no discount: {completed_order_id}')

#Completed + discounted
completed_discounted = (order_status == 1) & (discount > 0)
completed_orders_total_sales_discounted = total_sales[completed_discounted]
completed_order_id_discounted = order_id[completed_discounted]

print(f'Completed total sales with  discount: {completed_orders_total_sales_discounted}')
print(f'Completed order id with no discount: {completed_order_id_discounted}')

#High value + completed
high_value_completed = (order_status == 1) & (total_sales > 500)
high_value_completed_id = order_id[high_value_completed]
high_value_completed_total_sales = total_sales[high_value_completed]

print(f'High value order ids: {high_value_completed_id}')
print(f'High value total sales: {high_value_completed_total_sales}')

#High value + completed + no discount
high_value_completed_no_discount = (order_status == 1) & (total_sales > 500) & (discount == 0)
high_value_completed_no_discount_total_sales = total_sales[high_value_completed_no_discount]
high_value_completed_no_discount_order_id = order_id[high_value_completed_no_discount]

print(f'High value completed no discount total sales:{high_value_completed_no_discount_total_sales}')
print(f'High value completed no discount order id:{high_value_completed_no_discount_order_id}')

                #Region based combinations 

#North(1)
region_north = (order_status == 1) & (region == 1)
region_north_total_sales = total_sales[region_north]
region_north_quantity = quantity[region_north]

print(f'Total sales in the north is {region_north_total_sales}')
print(f'Quantity sold in the north:{region_north_quantity}')


#South(2)
region_south = (order_status == 1) & (region == 2)
region_south_total_sales = total_sales[region_south]
region_south_quantity = quantity[region_south]

print(f'Total sales in the south is: {region_south_total_sales}')
print(f'Quantity sold in the south:{region_south_quantity}')

#West(3)
region_west = (order_status == 1) & (region == 3)
region_west_total_sales = total_sales[region_west]
region_west_quantity = quantity[region_west]

print(f'Total sales in the west is: {region_west_total_sales}')
print(f'Quantity sold in the west:{region_west_quantity}')


#East(4)
region_east = (order_status == 1) & (region == 4)
region_east_total_sales = total_sales[region_east]
region_east_quantity = quantity[region_east]

print(f'Total sales in the east is: {region_east_total_sales}')
print(f'Quantity sold in the east:{region_east_quantity}')


                #Discounted orders in specific regions

#North(1)
discount_north = (discount > 0) & (region == 1)
discount_north_total_sales = total_sales[discount_north]
discount_north_quantity = quantity[discount_north]

print(f'The discount for the total sales in the north is{discount_north_total_sales}')
print(f'The discount for quantity in the north is {discount_north_quantity}')


#South(2)
discount_south = (discount > 0) & (region == 2)
discount_south_total_sales = total_sales[discount_south]
discount_south_quantity = quantity[discount_north]

print(f'The discount for the total sales in the south is{discount_south_total_sales}')
print(f'The discount for quantity in the south is {discount_south_quantity}')


#West(3)
discount_west = (discount > 0) & (region == 2)
discount_west_total_sales = total_sales[discount_west]
discount_west_quantity = quantity[discount_west]

print(f'The discount for the total sales in the west is{discount_west_total_sales}')
print(f'The discount for quantity in the west is {discount_west_quantity}')


#East(4)
discount_east = (discount > 0) & (region == 2)
discount_east_total_sales = total_sales[discount_east]
discount_east_quantity = quantity[discount_east]

print(f'The discount for the total sales in the west is{discount_east_total_sales}')
print(f'The discount for quantity in the west is {discount_east_quantity}')


