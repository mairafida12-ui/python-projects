import pandas as pd
import os

# Create the initial arrivals.csv file
data = {
    'Flight_Number': [ 'AA123', 'DL456', 'UA789', 'SW101', 'B6202', 'FR555'],
    'Airline': ['American', 'Delta', 'United', 'Southwest', 'JetBlue', 'Ryanair'],
    'Minutes_Delayed': [45, 120, None, 15, None, 75]
}

df_initial = pd.DataFrame(data)
df_initial.to_csv('arrivals.csv', index=False)
print("File 'arrivals.csv' has been created successfully.\n")
import pandas as pd
import os

# --- The Class ---
class Flight:
    def __init__(self, flight_number, delay_time):
        self.flight_number = flight_number
        self.delay_time = delay_time

        def check_severity(self):
            if 30 <= self.delay_time <= 60:
                  print(f"SEVERE WARNING:Flight {self.flight_number} is delayed by {self.delay_time} minutes!.")

# --- Data Cleaning (Pandas) ---
df = pd.read_csv('arrivals.csv')
df['Minutes Delayed'] = df['Minutes_Delayed'].fillna(0)

# ---Integration ---
# Filter for flights delayed by more than 30 minutes
delayed_flights = df[df['Minutes_Delayed'] > 30].copy()

if not delayed_flights.empty:
# Find the most delayed flight top_delayed_row = delayed_flights.loc[delayed_flights['Minutes_Delayed'].idxmax()]

#  Instantiate the Flight object
most_delayed_flight = Flight(top_delayed_row['Flight_Number'], top_delayed_row['Minutes_Delayed'])

# Rum the severity check
most_delayed_flight.check_severity()

# --- Appending (Pandas) ---
# Create a new single_row DataFrame for the log
new_log_entry = pd.DataFrame([{
      'Flight_Number':most_delayed_flight.delay_time,'Timestamp':pd.Timestamp.now()
}])

 log_filename = 'severe_delays_log.csv'

 # Check if log exists to decide whether to read it or start fresh
    if os.path.isfile(log_filename):
        master_log = pd.read_csv(log_filename)
        master_log = pd.concat([master_log, new_log_entry], ignore_index=True)
    else:
        master_log = new_log_entry

        # Save the updated log

master_log.to_csv(log_filename, index=False)
  print(f"\nlog updated: Added{most_delayed_flight.flight_number} to {log_filename}'.")
else:
  print("No significant delays detected today.")