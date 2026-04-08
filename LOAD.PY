from sqlalchemy import create_engine

def load_data(fact_orders, dim_customers, dim_products):

    engine = create_engine("sqlite:///ecommerce.db")

    fact_orders.to_sql("fact_orders", engine, if_exists="replace", index=False)
    dim_customers.to_sql("dim_customers", engine, if_exists="replace", index=False)
    dim_products.to_sql("dim_products", engine, if_exists="replace", index=False)