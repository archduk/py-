# Function to calculate total and display prices
def display_store():
    # Prices for individual items
    prices = {
        'Item 1': 200.0,
        'Item 2': 400.0,
        'Item 3': 600.0
    }
    
    # Display the store catalog
    print("Online Store")
    print("------------------------------")
    print(f"{'Product(S)':<20}{'Price':<10}")
    print(f"{'Item 1':<20}{prices['Item 1']}")
    print(f"{'Item 2':<20}{prices['Item 2']}")
    print(f"{'Item 3':<20}{prices['Item 3']}")
    
    # Combos with discounts
    combo1_price = prices['Item 1'] + prices['Item 2']  # No discount
    combo2_price = prices['Item 2'] + prices['Item 3']  # No discount
    combo3_price = prices['Item 1'] + prices['Item 3']  # No discount
    combo4_price = prices['Item 1'] + prices['Item 2'] + prices['Item 3']  # No discount
    
    # Apply a 10% discount to two-item combos and 25% discount to three-item combo
    combo1_discounted = combo1_price * 0.90
    combo2_discounted = combo2_price * 0.90
    combo3_discounted = combo3_price * 0.90
    combo4_discounted = combo4_price * 0.75
    
    # Print combo prices
    print(f"{'Combo 1 (Item 1 + 2)':<20}{combo1_discounted}")
    print(f"{'Combo 2 (Item 2 + 3)':<20}{combo2_discounted}")
    print(f"{'Combo 3 (Item 1 + 3)':<20}{combo3_discounted}")
    print(f"{'Combo 4 (Item 1 + 2 + 3)':<20}{combo4_discounted}")
    
    # Contact details
    print("\nFor delivery Contact: +254746736229")

# Call the function to display the store output
display_store()
