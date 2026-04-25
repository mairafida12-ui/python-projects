import pandas as pd

# Creating Shelter A data
data_a = {
    'Pet_Name' : ['Buddy' , 'Mittens' , 'Rex' , 'Goldie'],
    'Animal_Type' : ['Dog', 'Cat', 'Dog', 'Fish'],
    'Age_Years': [3,2,5,1]
}

# Creating Shelter B data (with some missing values to test cleaning)
data_b = {
    'Pet_Name' : ['Luna' , 'Bella' , 'Charlie' , None],
    'Animal_Type' : ['Cat', 'Dog', 'Dog', 'Dog'],
    'Age_Years': [4,1,7,None]
}

pd.DataFrame(data_a).to_csv('shelter_a.csv', index=False)
pd.DataFrame(data_b).to_csv('shelter_b.csv', index=False)
class RescuePet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
        self.is_adopted = False

    def process_adoption(self):
        self.is_adopted = True
        print(f"Success! {self.name} the {self.species} has been adopted.")
# --- Combining Data ---
df_a = pd.read_csv('shelter_a.csv')
df_b = pd.read_csv('shelter_b.csv')

# Merge and reset index to ensure a clean, continuous count combined_df = pd.concat([df_a, df_b], ignore_index=True)

# --- Data Cleaning ---
# Remove any rows with NaN values cleaned_df = combined_df.dropna()

# Filter to show only the dogs
dogs_df = cleaned_df[cleaned_df['Animal_Type'] == 'Dog']

# --- Integration ---
# We'll pick the first dog from our filtered list
target_dog = dogs_df.iloc[0]

# Instantiate the object using data from the DataFrame
adopted_pet = RescuePet(name=target_dog['Pet_Name'],

species= target_dog['Animal_Type'],
    age= target_dog['Age_Years']
                        )
# Process the adoption
adopted_pet.process_adoption()

# Create a small dictionary for the newly adopted pet
adoption_record = {
    'Pet_Name' : [adopted_pet.name],
    'Animal_Type' : [adopted_pet.species],
    'Age_Years': [adopted_pet.age],
    'Adoption_Status': [adopted_pet.is_adopted]
}

# Convert to DataFrame
final_export_df = pd.DataFrame(adoption_record)

# Export using append mode
# Note: header=False is used if the file already exists to avoid duplicate headers
import os
file_exists = os.path.isfile('successfull_adoption.csv')

final_export_df.to_csv('successfull_adoption.csv',
                       mode='a' , index=False,
                       header=not file_exists)
print("Adoption record appended to successfull_adoption.csv")





