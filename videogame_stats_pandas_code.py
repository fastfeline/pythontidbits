#Video game scores analysis -- made to test some pandas data analysis features.
#This is my first time using pandas, so there might be a few bugs.
#Video game scores and other data were created by me and are not from a real study.
#Code partially based off of pandastest.py by ArcticFox9

#import pandas
import pandas as pd

#reference the CSV file
df = pd.read_csv ("videogame_stats_pandas.csv")

#Title
print("Video Game Scores Analysis")

#Calculate how many data points
number_of_users = df.shape[0]
print ("Analyzing", number_of_users, "users and their scores.")

average_practice_hours = df['practicehours'].mean() #find the average (mean) number of hours practiced
average_score = df['averagescore'].mean() #find the average of each person's average score
average_high_score = df['highscore'].mean() #find the average of each person's high score
print("The average person practiced for", average_practice_hours, "hours, scored an average of", average_score, "points, and had a high score of", average_high_score, "." )

#Add up all the high scores:
high_score_sum = df['highscore'].sum()
print ("The sum of all the high scores is:", high_score_sum)
