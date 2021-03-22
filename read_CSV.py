import csv

with open('Users.csv', 'r') as f:
    csv_reader = csv.reader(f)

    with open('New_Users.csv', 'w', newline='') as new_file:
        csv_writer = csv.writer(new_file, delimiter='|')

        for line in csv_reader:
            csv_writer.writerow(line)

with open('Users.csv', 'r') as f:
    csv_reader = csv.DictReader(f)

    for line in csv_reader:
        print(line['Email'])
# DictWriter method with all headers in new csv file
with open('Users.csv', 'r') as f:
    csv_reader = csv.DictReader(f)

    with open('DitcWriter_New_Users.csv', 'w', newline='') as new_dict_writer_file:
        field_names = ['Fname', 'Lname', 'Email']
        csv_writer = csv.DictWriter(new_dict_writer_file, fieldnames=field_names, delimiter='|')

        csv_writer.writeheader()
        for line in csv_reader:
            csv_writer.writerow(line)

# DictWriter method with some headers removed in new csv file
with open('Users.csv', 'r') as f:
    csv_reader = csv.DictReader(f)

    with open('Removed_Email_New_Users.csv', 'w', newline='') as Removed_Email_New_Users:
        field_names = ['Fname', 'Lname']
        csv_writer = csv.DictWriter(Removed_Email_New_Users, fieldnames=field_names, delimiter='|')

        csv_writer.writeheader()
        for line in csv_reader:
            del line['Email']
            csv_writer.writerow(line)

