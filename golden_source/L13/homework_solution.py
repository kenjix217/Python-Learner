import csv
from datetime import datetime

def main():
    print("--- Lesson 13 Golden Source Solution ---")

    # 1. Create CSV data
    sales_data = [
        ['date', 'product', 'quantity', 'price'],
        ['2026-01-10', 'Widget A', 5, 29.99],
        ['2026-01-10', 'Widget B', 3, 49.99],
        ['2026-01-11', 'Widget A', 2, 29.99],
        ['2026-01-11', 'Widget C', 7, 19.99],
        ['2026-01-12', 'Widget A', 4, 29.99],
        ['2026-01-13', 'Widget B', 1, 49.99],
        ['2026-01-14', 'Widget D', 10, 9.99],
        ['2026-01-14', 'Widget A', 3, 29.99],
        ['2026-01-15', 'Widget C', 2, 19.99],
        ['2026-01-15', 'Widget B', 5, 49.99]
    ]

    filename = 'Python-Learner/golden_source/L13/sales.csv'
    report_filename = 'Python-Learner/golden_source/L13/sales_report.csv'

    # Write source CSV
    print(f"Creating sample data: {filename}")
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(sales_data)

    # 2. Read and analyze
    print("Reading and analyzing data...")
    transactions = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        transactions = list(reader)

    # 3. Calculations
    total_revenue = 0
    product_stats = {} # {name: {'qty': 0, 'revenue': 0}}
    unique_products = set()
    daily_revenue = {} # {date: revenue}

    for row in transactions:
        qty = int(row['quantity'])
        price = float(row['price'])
        product = row['product']
        date = row['date']
        
        transaction_val = qty * price
        total_revenue += transaction_val
        unique_products.add(product)
        
        # Product stats
        if product not in product_stats:
            product_stats[product] = {'qty': 0, 'revenue': 0}
        product_stats[product]['qty'] += qty
        product_stats[product]['revenue'] += transaction_val

        # Daily stats (Bonus)
        daily_revenue[date] = daily_revenue.get(date, 0) + transaction_val

    # Derived stats
    best_selling_product = max(product_stats.items(), key=lambda x: x[1]['qty'])
    best_product_name = best_selling_product[0]
    best_product_qty = best_selling_product[1]['qty']
    
    avg_transaction_val = total_revenue / len(transactions) if transactions else 0
    
    # Bonus: Best sales day
    best_day = max(daily_revenue.items(), key=lambda x: x[1])

    # 4. Generate Report
    print("\n--- Sales Summary Report ---")
    print(f"Total Revenue: ${total_revenue:,.2f}")
    print(f"Best-Selling Product: {best_product_name} ({best_product_qty} units)")
    print(f"Average Transaction: ${avg_transaction_val:.2f}")
    print(f"Unique Products: {len(unique_products)}")
    print(f"Best Sales Day: {best_day[0]} (${best_day[1]:,.2f})")

    # Write summary to CSV
    print(f"\nWriting report to: {report_filename}")
    with open(report_filename, 'w', newline='') as f:
        fieldnames = ['Metric', 'Value']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerow({'Metric': 'Total Revenue', 'Value': f"${total_revenue:.2f}"})
        writer.writerow({'Metric': 'Best-Selling Product', 'Value': f"{best_product_name} ({best_product_qty} units)"})
        writer.writerow({'Metric': 'Average Transaction', 'Value': f"${avg_transaction_val:.2f}"})
        writer.writerow({'Metric': 'Unique Products', 'Value': len(unique_products)})
        writer.writerow({'Metric': 'Best Sales Day', 'Value': f"{best_day[0]} (${best_day[1]:.2f})"})

if __name__ == "__main__":
    main()
