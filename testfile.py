import csv
from DictHash import DictHash
drama_dict = DictHash()
with open("kdrama.csv", newline="") as csvfile:
    linereader = csv.reader(csvfile, delimiter=',')
    next(csvfile)
    for row in linereader:
        drama_dict.store(row[0], row[1:])

print(drama_dict.search("The bride of Habaek"))
print(drama_dict["Warm and cozy"])
print(drama_dict.search("Hej"))
print(drama_dict["Hej"])