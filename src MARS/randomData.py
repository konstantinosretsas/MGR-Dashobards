import random
import csv
import datetime
import string
import pandas


# Enter the start and end date of the dates that will be created randomly
start_date = datetime.date(2023,3,29)
end_date = datetime.date(2024,3,28)

# Relative path
postcodes_file_path = "data/500postcodes.csv"
resources_file_path = "data/resources.csv"
contractor_file_path = "data/contractor.csv"
works_file_path = "data/work_description.csv"

# postcode list creation
with open(postcodes_file_path, 'r') as csvfile:
    reader = csv.reader(csvfile)

    count = 0
    Postcodes_list = []

    for row in reader:
        count = count + 1
        # print(row[0])
        Postcodes_list.append(row[0])

# resource list creation
with open(resources_file_path, 'r') as csvfile:
    reader = csv.reader(csvfile)

    count1 = 0
    Resources_list = []

    for row in reader:
        count1 = count1 + 1
        Resources_list.append(row[0]) 

# contractor list creation
with open(contractor_file_path, 'r') as csvfile:
    reader = csv.reader(csvfile)

    count2 = 0
    contractor_list = []

    for row in reader:
        count2 = count2 + 1
        # print(row[0])
        contractor_list.append(row[0])

# works list creation
with open(works_file_path, 'r') as csvfile:
    reader = csv.reader(csvfile)

    count3 = 0
    works_list = []

    for row in reader:
        count3 = count3 + 1
        # print(row[0])
        works_list.append(row[0])

data = []
for i in range(500):
    cwChoices = ["No", "Yes"]
    statusChoices = ["Authorised","Authorised","Rejected"]
    WorkStreamChoices = ["WS1","WS2","WS3"]
    rejectedchoices = ["Yes", "No"]
    # MGR_BE_Number Format
    lst1 = random.choices('123456', k=8)
    lst2 = []
    for j in range(0, len(lst1), 2):
        lst2.append(lst1[j] + lst1[j+1])

    Project_number = ''.join(random.choices('0123456789', k=8))
    Lot = random.randint(0, 4)
    Supplier = "KR Analytics Ltd"
    Deliverable = 'MARS Review'
    MGR_BE_Number = '.'.join(lst2)
    Location = Postcodes_list[i]
    Resource = Resources_list[(int("".join(random.choices("0123456789", k=1))))]
    Contractors_Name = contractor_list[(int("".join(random.choices("012345678", k=1))))]
    CW = cwChoices[(int("".join(random.choices("01", k=1))))]
    Work_des = works_list[(int("".join(random.choices("012345678", k=1))))]
    Year = 3
    Date_Received = start_date + datetime.timedelta(days=random.randint(1, (end_date - start_date).days)) 
    Date_Reviewed = Date_Received + datetime.timedelta(days=random.randint(1, 14)) 
    Duration = Date_Reviewed - Date_Received
    Status = statusChoices[(int("".join(random.choices("02", k=1))))]
    if Status=="Authorised":
        Authorised = "N/A"
    elif Status=="Rejected":
        Authorised = rejectedchoices[(int("".join(random.choices("01", k=1))))]
    if Status=="Authorised" and Authorised == "N/A":
        Invoice = "Yes"
    else: Invoice="No"
    Comments = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
    WorkStream = WorkStreamChoices[(int("".join(random.choices("02", k=1))))]
    data.append([Project_number, Lot, Supplier, Deliverable, MGR_BE_Number, Location, Resource, Contractors_Name, CW, Work_des, Year, Date_Received,Date_Reviewed,Duration, Status, Authorised,Invoice,Comments,WorkStream])

# Define the filename to save the data to
filename = 'MARS Tracker.csv'

# Open the file in write mode and create a CSV writer object
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(['Project number', 'Lot', 'Supplier', 'Deliverable','MGR BE Number', 'Location', 'Resource', 'Contractors Name','CW', 'Work Description (e.g. Roof Works)','Year', 'Date Received','Date Reviewed', 'Duration between receipt/review','Status (Authorised or Rejected with amendments Req)','Has been authorised eventually?','Invoiced to MGR?', 'Comments', 'Work Stream'])

    # Write each row of data
    for row in data:
        writer.writerow(row)

# Get the postcodes from the other csv file

print("Random data saved to", filename)
