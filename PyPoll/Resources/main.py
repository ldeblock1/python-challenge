import os
import csv

election_data = []
csv_path = os.path.join("..","python-challenge","PyPoll","Resources","election_data.csv")

with open(csv_path) as csvfile:
    election_data_read = csv.reader(csvfile, delimiter=",")
    next(election_data_read)

    for row in election_data_read:
        election_data.append(row)

#Total number of votes cast
    total_votes = len(election_data)

#The Candidates and their votes recieved
    Candidate_Dict = {}
    Candidate_count = 0
    for rows in election_data:

        Current_Candidate = rows[2]
        
        if Current_Candidate in Candidate_Dict:
            Candidate_Dict[Current_Candidate] += 1
        else:
            Candidate_Dict[Current_Candidate] = 1


    Candidates = list(Candidate_Dict)
    results = ""
    Winner = ""
    max_votes = 0
    for candidate in Candidates:
        percent_share = (Candidate_Dict[candidate]/total_votes) * 100
        results += (f"{candidate}: {Candidate_Dict[candidate]} ({round(percent_share,2)}%)\n\n" )

        if Candidate_Dict[candidate] > max_votes:
            max_votes = Candidate_Dict[candidate]
            Winner = candidate


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

print(output)

output_path = os.path.join("..","python-challenge","PyPoll","Resources", "output.txt")
with open(output_path, 'w') as file:
    file.write(output)
