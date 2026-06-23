import csv

logs = []

with open("security_logs.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        logs.append(row)

print("Total log entries:", len(logs))