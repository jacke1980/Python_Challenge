#import packages 
import csv
import os

#define function to fix percentage format to 3 decimal points 
def fixPercent(num):
    num = "{:.3%}".format(num)
    return num

input_file = os.path.join("Resources", "election_data.csv")
output_file = os.path.join("Analysis", "pyPoll_analysis.txt")


#create empty lists and variables for storing data #
Candidates = []
VoteCounts = []
VotePercent = []
TotalVotes = 0
WinnerCount = 0

#read the CSV file 
with open(input_file, 'r') as election_data:
    reader = csv.reader(election_data, delimiter=",")

    Headers = next(reader)

#for loop to go through each row in the CSV file and count the total number of votes 

    for row in reader:
        TotalVotes += 1
    
#get candidate names and individual vote counts and store in lists
        if row[2] not in Candidates:

#append the name to Candidates and a value of 1 to VoteCounts list
            Candidates.append(row[2])
            VoteCounts.append(1)

#if row[2] (candidate name) is in the Candidates list
        else:

# get the index of the candidate from the Candidates list in order to increase the vote count by 1
            CandidateIndex = Candidates.index(row[2])
            VoteCounts[CandidateIndex] += 1
        

# calculate percentage of votes for each candidate 
for i in range(len(VoteCounts)):
    VotePercent.append(VoteCounts[i] / TotalVotes)

# calculate the winner based on most votes 
for i in range(len(VoteCounts)):

# if the number of votes is greater than WinnerCount (initially zero)
    if VoteCounts[i] > WinnerCount:
        
#update WinnerCount to the number of votes at index i
        WinnerCount = VoteCounts[i]

#update Winner to the candidate name at index i
        Winner = Candidates[i]

#create a text file with the analysis output 
with open(output_file, 'w') as textfile:
    textfile.write(f"Election Results\n"
                   f"----------------------------\n"
                   f"Total Votes: {TotalVotes}\n"
                   f"----------------------------\n"
                   )

# for loop to iteratively write each candidate's info
    for i in range(len(Candidates)):
        textfile.write(f"{Candidates[i]}: {fixPercent(VotePercent[i])} ({VoteCounts[i]})\n")

    textfile.write(f"----------------------------\n"
                   f"Winner: {Winner}\n"
                   f"----------------------------\n"
                  )

#read the output file and print analysis to terminal 
with open (output_file, 'r') as analysis:
    results = analysis.read()
    print(results)