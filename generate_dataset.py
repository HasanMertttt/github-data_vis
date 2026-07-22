import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 1. Set random seed for reproducibility
np.random.seed(42)

# 2. Set sample size (~2000 rows)
n_rows = 2000

# 3. Generate transaction IDs
transaction_ids = [f"TXN-{10000 + i}" for i in range(n_rows)]

# 4. Generate transaction dates over a 6-month period (2024-01-01 to 2024-06-30)
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 6, 30)
total_seconds = int((end_date - start_date).total_seconds())

random_seconds = np.random.randint(0, total_seconds, size=n_rows)
transaction_dates = [start_date + timedelta(seconds=int(s)) for s in random_seconds]
transaction_dates.sort()  # Chronological order

# 5. Define branch locations and their probabilities
branches = ['Downtown', 'Financial District', 'Suburban Mall', 'University Campus', 'Airport Terminal']
branch_probs = [0.30, 0.25, 0.20, 0.15, 0.10]
branch_names = np.random.choice(branches, size=n_rows, p=branch_probs)

# 6. Define product categories, products, and prices
products_catalog = {
    'Hot Coffee': [
        ('Espresso', 3.00),
        ('Americano', 3.50),
        ('Cappuccino', 4.50),
        ('Caffè Latte', 4.75),
        ('Caramel Macchiato', 5.25)
    ],
    'Cold Coffee': [
        ('Iced Americano', 3.75),
        ('Iced Latte', 5.00),
        ('Cold Brew', 4.80),
        ('Frappuccino', 5.50)
    ],
    'Tea & Beverages': [
        ('Green Tea', 3.25),
        ('Earl Grey', 3.25),
        ('Chai Latte', 4.50),
        ('Matcha Latte', 5.00)
    ],
    'Bakery & Pastry': [
        ('Butter Croissant', 3.50),
        ('Chocolate Muffin', 3.80),
        ('Blueberry Scone', 3.75),
        ('Almond Croissant', 4.25)
    ],
    'Sandwiches & Wraps': [
        ('Turkey & Cheese Sandwich', 7.50),
        ('Veggie Wrap', 6.80),
        ('Avocado Toast', 8.25)
    ],
    'Merchandise': [
        ('Coffee Beans 250g', 14.50),
        ('Reusable Travel Mug', 18.00)
    ]
}

categories = list(products_catalog.keys())
category_probs = [0.35, 0.25, 0.15, 0.15, 0.07, 0.03]

product_categories = []
product_names = []
prices = []

for _ in range(n_rows):
    cat = np.random.choice(categories, p=category_probs)
    prod_info = products_catalog[cat][np.random.randint(0, len(products_catalog[cat]))]
    product_categories.append(cat)
    product_names.append(prod_info[0])
    prices.append(prod_info[1])

# 7. Generate quantities and compute total amounts
quantities = np.random.choice([1, 2, 3, 4], size=n_rows, p=[0.70, 0.20, 0.07, 0.03])
prices = np.array(prices)
quantities = np.array(quantities)
total_amounts = np.round(prices * quantities, 2)

# 8. Generate customer demographics and order details
payment_methods = np.random.choice(['Credit Card', 'Mobile Pay', 'Cash', 'Gift Card'], size=n_rows, p=[0.50, 0.35, 0.10, 0.05])
customer_ages = np.random.randint(18, 70, size=n_rows)
customer_genders = np.random.choice(['Female', 'Male', 'Non-Binary', 'Prefer not to say'], size=n_rows, p=[0.48, 0.46, 0.04, 0.02])
loyalty_members = np.random.choice([1, 0], size=n_rows, p=[0.40, 0.60])

# Satisfaction scores (1 to 5) with high probability for positive ratings
satisfaction_scores = np.random.choice([1, 2, 3, 4, 5], size=n_rows, p=[0.03, 0.07, 0.15, 0.45, 0.30])

# Weekend flag derived from date
is_weekends = [1 if d.weekday() >= 5 else 0 for d in transaction_dates]

# 9. Create Pandas DataFrame
df = pd.DataFrame({
    'transaction_id': transaction_ids,
    'transaction_date': transaction_dates,
    'branch_name': branch_names,
    'product_category': product_categories,
    'product_name': product_names,
    'quantity': quantities,
    'price': prices,
    'total_amount': total_amounts,
    'payment_method': payment_methods,
    'customer_age': customer_ages,
    'customer_gender': customer_genders,
    'loyalty_member': loyalty_members,
    'satisfaction_score': satisfaction_scores,
    'is_weekend': is_weekends
})

# Save to CSV in Desktop/github-data_vis directory
output_csv_path = 'C:/Users/LENOVO/Desktop/github-data_vis/coffee_shop_sales.csv'
df.to_csv(output_csv_path, index=False)
print(f"Dataset successfully created with shape {df.shape} and saved to {output_csv_path}")
