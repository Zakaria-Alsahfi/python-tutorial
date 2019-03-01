'''How to Read, Parse, and Write CSV Files'''
import csv
# to read csv file
# with open('names.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     # to skip the value line
#     next(csv_reader)
#     for line in csv_reader:
#         # to print all values
#         # print(line)
#         # to print by index value
#         print(line[2])
#-----------------------------------------------------
# to write to a csv file
# with open('names.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     with open('new_names.csv', 'w') as new_file:
#         csv_writer = csv.writer(new_file, delimiter='\t')
#         for line in csv_reader:
#             csv_writer.writerow(line)
#-----------------------------------------------------
# if the delimiter in the csv file is not a comma we must explicitly pass in that we want a specific delimiter
# with open('new_names.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter='\t')
#     for line in csv_reader:
#         print(line)
#-----------------------------------------------------
# using dictionary reader
# with open('names.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     for line in csv_reader:
#         # print(line)
#         print(line['email'])
# using this render method makes reader a lot easier to parse out the information that we want. in the reguler reader method we use index number to find a vlue nut with this method we just use the key value in the dictionary.
#-----------------------------------------------------
# using dictionary writer
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    with open('new_names.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name', 'email']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
        # to print with header
        csv_writer.writeheader()
        for line in csv_reader:
            csv_writer.writerow(line)
#-----------------------------------------------------
