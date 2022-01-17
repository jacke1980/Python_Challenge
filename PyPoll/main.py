import os
import csv
import pandas as pd

#Reference to Poll csv file
Poll_Path = os.path.join("Resources", "election_data.csv")
Poll_Path_df = pd.read_csv(Poll_Path, encoding="utf-8")
Poll_Path_df.head()

#Total Votes
Votes = len(Poll_Path_df)
print(Votes)

#Finding candidates
Candidates=list(Poll_Path_df["Candidate"].unique())
print(Candidates)

#Finding votes by candidate
Vote_chart=Poll_Path_df["Candidate"].value_counts()
print(Vote_chart)

#Finding the Winner
Winner=Candidates[0]
print("The winner is: "+ Winner)