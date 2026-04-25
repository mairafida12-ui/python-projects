import pandas as pd
# creating a messy dictionary to represent the raw data
data = {
    'Student_Name' :['Alice', 'Bob', 'Charlie', 'David', 'Eva'] ,
    'Math_Score' :[85, None, 45, 90, 30] ,
    'Science_Score' :[78, 42, None, 95, 20] ,
}

# Save as CSV
df_raw = pd.DataFrame(data)
df_raw.to_csv('raw_grades.csv' , index=False)
print("File 'raw_grades.csv' created successfully")
class Student:
    def __init__(self, name: object, math_score: object, science_score: object) -> None:
        self.name = name
        self.math_score = math_score
        self.science_score = science_score
        self.status = None

    def check_status(self):
        # Calculate average and determine Pass/Fail
        average = (self.math_score+self.science_score) / 2
        if average >= 50:
            self.status = "Pass"
        else:
                self.status = "Fail"
# --- Data Cleaning (Pandas) ---
df = pd.read_csv('raw_grades.csv')
# Filling missing values with 0
df_cleaned = df.fillna(0)


# --- Integration ---
student_objects = []

for index, row in df_cleaned.iterrows():
   # Instantiate Student object
   temp_student = Student(
       name=row['Student_Name'],

math_score=row['Math_Score'],

science_score=row['Science_Score'],
   )
   # Run the logic method
   temp_student.check_status()
   # Store the object
   student_objects.append(temp_student)
# Extracting data from objects
# into a list of dictionaries:
processed_data = []
for s in student_objects:
     processed_data.append({
    "Student_Name": s.name,
    "Math_Score": s.math_score,
    "Science_Score": s.science_score,
    "status": s.status,
     })

# --- Exporting (Pandas)
final_df =pd.DataFrame(processed_data)

# Adding the School_Year column
final_df["School_Year"] = "2023-2024"

# Saving to CSV
final_df .to_csv('final_grades.csv' , index=False)

print("\nProcessing complete! 'final_grades.csv' has been generated.")
print('final_df')
