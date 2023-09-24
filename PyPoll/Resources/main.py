import os
import csv

election_data = []
#Set the path
csv_path = os.path.join("..","python-challenge","PyPoll","Resources","election_data.csv")
# Open the csv file
with open(csv_path) as csvfile:
    election_data_read = csv.reader(csvfile, delimiter=",")
#Skip the headers
    next(election_data_read)
# Add the data to election_data list
    for row in election_data_read:
        election_data.append(row)

#Total number of votes cast
    total_votes = len(election_data)

#The Candidates and their votes recieved in a dictionary
    Candidate_Dict = {}

    for rows in election_data:
#Set the column
        Current_Candidate = rows[2]
# If the current candidate is already in Candidate Dict, add one to it's count attribute. If its the first time seeing a candidate,
# collect the name as the key and set it's number attribute to one.         
        if Current_Candidate in Candidate_Dict:
            Candidate_Dict[Current_Candidate] += 1
        else:
            Candidate_Dict[Current_Candidate] = 1

#
    Candidates = list(Candidate_Dict)
    results = ""
    Winner = ""
    max_votes = 0
#For every candidate in the candidate list, caluclate percent share. Record all of these in results variable
    for candidate in Candidates:
        percent_share = (Candidate_Dict[candidate]/total_votes) * 100
#print the candidate name, value the cadidate is attacked to, and their calculated percent share.
        results += (f"{candidate}: {Candidate_Dict[candidate]} ({round(percent_share,2)}%)\n\n" )
#Find the winner
        if Candidate_Dict[candidate] > max_votes:
            max_votes = Candidate_Dict[candidate]
            Winner = candidate

#Set output variable
output = (
    f"\nElection Results\n\n"
    f"--------------------------------\n\n"
    f"Total Votes Cast: {total_votes}\n\n"
    f"--------------------------------\n\n"
    f"{results}"
    f"--------------------------------\n\n"
    f"Winner: {Winner} with votes: {max_votes}\n\n"
    f"--------------------------------\n"
    )
#print output in terminal
print(output)
#print output in a text file
output_path = os.path.join("..","python-challenge","PyPoll","Resources", "output.txt")
with open(output_path, 'w') as file:
    file.write(output)
