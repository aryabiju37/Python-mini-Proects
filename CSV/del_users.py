import csv

def delete_user(fname,lname):
    with open("users.csv","r") as file:
        csv_reader = csv.reader(file)
        rows = list(csv_reader)

    count = 0
    with open("users.csv","w") as wfile:
        csv_writer = csv.writer(wfile)
        for row in rows:
            if row[0]==fname and row[1]==lname:
                count += 1
            else:
                csv_writer.writerow(row)
        return "Users Deleted: {}".format(count)