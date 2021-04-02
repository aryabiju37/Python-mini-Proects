from csv import writer,DictWriter
# with open("Cats.csv","w") as file:
#     csv_writer = writer(file)
#     csv_writer.writerow(["Name","Breed","Age"])
#     csv_writer.writerow(["Garfield","Orange Taby",11])


with open("Kitty.csv","w") as file:
    headers = ["Name","Breed","Age"]
    csv_writer = DictWriter(file,fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerow(
        {
            "Name":"George",
            "Age":"1.5 months",
            "Breed":"Tom cat"
        }
    )
    csv_writer.writerow(
        {
            "Name":"Ezra",
            "Age":"2 months",
            "Breed":"Tabby cat"
        }
    )
