from csv import writer
with open("Cats.csv","w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Name","Age"])
    csv_writer.writerow(["Ryu","3"])
    csv_writer.writerow(["Kitty","1"])