E-Commerce ETL Pipeline

This project is a basic attempt at building an end-to-end ETL pipeline using a real-world e-commerce dataset.

The idea was simple: take raw CSV data, clean it properly, combine multiple tables, and make it usable for analysis.

What I did in this project

- Loaded multiple datasets (customers, orders, products, order items)
- Checked for missing values and duplicates
- Cleaned data based on actual business logic instead of blindly dropping values
- Merged different tables into one usable dataset
- Created new features like revenue, year, and month
- Built simple fact and dimension tables
- Loaded final data into a database
- Ran SQL queries to extract insights
- Visualized results using Power BI

Tech Stack

- Python (Pandas, NumPy)
- SQL (SQLite used here, but can be switched to MySQL)
- SQLAlchemy
- Power BI

Project Structure

project/
│
├── data/                  (place dataset here)
├── extract.py             (loads raw data)
├── transform.py           (cleaning and merging)
├── load.py                (loads data into database)
├── main.py                (runs the full pipeline)
│
├── sql/
│   └── analysis.sql
│
├── requirements.txt
└── README.md

Dataset

Dataset is not included because of size limitations.

You can download it from Kaggle:
https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

After downloading, place all CSV files inside the data folder.

How to run

1. Install dependencies:
pip install -r requirements.txt

2. Run:
python main.py

This will create a database file (ecommerce.db) with cleaned tables.

Database Note

SQLite is used here because the project was developed in Colab where local MySQL connection is not possible.

The same pipeline can be used with MySQL by just changing the connection string.

Example analysis

- Monthly revenue trend
- Top product categories
- Top cities by revenue

What I learned

- How real-world data is distributed across multiple tables
- How to clean and prepare data properly
- How ETL pipelines are structured step by step
- How to convert raw data into meaningful insights

Future improvements

- Add logging
- Automate the pipeline
- Connect to a cloud database
