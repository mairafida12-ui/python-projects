import pandas as pd

# Creating the product catalog
data = {
    'Product_ID':[101, 102, 103, 104,105] ,
    'Category' : ['Electronics' , 'Home' , 'Electronics' , 'Books' , 'Electronics'],
    'Price' : [500.0, 45.0, 1200.0, 20.0, 150.0] ,
}

pd.DataFrame(data).to_csv('products.csv', index=False)
class Product:
    def __init__(self, prod_id, price):
        self.prod_id = prod_id
        self.price = price

    def apply_discount(self, percent_off):
        # Calculation: Price * (1 - (Discount / 100))
         self.price = self.price * (1 - (percent_off / 100))

# --- Filtering ---
df = pd.read_csv('products.csv')

# Create a copy of the electronics only to avoid SettingWithCopy warnings later
electronics_df = df[df['Category'] == 'Electronics'].copy()

# ---Integration ---
new_prices = []

for index, row in electronics_df.iterrows():
 product= Product(row['Product_ID'], row['Price'])
product.apply_discount(20)
new_prices.append(product.price)

# --- Rebuilding ---
# Replace old prices with the discounted prices from our list
electronics_df['Price'] = new_prices

# --- Saving ---
# Note: This requires the 'openpyxl' library installed (pip install openpyxl)
electronics_df.to_excel ('holiday_promos.xlsx' , index = False)

print("Holiday promo catalog created successfully!")
print(electronics_df)












