import csv
from matplotlib import pyplot as plt
from datetime import datetime

# Get dates, low, and high temperatures from file.
filename = 'death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[2], "%Y-%m-%d")
            #print(row[8])
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            lows.append(low)
            highs.append(high)
        

    #print(highs)

# Plot data.
fig = plt.figure(figsize=(10,6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
title = "Daily high and low temperatures - 2018\nDeath Valley, CA"
plt.title(title, fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
