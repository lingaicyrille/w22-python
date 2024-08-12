import csv


with open("test.csv",'w',newline='') as f:

    writer = csv.writer(f)
    Header = ['Name', 'Cell', 'Profession', 'Email']
    writer.writerow(Header)
    writer.writerow(['Brandon', '555 555 5555','DevOps Engineer','dkkhg@gmail.com'])