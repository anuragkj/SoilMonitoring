import csv
import random
from datetime import datetime, timedelta

# Define the start and end dates for the data
start_date = datetime(2023, 4, 1)
end_date = datetime(2023, 4, 20)

# Define the headers for the CSV file
headers = ['Date', 'Time', 'Temperature', 'Humidity', 'Moisture']

# Define the range of values for each column
temp_range = (20.0, 45.0)
humid_range = (50, 70)
moist_range = (800, 900)

# Create a list to store the data
data = []

# Loop through each day
current_date = start_date
while current_date <= end_date:
    # Loop through each time interval
    for i in range(20):
        # Generate random values for each column
        temp = round(random.uniform(*temp_range), 1)
        humid = random.randint(*humid_range)
        moist = random.randint(*moist_range)

        # Format the date and time values
        date_str = current_date.strftime('%m/%d/%Y')
        time_str = current_date.strftime('%H:%M:%S')

        # Append the data to the list
        data.append([date_str, time_str, temp, humid, moist])

        # Increment the time by 30 minutes
        current_date += timedelta(minutes=30)

    # Increment the date by 1 day
    current_date += timedelta(days=1)

# Write the data to a CSV file
with open('random_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)
    writer.writerows(data)
