import csv 
 
data = [ 
    ["Name", "Role"], 
    ["XYZ", "DevOps Engineer"], 
    ["Rafi", "Security Analyst"] 
] 
 
with open("users.csv", "w", newline="") as f: 
    writer = csv.writer(f) 
    writer.writerows(data)
print("CSV file 'users.csv' created successfully.")

with open("users.csv", "r") as f: 
    reader = csv.reader(f) 
    for row in reader: 
        print(row)
print("CSV file 'users.csv' read successfully.")
