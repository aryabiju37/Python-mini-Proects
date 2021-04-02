from csv import reader,writer

with open("fighters.csv") as file:
    csv_reader = reader(file)      
    fighters = [[s.upper() for s in row] for row in csv_reader]
    for row in csv_reader:
        print(type(row))

with open("screamingfighter.csv","w") as file:
    csv_writer = writer(file)
    for fighter in fighters:
        csv_writer.writerow(fighter)

with open("fighters.csv") as file:
    csv_reader = reader(file)
    with open("screaming_fighters.csv","w") as file:
        csv_writer = writer(file)
        #print(type(csv_writer))
        for fighter in csv_reader:
            csv_writer.writerow([s.upper() for s in fighter])