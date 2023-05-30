#it is a ball-by-ball dataset so its has 240 data for a single match
#also there are nearly 12 seasons in this dataset

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
import numpy as np

# Load IPL data from a CSV file
ipl_data = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/IPL/IPL Ball-by-Ball 2008-2020.csv')

# Print the first few rows of the data
# print(ipl_data.head())

# Perform basic analysis
total_matches = len(ipl_data)
total_teams = ipl_data['batting_team'].nunique()
total_players = ipl_data['batsman'].nunique()

print(f"Total Matches: {total_matches}")
print(f"Total Teams: {total_teams}")
print(f"Total Players: {total_players}")

# Calculate the number of matches for each team
matches_per_team = ipl_data['batting_team'].value_counts() // 240

# Round up the values to the next integer
matches_per_team = np.ceil(matches_per_team).astype(int)

# Print the result
print(matches_per_team)

# Find the maximum run scorer
max_run_scorer = ipl_data.groupby('batsman')['batsman_runs'].sum().idxmax()

# Find the team with the most matches
team_with_most_matches = ipl_data['batting_team'].value_counts().idxmax()

print(f"Maximum Run Scorer: {max_run_scorer}")
print(f"Team with the Most Matches: {team_with_most_matches}\nMaximum Matches: {matches_per_team.max()}")

# Find the top 10 run scorers
top_10_run_scorers = ipl_data.groupby('batsman')['batsman_runs'].sum().nlargest(10)
print(top_10_run_scorers)

# Visualize top 10 run scorers
plt.figure(figsize=(10, 6))
sns.barplot(x=top_10_run_scorers.index, y=top_10_run_scorers.values)
plt.xlabel('Batsman')
plt.ylabel('Number of Runs')
plt.title('Top 10 Run Scorers in IPL')
plt.xticks(rotation=90)
plt.show()

# Visualize team with the most wins
plt.figure(figsize=(8, 6))
sns.countplot(x='batting_team', data=ipl_data)
plt.xlabel('Team')
plt.ylabel('Number of Wins')
plt.title('Team with the Most Wins in IPL')
plt.xticks(rotation=90)
plt.show()

#New Dataset
ipl_data2 = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/IPL/IPL Matches 2008-2020.csv')

# Visualize the count of matches played in each city
plt.figure(figsize=(10, 6))
sns.countplot(x='city', data=ipl_data2)
plt.xticks(rotation=90)
plt.xlabel('City')
plt.ylabel('Match Count')
plt.title('Number of Matches Played in Each City')
plt.show()

# Visualize the count of matches played on each date
plt.figure(figsize=(10, 6))
sns.countplot(x='date', data=ipl_data2)
plt.xticks(rotation=90)
plt.xlabel('Date')
plt.ylabel('Match Count')
plt.title('Number of Matches Played on Each Date')
plt.show()

# Visualize the count of player of the match awards
plt.figure(figsize=(10, 6))
sns.countplot(x='player_of_match', data=ipl_data2)
plt.xticks(rotation=90)
plt.xlabel('Player')
plt.ylabel('Award Count')
plt.title('Number of Player of the Match Awards')
plt.show()

# Visualize the count of matches won by each team
plt.figure(figsize=(10, 6))
sns.countplot(x='winner', data=ipl_data2)
plt.xticks(rotation=90)
plt.xlabel('Team')
plt.ylabel('Match Win Count')
plt.title('Number of Matches Won by Each Team')
plt.show()