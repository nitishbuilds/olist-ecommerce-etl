import pandas as pd

def transform_data(customers, orders, order_items, products):

    orders = orders[orders['order_status'] == 'delivered']

    products['product_category_name'].fillna("unknown", inplace=True)
    products.fillna(0, inplace=True)

    df = order_items.merge(orders, on="order_id", how="inner")
    df = df.merge(customers, on="customer_id", how="inner")
    df = df.merge(products, on="product_id", how="inner")

    df['revenue'] = df['price'] + df['freight_value']
    df['year'] = df['order_purchase_timestamp'].dt.year
    df['month'] = df['order_purchase_timestamp'].dt.month

    df.dropna(subset=['order_purchase_timestamp'], inplace=True)

    fact_orders = df[[
        'order_id','customer_id','product_id','price',
        'freight_value','revenue','order_purchase_timestamp',
        'year','month','customer_city','product_category_name'
    ]]

    dim_customers = customers[['customer_id','customer_city','customer_state']]
    dim_products = products[['product_id','product_category_name']]

    return fact_orders, dim_customers, dim_products