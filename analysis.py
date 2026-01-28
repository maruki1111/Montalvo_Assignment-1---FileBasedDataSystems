import pandas as pd
df = pd.read_csv("human_decision_fatigue_dataset.csv")
print("Shape (rows, columns):", df.shape)
#print(df.head())

#1
print("\n#1: Printing first 2 rows")
print(df[:2])

#2
print("\n#2: Printing only first row")
#print(df.iloc[0])
print(df.iloc[:1])

#3
print("\n#3: Printing rows 10-19")
print(df.iloc[10:20])

#4
print("\n#4: Printing columns")
print(df.columns)

#5
print("\n#5: Printing first 10 rows, of one column")
print(df["Cognitive_Load_Score"].head(10))

#6
print("\n#6: Printing first 10 rows, of 3 columns")
print(df[["Decisions_Made", "Stress_Level_1_10", "Fatigue_Level"]].head(10))


#7a
print("\n#7a, Data Question 1: Did participants who slept less in general drink more coffee on the day of testing?")

median_sleep = df["Sleep_Hours_Last_Night"].median()
print(f"Median sleep = {median_sleep} hours")

low = df[df["Sleep_Hours_Last_Night"] < median_sleep]["Caffeine_Intake_Cups"].mean()
high = df[df["Sleep_Hours_Last_Night"] >= median_sleep]["Caffeine_Intake_Cups"].mean()

print("Avg. cups of coffee (sleep below median group):", low)
print("Avg. cups of coffee (sleep = or above median group):", high)


#7b
print("\n#7b, Data Question 2: At what time of day was the majority of this testing done?")
time_counts = {}
for time in df["Time_of_Day"]:
    if time in time_counts:
        time_counts[time] += 1
    else:
        time_counts[time] = 1

print(time_counts)

#7c
print("\n#7c, Data Question 3: Does 'Fatigue_Level' influence changes in 'System_Recommendation' variable categorization?")

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

print("\nContinue → \nLow:", cont_low,
      "Moderate:", cont_mid,
      "High:", cont_high)

print("\nSlow Down → \nLow:", slow_low,
      "Moderate:", slow_mid,
      "High:", slow_high)

print("\nTake Break → \nLow:", break_low,
      "Moderate:", break_mid,
      "High:", break_high)
