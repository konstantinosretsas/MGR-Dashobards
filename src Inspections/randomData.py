import random
import csv
import datetime
import string
import pandas


# Enter the start and end date of the dates that will be created randomly
start_date = datetime.date(2023,3,29)
end_date = datetime.date(2024,3,28)

mid_date = datetime.date(2023,10,1)
start_date2 = datetime.date(2023,3,29)

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

data = []
for i in range(500):
    hubchoices = ["Green", "Red","Blue"]
    invoicechoices = ["Yes", "No"]
    batches = ["1", "2"]
    startingdate = [start_date2,mid_date]
    # BE_Number Format
    lst1 = random.choices('123456', k=8)
    lst2 = []
    for j in range(0, len(lst1), 2):
        lst2.append(lst1[j] + lst1[j+1])

    
    BE_Number = '.'.join(lst2)
    Location = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
    PI_Ref = "".join(random.choices("012345678", k=4))
    Post_Code = Postcodes_list[i]
    Prog_Yr = 3
    Hub=hubchoices[(int("".join(random.choices("02", k=1))))]
    Resource = Resources_list[(int("".join(random.choices("0123456789", k=1))))]
    Starting_date = startingdate[(int("".join(random.choices("01", k=1))))]
    
    # Visit Dates
    if abs(Starting_date-start_date)==0:
        Visit_date = start_date + datetime.timedelta(days=random.randint(1, (end_date - start_date).days))
    else:
        Visit_date = Starting_date+ datetime.timedelta(days=random.randint(1, (end_date - Starting_date).days))

    Peer_Reviewer = Resources_list[(int("".join(random.choices("0123456789", k=1))))]
    Date_Reviewed = Visit_date + datetime.timedelta(days=random.randint(1, 14)) 
    Report_Issued = Date_Reviewed + datetime.timedelta(days=random.randint(1, 14))
    InvoicetoMGR = invoicechoices[(int("".join(random.choices("01", k=1))))]
    Property_archived = ""
    Aborted = Visit_date
    Additional_photos = ""
    Photos_notuploading = ""
    reports_uploaded = ""
    properties_notcommunicated = ""
    Access_denied = ""
    Comments = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
    Visit_date2 = ""
    Property_batch = batches[(int("".join(random.choices("01", k=1))))]
    outstanding = ""
    data.append([BE_Number, Location, PI_Ref, Post_Code, Prog_Yr, Hub, Resource, Starting_date, Visit_date, Peer_Reviewer, Date_Reviewed, Report_Issued,InvoicetoMGR,Property_archived,Aborted,Additional_photos,Photos_notuploading,reports_uploaded,reports_uploaded,properties_notcommunicated,Access_denied,Comments,Visit_date2,Property_batch,outstanding])

# Define the filename to save the data to
filename = 'PI Tracker.csv'

# Open the file in write mode and create a CSV writer object
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(["BE Number","Location","PI Ref","Post Code","Prog Yr","Hub","Resource ","Starting Date","Visit Date","Peer Reviewer","Peer Review Date","Report Issued","Invoiced to MGR?","Property Archived (date notified by RMG)","Aborted","Additional photos required","Photos not uploading on app","Report not uploading on app","Report uploaded on app but not on CRD","Properties that are archived not communicated","Access denied" ,"Comments","Visit Date2","Yr 3 Property Batch No.","Outstanding (Reports not issued)"])
    # Write each row of data
    for row in data:
        writer.writerow(row)

# Get the postcodes from the other csv file

print("Random data saved to", filename)
