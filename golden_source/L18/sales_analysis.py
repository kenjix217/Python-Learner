"""
Lesson 18: Data Analysis with Python
Golden Source Solution: Sales Data Analysis

This script demonstrates basic data analysis without external dependencies (pure Python):
1. Aggregation (sum, max, min)
2. Calculated metrics (ROI, Profit Margin, Growth Rate)
3. Trend identification
""",
import statistics

def analyze_sales_data():
    # 1. Create data for 12 months
    data = [
        {"month": "Jan", "sales": 12000, "expenses": 8000, "customers": 150},
        {"month": "Feb", "sales": 15000, "expenses": 8500, "customers": 180},
        {"month": "Mar", "sales": 14000, "expenses": 9000, "customers": 160},
        {"month": "Apr", "sales": 18000, "expenses": 9500, "customers": 210},
        {"month": "May", "sales": 22000, "expenses": 11000, "customers": 250},
        {"month": "Jun", "sales": 25000, "expenses": 12000, "customers": 290},
        {"month": "Jul", "sales": 24000, "expenses": 11500, "customers": 280},
        {"month": "Aug", "sales": 26000, "expenses": 12500, "customers": 300},
        {"month": "Sep", "sales": 23000, "expenses": 11000, "customers": 260},
        {"month": "Oct", "sales": 28000, "expenses": 13000, "customers": 320},
        {"month": "Nov", "sales": 32000, "expenses": 15000, "customers": 380},
        {"month": "Dec", "sales": 35000, "expenses": 16000, "customers": 400}
    ]

    print("=== Sales Data Analysis Report ===\n")

    # 2. Calculate total revenue, profit, ROI
    total_revenue = sum(d['sales'] for d in data)
    total_expenses = sum(d['expenses'] for d in data)
    total_profit = total_revenue - total_expenses
    roi = (total_profit / total_expenses) * 100
    profit_margin = (total_profit / total_revenue) * 100

    print(f"Total Revenue:   ${total_revenue:,.2f}")
    print(f"Total Expenses:  ${total_expenses:,.2f}")
    print(f"Total Profit:    ${total_profit:,.2f}")
    print(f"Overall ROI:     {roi:.2f}%")
    print(f"Profit Margin:   {profit_margin:.2f}%")
    print("-" * 30)

    # 3. Find best/worst months based on Profit
    # Calculate profit per month first
    for d in data:
        d['profit'] = d['sales'] - d['expenses']

    best_month = max(data, key=lambda x: x['profit'])
    worst_month = min(data, key=lambda x: x['profit'])

    print(f"Best Month (Profit):  {best_month['month']} (${best_month['profit']:,.2f})")
    print(f"Worst Month (Profit): {worst_month['month']} (${worst_month['profit']:,.2f})")
    print("-" * 30)

    # 4. Calculate growth rate month-over-month (Revenue)
    print("Month-over-Month Revenue Growth:")
    growth_rates = []
    for i in range(1, len(data)):
        prev = data[i-1]['sales']
        curr = data[i]['sales']
        growth = ((curr - prev) / prev) * 100
        growth_rates.append(growth)
        print(f"  {data[i]['month']}: {growth:+.2f}%")
    
    avg_growth = statistics.mean(growth_rates)
    print(f"\nAverage Monthly Growth: {avg_growth:+.2f}%")
    print("-" * 30)

    # 5. Identify trends (Simple interpretation)
    print("Trends Analysis:")
    if avg_growth > 5:
        print("- Strong positive growth trend observed.")
    elif avg_growth > 0:
        print("- Moderate growth trend observed.")
    else:
        print("- Negative growth trend observed.")

    sales_values = [d['sales'] for d in data]
    variance = statistics.variance(sales_values)
    print(f"- Sales volatility (variance): {variance:,.0f}")
    
    # Customer efficiency (Revenue per customer)
    total_customers = sum(d['customers'] for d in data)
    avg_rev_per_customer = total_revenue / total_customers
    print(f"- Average Revenue per Customer: ${avg_rev_per_customer:.2f}")

if __name__ == "__main__":
    analyze_sales_data()
