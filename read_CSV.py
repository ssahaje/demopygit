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

with open('Users.csv', 'r') as f:
    csv_reader = csv.DictReader(f)

    with open('DitcWriter_New_Users.csv', 'w', newline='') as new_dict_writer_file:
        field_names = ['Fname', 'Lname', 'Email']
        csv_writer = csv.DictWriter(new_dict_writer_file, fieldnames=field_names, delimiter='|')

        csv_writer.writeheader()
        for line in csv_reader:
            csv_writer.writerow(line)