def calculate_change(total_amount, amount_given):
    return amount_given - total_amount

def display_change(change, currency):
    if change < 0:
        print("Insufficient amount provided.")
    else:
        print(f"The change is: {change:.2f} {currency}")

def get_bill_denominations(currency):
    if currency == "PHP":
        return [20, 50, 100, 200, 500, 1000]
    elif currency == "USD":
        return [1, 5, 10, 20, 50, 100]
    else:
        return []

def main():
    print("Calculate Change")
    currency = input("Choose currency (PHP/USD): ").strip().upper()

    bill_denominations = get_bill_denominations(currency)
    if not bill_denominations:
        print("Invalid currency selected.")
        return

    print(f"Available bill denominations in {currency}: {bill_denominations}")
    
    try:
        total_amount = float(input(f"Enter the total amount in {currency}: "))
        amount_given = float(input(f"Enter the amount given in {currency}: "))
        
        change = calculate_change(total_amount, amount_given)
        display_change(change, currency)

        if change >= 0:
            print("You can use the following denominations for change:")
            for bill in bill_denominations:
                count = change // bill
                if count > 0:
                    print(f"{int(count)} x {bill} {currency} bill(s)")
                    change -= count * bill
            
    except ValueError:
        print("Please enter a valid amount.")

if __name__ == "__main__":
    main()
