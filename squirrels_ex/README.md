# Central Park Squirrel Census (2018) — Three Data Questions
#edstem workspace link: https://edstem.org/us/courses/91931/workspaces/pyrPXkGC6Ul2skYNCUG1jN6zNxZ89x4M

## Why I Chose This Dataset
I chose the Central Park Squirrel Census dataset because it’s real, local (NYC), 
and easy to understand: each row represents a squirrel sighting, and the columns describe 
attributes of that sighting (like fur color, age, and location). 
It’s also a good example of a dataset that supports interesting questions, while still having clear 
limits (e.g., “Age” is a category, not a number).

And it has an associated web output: https://www.thesquirrelcensus.com/

---

## Three Data Questions

# Question: How many gray squirrels are there?
#count = 0
#for row in squirrels:
#    if row["Primary Fur Color"] == "Gray":
#       count += 1
#print(count)
#output: 2473

Why the data structure supports this question:
This works because the dataset is tabular: each row is one squirrel sighting, 
and the Primary Fur Color column stores a categorical label for fur color. 
Counting the rows where that column equals "Gray" gives the total number of gray squirrel
sightings.

# Question: How many Adult vs Juvenile squirrels are there overall?
#adult_count = 0
#juvenile_count = 0

#for row in squirrels:
#    if row["Age"] == "Adult":
#        adult_count += 1
#    elif row["Age"] == "Juvenile":
#        juvenile_count += 1

#print("Adults:", adult_count)
#print("Juveniles:", juvenile_count)
#output: Adults: 2568 Juveniles: 330

Why the data structure supports this question:
This works because Age is a single column that categorizes each row (sighting) as Adult, Juvenile, or blank/unknown. 
Since each row is one observation, counting the frequency of each category summarizes how many sightings fall into each 
age group.

# Question: How many Adult vs Juvenile gray squirrels are there?
#adult_gray = 0
#juvenile_gray = 0

#for row in squirrels:
#    if row["Primary Fur Color"] == "Gray":
#        if row["Age"] == "Adult":
#            adult_gray += 1
#        elif row["Age"] == "Juvenile":
#            juvenile_gray += 1

#print("Adult gray squirrels:", adult_gray)
#print("Juvenile gray squirrels:", juvenile_gray)
#output: Adult gray squirrels: 2125 Juvenile gray squirrels: 256

Why the data structure supports this question:
This works because we can filter rows using one column (Primary Fur Color == "Gray") and then summarize a second column (Age).
The dataset’s “one row = one sighting” structure makes it possible to combine conditions and get category counts within a 
subset of the data.


What the Data Cannot Answer

A question I might want to answer is: “What is the exact oldest squirrel in Central Park?” This dataset cannot answer that 
because the Age column is not a numeric age (like years); it only provides categories (Adult and Juvenile) and sometimes 
missing values. The data also can’t tell us anything about an individual squirrel’s lifespan or whether the same squirrel 
appears in multiple rows, because sightings are not guaranteed to be unique individuals. It would be misleading to assume 
that “Adult” means a specific age or that each row represents a different squirrel with no repeats.







