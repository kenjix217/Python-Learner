import json
from datetime import datetime

def main():
    print("--- Lesson 11 Golden Source Solution ---")
    
    # 1. Create data for 3 months
    # Using datetime for the bonus challenge to include actual dates
    current_year = datetime.now().year
    
    sales_data = [
        {
            "month": "January",
            "date": f"{current_year}-01-31",
            "sales": 15000,
            "customers": 120,
            "top_product": "Widget A"
        },
        {
            "month": "February",
            "date": f"{current_year}-02-28",
            "sales": 18000,
            "customers": 145,
            "top_product": "Widget B"
        },
        {
            "month": "March",
            "date": f"{current_year}-03-31",
            "sales": 21000,
            "customers": 160,
            "top_product": "Widget A"
        }
    ]

    # 2. Convert to JSON format
    json_string = json.dumps(sales_data, indent=2)
    
    # 3. Print the JSON string
    print("\nGenerated JSON Data:")
    print(json_string)

    # 4. Parse it back
    data = json.loads(json_string)

    # 5. Calculate statistics
    total_sales = 0
    total_customers = 0
    months_count = len(data)
    
    highest_sales_month = data[0]

    for month_data in data:
        total_sales += month_data["sales"]
        total_customers += month_data["customers"]
        
        if month_data["sales"] > highest_sales_month["sales"]:
            highest_sales_month = month_data

    average_customers = total_customers / months_count

    print("\n--- Analysis Results ---")
    print(f"Total Sales: ${total_sales:,}")
    print(f"Average Customers: {average_customers:.1f}")
    print(f"Highest Sales Month: {highest_sales_month['month']} (${highest_sales_month['sales']:,})")

    # Bonus: Calculate how long ago each month was
    print("\n--- Bonus: Time Analysis ---")
    now = datetime.now()
    for month_data in data:
        month_date = datetime.strptime(month_data["date"], "%Y-%m-%d")
        delta = now - month_date
        print(f"{month_data['month']} was {delta.days} days ago.")

if __name__ == "__main__":
    main()
