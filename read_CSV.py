import csv

with open('Users.csv', 'r') as f:
    csv_reader = csv.reader(f)

    with open('New_Users.csv', 'w', newline='') as new_file:
        csv_writer = csv.writer(new_file, delimiter='|')

        for line in csv_reader:
            csv_writer.writerow(line)