import pandas as pd

# Creating the initial stock data
stock_data = {
    'Ingredient': ['Coffee Beans', 'Milk', 'Sugar', 'Cocoa Powder' ],
    'Qty_kg': [10.0, 20.0, 5.0, 3.0],
    'Cost_per_kg': [15.00, 2.50, 1.20, 8.00]
}

df_morning =pd.DataFrame(stock_data)
df_morning.to_csv('morning_stock.csv' , index = False)
print("Initial stock file 'morning_stock.csv' created.")
class Ingredient:
    def __init__(self,name,quantity):
        self.name = name
        self.quantity =float (quantity)

    def use_item(self,amount):
        if amount<=self.quantity:
            self.quantity -= amount
            print(f"Used {amount} kg of {self.name}. Remaining:{self.quantity}kg" )
        else:
            print(f"Error: Not enough {self.name}. in stock!")
# Load the data
df =pd.read_csv('morning_stock.csv')

# Rename the column as required
df =df.rename(columns={'Qty_kg':'Current_Quantity'})

# Use filtering to isolate "Coffee Beans"
# .iloc[0] converts the filtered one-row DataFrame into a Series for easy access
coffee_row = df[df['Ingredient'] == 'Coffee Beans'].iloc[0]

# Instantiate the object using the filtered data
coffee_obj = Ingredient(
    name=coffee_row['Ingredient'],
    quantity=coffee_row['Current_Quantity']
)
# --- Simulation ---
# Using 2.5 kg of beans
coffee_obj.use_item(2.5)

# --- Updating and Saving ---
# Use .loc to find the row where Ingredient is 'Coffee  Beans'
# and update the 'Current_Quantity' column
df.loc[df['Ingredient'] == 'Coffee Beans', 'Current_Quantity'] = coffee_obj.quantity

# Save the updated report df.to_csv('evening_stock.csv', index=False)

print("\nInventory updated successfully. 'evening_stock.csv' generated.")
print(df)




