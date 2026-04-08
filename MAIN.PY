from extract import extract_data
from transform import transform_data
from load import load_data

def run_pipeline():
    customers, orders, order_items, products = extract_data()

    fact_orders, dim_customers, dim_products = transform_data(
        customers, orders, order_items, products
    )

    load_data(fact_orders, dim_customers, dim_products)

if __name__ == "__main__":
    run_pipeline()