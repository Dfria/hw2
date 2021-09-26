# -------------------------------------------------------------------------
# AUTHOR: Jordan Dallas Frias
# FILENAME: naive_bayes.py
# SPECIFICATION:
# FOR: CS 4210- Assignment #2
# TIME SPENT: 10 hours
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

# importing some Python libraries
import csv
from sklearn.naive_bayes import GaussianNB

# reading the training data
# --> add your Python code here

db = []
with open('weather_training.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            db.append(row)
            # print(row)

# transform the original training features to numbers and add to the 4D array X. For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
# --> add your Python code here
X = []
# transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
# --> add your Python code here
Y = []

for i in db:
    row = []
    for n, a in enumerate(i):
        if n != 0 or n != len(i) - 1:
            if a == "Sunny":
                row.append(1)
            elif a == "Overcast":
                row.append(2)
            elif a == "Rain":
                row.append(3)
            elif a == "Cool":
                row.append(1)
            elif a == "Mild":
                row.append(2)
            elif a == "Hot":
                row.append(3)
            elif a == "Normal":
                row.append(1)
            elif a == "High":
                row.append(2)
            elif a == "Weak":
                row.append(1)
            elif a == "Strong":
                row.append(2)
            if (n == len(i) - 1):
                if a == "Yes":
                    Y.append(1)
                else:
                    Y.append(2)
    X.append(row)

# fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

# reading the data in a csv file
# --> add your Python code here
samples = []
with open('weather_test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            samples.append(row)
            # print(row)

# printing the header os the solution
print("Day".ljust(15) + "Outlook".ljust(15) + "Temperature".ljust(15) + "Humidity".ljust(15) + "Wind".ljust(
    15) + "PlayTennis".ljust(15) + "Confidence".ljust(15))

# use your test samples to make probabilistic predictions.
# --> add your Python code here

for i in samples:
    row = []
    for n, a in enumerate(i):
        if n != 0:
            if a == "Sunny":
                row.append(1)
            elif a == "Overcast":
                row.append(2)
            elif a == "Rain":
                row.append(3)
            elif a == "Cool":
                row.append(1)
            elif a == "Mild":
                row.append(2)
            elif a == "Hot":
                row.append(3)
            elif a == "Normal":
                row.append(1)
            elif a == "High":
                row.append(2)
            elif a == "Weak":
                row.append(1)
            elif a == "Strong":
                row.append(2)

    output = [row]
    predicted = clf.predict_proba(output)[0]

    if predicted[0] >= .75:
        print(i[0].ljust(15) + i[1].ljust(15) + i[2].ljust(15) + i[3].ljust(15) + i[4].ljust(15) + "Yes".ljust(15)
              + str(predicted[0]).ljust(15))
    if predicted[1] >= .75:
        print(i[0].ljust(15) + i[1].ljust(15) + i[2].ljust(15) + i[3].ljust(15) + i[4].ljust(15) + "No".ljust(15)
              + str(predicted[1]).ljust(15))


