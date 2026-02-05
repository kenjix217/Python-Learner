import json
from datetime import datetime

def convert_currency(amount, from_currency, to_currency, rates):
    """
    Converts an amount from one currency to another using the provided rates.
    Assumes base currency of rates is USD.
    """
    # Normalize inputs to uppercase
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()
    
    # Check if currencies exist in rates
    # Note: USD is the base, so it might not be in the 'rates' dict explicitly if we don't put it there,
    # but logically rate of USD to USD is 1.0.
    
    # Helper to get rate relative to USD
    def get_usd_rate(code):
        if code == "USD":
            return 1.0
        if code not in rates:
            raise ValueError(f"Currency code '{code}' not found in exchange rates.")
        return rates[code]

    try:
        from_rate = get_usd_rate(from_currency)
        to_rate = get_usd_rate(to_currency)
        
        # Convert to USD first (Amount / From_Rate), then to Target ( * To_Rate)
        # Since rates are 1 USD = X Currency:
        # 100 EUR -> ? USD -> ? JPY
        # USD Value = Amount / Rate_of_From (e.g., 100 EUR / 0.92 = 108 USD) -- WAIT. 
        # Usually "USD": {"EUR": 0.92} means 1 USD = 0.92 EUR.
        # So to get USD from EUR: Amount / Rate.
        # To get JPY from USD: USD_Amount * Rate.
        
        usd_value = amount / from_rate
        target_value = usd_value * to_rate
        return target_value
        
    except ValueError as e:
        return str(e)

def find_best_value(amount_usd, rates):
    """
    Finds which currency gives the largest numeric value for a given USD amount.
    """
    best_code = "USD"
    best_amount = amount_usd
    
    for code, rate in rates.items():
        converted = amount_usd * rate
        if converted > best_amount:
            best_amount = converted
            best_code = code
            
    return best_code, best_amount

def main():
    print("--- Lesson 12 Golden Source Solution ---")

    # 1. Create a dictionary simulating API response
    rates_data = {
        "base": "USD",
        "date": datetime.now().strftime("%Y-%m-%d"),
        "rates": {
            "EUR": 0.92,
            "GBP": 0.79,
            "JPY": 149.50,
            "CAD": 1.35,
            "AUD": 1.52
        }
    }

    # 2. Convert to JSON string
    json_string = json.dumps(rates_data, indent=2)
    print("\nSimulated API Response:")
    print(json_string)

    # 3. Parse it back
    data = json.loads(json_string)
    rates = data["rates"]

    # 4. Convert $100 USD to at least 3 different currencies
    amount_usd = 100
    target_currencies = ["EUR", "GBP", "JPY", "CAD"]

    print(f"\n--- Conversions for ${amount_usd} USD ---")
    for code in target_currencies:
        result = convert_currency(amount_usd, "USD", code, rates)
        # Format based on currency type (simple logic)
        symbol = "¥" if code == "JPY" else "£" if code == "GBP" else "€" if code == "EUR" else "$"
        print(f"{code}: {symbol}{result:,.2f}")

    # Bonus: Error Handling Test
    print("\n--- Bonus: Error Handling Test ---")
    bad_result = convert_currency(100, "USD", "ZZZ", rates)
    print(f"Converting to ZZZ: {bad_result}")

    # Bonus: Best Value
    print("\n--- Bonus: Best Numeric Value ---")
    best_code, best_amt = find_best_value(100, rates)
    print(f"For $100 USD, the largest numeric amount is in {best_code}: {best_amt:,.2f}")

if __name__ == "__main__":
    main()
