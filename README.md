[README.md](https://github.com/user-attachments/files/24918931/README.md)

(This may be better to read in code, the preview looks wrong and a bit messy)



# Human Decision Fatigue Dataset - Data Questions and Write-up
https://www.kaggle.com/datasets/sonalshinde123/human-decision-fatigue-behavioral-dataset/data


## Why I Chose This Dataset
I chose this dataset because I have strong interests in cognitive psychology and psychological research, 
and because the columns included seemed like they had a really detailed breadth of subjects and variety in the factors that they measured. I was specifically drawn to the fact that it has many different measures for the participants' cognitive loads and lives outside the experiment, measuring cognitive load scores, stress levels 1-10, decision fatigue scores, overall fatigue level, and error rates for stress measures, and hours awake so far, caffeine intake, sleep the night before, and time ofday as supplemental variables. 

## Three Data Questions

### Question 1: Did participants who slept less in general drink more coffee on the day of testing?
---
median_sleep = df["Sleep_Hours_Last_Night"].median()
print(f"Median sleep = {median_sleep} hours")

low = df[df["Sleep_Hours_Last_Night"] < median_sleep]["Caffeine_Intake_Cups"].mean()
high = df[df["Sleep_Hours_Last_Night"] >= median_sleep]["Caffeine_Intake_Cups"].mean()

print("Avg. cups of coffee (sleep below median group):", low)
print("Avg. cups of coffee (sleep = or above median group):", high)

Output: 
Median sleep = 6.1 hours
Avg cups of coffee (sleep below median group): 2.086535303776683
Avg cups of coffee (sleep = or above median group): 1.7173946957878314
---

In general yes, participants who slept less than the median number of hours on average consumed a slightly higher amount of coffee on the day of testing. The data works for this because both columns contain numeric values, so splitting the Sleep_Hours_Last_Night variable into high/low categories based on the median with pandas allows us to then split the coffee counts by these new sleep categories and compute the averages per group. 


### Question 2: At what time of day was the majority of this testing done?
Was most of this testing done during the day or at night?
---
   time_counts = {}
   for time in df["Time_of_Day"]:
       if time in time_counts:
           time_counts[time] += 1
       else:
           time_counts[time] = 1

   print(time_counts)

Output:
{'Evening': 6299, 'Afternoon': 8827, 'Night': 3830, 'Morning': 6044}
---

The data works well for this question because since as the 'Time_of_Day' variable is organized into categories, we can split the column into counts for each category by iterating over each data point and then categorize it by category into a dictionary, and then print all categories' final counts at the end very smoothly.

### Question 3: Does 'Fatigue_Level' influence changes in 'System_Recommendation' variable categorization?
---
print("System recommendations: ")
rec_counts = {}
for rec in df["System_Recommendation"]:
    if rec in rec_counts:
        rec_counts[rec] += 1
    else:
        rec_counts[rec] = 1

print(rec_counts)

cont_low = cont_mid = cont_high = 0
slow_low = slow_mid = slow_high = 0
break_low = break_mid = break_high = 0

for i in range(len(df)):
    rec = df["System_Recommendation"].iloc[i]
    fatigue = df["Fatigue_Level"].iloc[i]

    if rec == "Continue":
        if fatigue == "Low":
            cont_low += 1
        elif fatigue == "Moderate":
            cont_mid += 1
        elif fatigue == "High":
            cont_high += 1

    elif rec == "Slow Down":
        if fatigue == "Low":
            slow_low += 1
        elif fatigue == "Moderate":
            slow_mid += 1
        elif fatigue == "High":
            slow_high += 1

    elif rec == "Take Break":
        if fatigue == "Low":
            break_low += 1
        elif fatigue == "Moderate":
            break_mid += 1
        elif fatigue == "High":
            break_high += 1

print("\n'Continue' → \nLow:", cont_low, "Moderate:", cont_mid, "High:", cont_high)

print("\n'Slow Down' → \nLow:", slow_low, "Moderate:", slow_mid, "High:", slow_high)

print("\n'Take Break' → \nLow:", break_low, "Moderate:", break_mid, "High:", break_high)

Output:
System recommendations: 
{'Continue': 11728, 'Take Break': 8404, 'Slow Down': 4868}

Continue → 
Low: 11728 Moderate: 0 High: 0

Slow Down → 
Low: 1 Moderate: 4867 High: 0

Take Break → 
Low: 0 Moderate: 0 High: 8404
---
The Fatigue_Level variable definitely has something to do with how System_Recommendation splits the data into categories. 

Honestly, I don't think this data is super built to answer this question without deeper analysis, but I do think it's a natural question to ask due to how the data is formatted, and the lack of other info. The 'System_Recommendation' and 'Fatigue_Level' variables are right next to each other in the dataset and I noticed some alignment in the categories, so I wanted to see a bit better if there was real alignment throughout the dataset or only in the pieces that I observed. The dataset also seems to have many other variables that could influence system recommendations, further suggesting this analysis, such as variables like 'Task_Switches', 'Decisions_Made', 'Error_Rate', or 'Stress_Level_1_10'.


### What the data cannot answer

Although the dataset includes the System_Recommendation variable that's mentioned in my Question 3 and I attempt to understand which changes in the data might drive categorical changes for this variable (from Continue, to Slow Down, to Take Break), nowhere in the data or in the explanation of the dataset does the provider include any explanation of how this variable is actually determined, nor how it relates to the experiment itself. I think it would be an interesting variable to look at if it included some sort of label as to which factors influence this variable's categorizations, but as of now with no information, any assumption of where it comes from (maybe without correlational data) without first running tests may cause us to incorrectly assume that *any* of these other variables (which are all related to each other and could intuitively influence a human recommendation to slow down) may be contributing factors to the 'System_Recommendation' variable, when we don't know it's origin or the variable's behaviors whatsoever or really at all beyond Question 3.
