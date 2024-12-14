import numpy as np
import csv
import matplotlib.pyplot as plt
from datetime import datetime


times = list()
bgs = list()

with open('test_data\CSV_morrisseyjackson_92442310_14Dec2024_1116.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        times.append(datetime.fromisoformat(row['EventDateTime']))
        bgs.append(int(row['Readings (mg/dL)']))


fig, ax = plt.subplots()
ax.plot(times, bgs)

plt.show()