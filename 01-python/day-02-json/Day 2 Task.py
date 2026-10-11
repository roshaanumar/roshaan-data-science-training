#load data
import json
f = open("users.json", "r")
data = json.load(f)
#Find unique countries
distinct_country = []
for record in data:
    value = record["country"]
    if value not in distinct_country:
        distinct_country.append(value)
print(distinct_country) 
#count records
def count_records(data):
    return len(data) 
print(count_records(data))
#Filter records
for record in data:
    if record["status"] == "active" and record["age"] > 30:
        print("Status: active" + " Age: " + str(record["age"]))
    elif record["status"] == "pending" or record["age"] > 35:
        print("Status: pending" + " Age: " + str(record["age"]))
    else:
        print("Status: inactive" + " Age: " + str(record["age"]))
#Search name
input_name = input("Enter a name to search: ")
if input_name in [record["name"] for record in data]:
    print("Found " + input_name)
else:
    print("Not found " + input_name)
#Remove duplicates
print("Before removing duplicates: " + str(len(data)))
unique_records = []
for record in data:
    if record not in unique_records:
        unique_records.append(record)
        x = unique_records 
        data = x
print("After removing duplicates: " + str(len(data)))
f.close()