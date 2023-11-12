# Please note that before running this code, make sure you are having the correct path for your own device.
# If you wanted to run the code in visual studio, if you choose to open only the PyPoll folder, then the path to write your txt file would be: "Analysis","analysis.txt"
# If you chose to open the entire python challenge folder the path would change to: "PyPoll","Analysis","analysis.txt"
# The path depends on where you store these files or you want to store your txt file.

import os
import csv


# Path to collect data from the resources folder
election_data_csv = r"PyPoll\Resources\election_data.csv"


# Lists to store data:
# The list of all the Ballot IDs included in the dataset which also shows the list of votes
Total_ID = []

#List of candidates (No Duplicate)
Candidates = []

# List of total votes for each candidate
Total_Candidate_Vote =[]

# This list contains all the candidates plus their duplicates based on however times a vote is dedicated to them. 
Candidate_vote = []

# This list contains the winning votes percentage of all candidates
Candidate_vote_percentage = []


# Read in the CSV file
with open(election_data_csv, "r") as csvfile:

    # Splits the data on commas
    csvreader = csv.reader(csvfile, delimiter=",")

    # Storing the header row
    header_row = next(csvreader)
    
    # Loop through the data
    for row in csvreader:

        # Adding all the Ballot IDs to the Total_ID list
        Total_ID.append(row[0])

        # Counting the total number of votes included in the dataset
        Total_Votes_Count = len(Total_ID)

        # Adding all the candidates to the Candidates list. The if condition is saying to not add duplicates of the same candidate to the list. 
        if row[2] not in Candidates:
            Candidates.append(row[2]) 

        # Adding all the candidates plus their duplicates based on however times a vote is dedicated to them.
        Candidate_vote.append(row[2])

    # Loop through all the candidates and counts all the duplicate occurrences of the same candidates and adds them to the Total_Candidate_Vote list
    # index shows the location of the item in the list, here our item is the candidate
    for candidate in Candidates:   
        Total_Candidate_Vote.append(Candidate_vote.count(Candidates[Candidates.index(candidate)]))

    # Loop through all the total candidate votes in order to find the percentage of votes each candidate won
    # To find the percentage, the total candidate vote gets divided by the total number of votes and dets multiplied by 100 to have the percentage
    # Code also rounds the final result to have 3 decimal places. Then, the numbers are added to the Candidate_vote_percentage list
    for votes in Total_Candidate_Vote:
        Vote_Percentage = round(float(((Total_Candidate_Vote[Total_Candidate_Vote.index(votes)]) / Total_Votes_Count) * 100) , 3)
        Candidate_vote_percentage.append(Vote_Percentage)

    # The winner of the election is the one with either the highest number of votes or the highest percentage of votes. 
    Winner = Candidates[Candidate_vote_percentage.index(max(Candidate_vote_percentage))]


# Printing all the requested values in the terminal   
print("Election Results")
print("-------------------------")
print(f"Total Votes: {Total_Votes_Count}")
print("-------------------------")
# since the index of each of the candidates and their corresponding vote percentage & total vote number are the same, the for loop is created to print out the results specific to each candidate in the same line.
for index in range(len(Candidates)):
    print(f"{Candidates[index]}: {Candidate_vote_percentage[index]}% ({Total_Candidate_Vote[index]})")
print("-------------------------")
print(f"Winner: {Winner}")
print("-------------------------")


# This creates the analysis.txt file and will add it under the Analysis folder.
Analysis = os.path.join("PyPoll","Analysis","analysis.txt")

# Open the analysis file
with open(Analysis, "w") as txtfile:
    
    # Writes all the requested values and results in the created text file. 
    # "\n" is used to go to the next line
    txtfile.write("Election Results" + "\n")
    txtfile.write("\n")
    txtfile.write("-------------------------" + "\n")
    txtfile.write("\n")
    txtfile.write(f"Total Votes: {Total_Votes_Count}" + "\n")
    txtfile.write("\n")
    txtfile.write("-------------------------" + "\n")
    txtfile.write("\n")
    for index in range(len(Candidates)):
        txtfile.write(f"{Candidates[index]}: {Candidate_vote_percentage[index]}% ({Total_Candidate_Vote[index]})" + "\n")
    txtfile.write("\n")
    txtfile.write("-------------------------" + "\n")
    txtfile.write("\n")
    txtfile.write(f"Winner: {Winner}" + "\n")
    txtfile.write("\n")
    txtfile.write("-------------------------" + "\n")    
        
      



            