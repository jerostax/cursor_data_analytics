import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_csv(file_path=None):
    """
    Loads and cleans sales data, computes total sale for each record,
    outputs aggregated sales by date, summary statistics, and displays charts.

    If no file_path is provided, defaults to 'sales_data.csv' in the same directory as this script.

    :param file_path: Path to the CSV file
    """
    if file_path is None:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, 'sales_data.csv')

    try:
        # Import sales data and parse dates
        df = pd.read_csv(file_path, parse_dates=['date'])
        initial_rows = df.shape[0]

        # Data cleaning
        df = df.drop_duplicates()
        df = df.dropna(subset=['date', 'quantity', 'price'])
        df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
        df['price']    = pd.to_numeric(df['price'], errors='coerce')
        df = df.dropna(subset=['quantity', 'price'])
        df = df[(df['quantity'] > 0) & (df['price'] > 0)]
        cleaned_rows = df.shape[0]

        # Compute total sale per record
        df['total'] = df['quantity'] * df['price']

        # Print summary statistics
        print(f"Rows before cleaning: {initial_rows}, after cleaning: {cleaned_rows}")
        print("\nDescriptive statistics for Quantity, Price, Total:")
        print(df[['quantity', 'price', 'total']].describe().to_string())

        # Aggregate sales by date
        sales_by_date = df.groupby('date', as_index=False)['total'].sum()
        print("\nSales by date (first 10 rows):")
        print(sales_by_date.head(10).to_string(index=False))

        # Top customers by total sales
        sales_by_customer = (
            df.groupby('customer_id', as_index=False)['total']
              .sum()
              .sort_values('total', ascending=False)
        )
        print("\nTop 5 customers by total sales:")
        print(sales_by_customer.head(5).to_string(index=False))

        # Plotting
        sns.set(style='whitegrid')
        
        # 1) Line plot: Total Sales Over Time
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=sales_by_date, x='date', y='total', marker='o', color='teal')
        plt.title('Total Sales Over Time')
        plt.xlabel('Date')
        plt.ylabel('Total Sales')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        # 2) Bar plot: Top 10 Products by Sales
        top_products = (
            df.groupby('product_id', as_index=False)['total']
              .sum()
              .nlargest(10, 'total')
        )
        plt.figure(figsize=(10, 6))
        sns.barplot(data=top_products, x='product_id', y='total', palette='viridis')
        plt.title('Top 10 Products by Total Sales')
        plt.xlabel('Product ID')
        plt.ylabel('Total Sales')
        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    analyze_csv()
