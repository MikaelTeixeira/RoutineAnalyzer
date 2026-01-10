import pandas as pd

def show_activity_percentage(dataframe, week_days: list):
    
    print(f"\nTOTAL ACTIVITIES PER DAY")

    total_week_activities = 0
    week_count = {}
    df = dataframe

    for day in week_days:
        total_activities = df[f"{day}"].count()
        total_week_activities += total_activities

        count = df[f"{day}"].value_counts()

        print(f"\n{day.upper()}")

        for activity, activity_amount in count.items():
            
            if activity in week_count:
                week_count[activity] += activity_amount
            else:
                week_count[activity] = activity_amount

            percent = (activity_amount / total_activities) * 100

            print(f"{activity.title()} = {activity_amount} hours ({percent:.2f}%)")

    print(f"\n{'=' * 32}")
    print(f"WEEKLY ACTIVITY REPORT")
    print(f"{'=' * 32}")

    for activity_name, activity_count in week_count.items():
        percent = (activity_count / total_week_activities) * 100
        print(f"'{activity_name.title()}' represents {percent:.2f}% of total week activities.")

df_name = "RoutineAnalyzer Week days template.csv"

df = pd.read_csv(df_name)

df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

''' df.map iterates through each individual cell of my dataframe; by applying .strip(), it removes leading and trailing whitespaces from every cell.

Lambda is an anonymous function. In short: you don't need to define a formal function for this specific task. It is ideal to use Lambda when a function won't be reused, as it is faster and more practical. If I needed to clean multiple CSVs, creating a dedicated function would be a better approach.

In this example, it removes double spaces if the cell contains a string. If it doesn't, it returns the cell as is.

NOTE: I'm just adding a description because I'm learning how to use Lambda and some functions from pandas. '''


ENGLISH_WEEK_DAYS = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

PORTUGUESE_WEEK_DAYS = ["SEGUNDA", "TERÇA", "QUARTA", "QUINTA", "SEXTA", "SÁBADO", "DOMINGO"]


show_activity_percentage(df, ENGLISH_WEEK_DAYS)