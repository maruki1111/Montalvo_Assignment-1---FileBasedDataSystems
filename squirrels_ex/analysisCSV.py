#native python approach: https://docs.python.org/3/library/csv.html
import csv

def load_csv(filepath):
    data = []

    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)

    return data


# Example usage
squirrels = load_csv("squirrel.csv")
# prints the entire list of dictionaries (each data row is a dict object, together 
# the entire dataset is a list of dictionaries)
#print(squirrels)

#prints first number of rows specified
#print(squirrels[:2])

#print the first row etc . . . 
#print(squirrels[0])

#slices 
#print(squirrels[10:20])

#see columns in dataset
#print(squirrels[0].keys())

#print data in a column
#for row in squirrels:
#    print(row["Age"])
#

#print only the first 10 rows of Age
#for row in squirrels[:10]:
#    print(row["Age"])

#slice Age
#for row in squirrels[3:20]:
#    print(row["Age"])

#print multiple columns 
#for row in squirrels[:10]:
#    print(row["Age"], row["Primary Fur Color"], row["Foraging"])

#print the first 10 rows from three columns
#for row in squirrels[:10]:
#    print(
#        row["Age"],
#        row["Primary Fur Color"],
#        row["Foraging"]
#    )


#show me where all the grey squirrels were spotted
#for row in squirrels:
#    if row["Primary Fur Color"] == "Gray":
#        print(row["X"], row["Y"])


#how many grey squirrels are there?
count = 0

for row in squirrels:
    if row["Primary Fur Color"] == "Gray":
       count += 1

print(count)

#how many adults vs how many juvenile?
adult_count = 0
juvenile_count = 0

for row in squirrels:
    if row["Age"] == "Adult":
        adult_count += 1
    elif row["Age"] == "Juvenile":
        juvenile_count += 1

print("Adults:", adult_count)
print("Juveniles:", juvenile_count)

#how many adult vs how many juvenile GREY squirrels
adult_gray = 0
juvenile_gray = 0

for row in squirrels:
    if row["Primary Fur Color"] == "Gray":
        if row["Age"] == "Adult":
            adult_gray += 1
        elif row["Age"] == "Juvenile":
            juvenile_gray += 1

print("Adult gray squirrels:", adult_gray)
print("Juvenile gray squirrels:", juvenile_gray)










