import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Generate random dates
start_date = datetime(2020, 1, 1)
end_date = datetime(2020, 12, 31)
date_range = [start_date + timedelta(days=random.randint(0, 365)) for _ in range(1000)]

# Generate random products
products = ['Product A', 'Product B', 'Product C', 'Product D']

# Generate random units sold and revenue for each product
data = []
for date in date_range:
    for product in products:
        units_sold = random.randint(10, 100)
        revenue = round(random.uniform(50, 200) * units_sold, 2)
        data.append([date.strftime('%Y-%m-%d'), product, units_sold, revenue])

# Create DataFrame
df = pd.DataFrame(data, columns=['Date', 'Product', 'Units Sold', 'Revenue'])

# Save DataFrame to CSV
df.to_csv('sales_data.csv', index=False)

print("CSV file 'sales_data.csv' generated successfully.")
