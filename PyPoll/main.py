import os
import csv

# Create a file path for data
election_data = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

# Open and read the data path
with open(election_data, "r") as data_file:
    csvreader = csv.reader(data_file, delimiter = ",")

    # Read Header and create Column Names for the headers.
    csv_header = next(csvreader)
    voter_id = csv_header[0]
    county = csv_header[1]
    candidate = csv_header[2]

    # Total Number of Votes Cast
    voter_id_list = []
    candidate_list = []
    for row in csvreader:
        voter_id_list.append(row[0])
        candidate_list.append(row[2])
    total_voters = "{:,}".format(len(voter_id_list))
    #print(total_voters)

    # Complete list of candidates who received votes
    unique_candidate_list = list(set(candidate_list))
    #print(unique_candidate_list)

    # Total Count and Percentage of votes each cadidate won
    # Khan
    khan_votes = (candidate_list.count("Khan"))
    khan_vote_percent = "{:.3%}".format(khan_votes / len(candidate_list))

    #Li
    li_votes = (candidate_list.count("Li"))
    li_vote_percent = "{:.3%}".format(li_votes / len(candidate_list))

    #O'Tooley
    otooley_votes = (candidate_list.count("O'Tooley"))
    otooley_vote_percent = "{:.3%}".format(otooley_votes / len(candidate_list))

    # Correy
    correy_votes = (candidate_list.count("Correy"))
    correy_vote_percent = "{:.3%}".format(correy_votes / len(candidate_list))

    # Winner of the election based on popular vote
    vote_counter = []
    vote_counter.extend([khan_votes, li_votes, otooley_votes, correy_votes])

    if khan_votes == max(vote_counter):
        winner = "Khan"
    elif li_votes == max(vote_counter):
        winner = "Li"
    elif otooley_votes == max(vote_counter):
        winner = "O'Tooley"
    elif correy_votes == max(vote_counter):
        winner = "Correy"

    # Display final analysis of election data
    results =       ("Election Results"
                    "\n-------------------------------------------"
                    f"\nTotal Votes: {total_voters}"
                    "\n-------------------------------------------"
                    f"\nKhan:       {khan_vote_percent}      ({'{:,}'.format(khan_votes)})"
                    f"\nCorrey:     {correy_vote_percent}      ({'{:,}'.format(correy_votes)})"
                    f"\nLi:         {li_vote_percent}      ({'{:,}'.format(li_votes)})"
                    f"\nO'Tooley:   {otooley_vote_percent}       ({'{:,}'.format(otooley_votes)})"
                    "\n-------------------------------------------"
                    f"\nWinner: {winner}"
                    )
    print(results)

    # Write final analysis to 'election_results.txt' file
    election_results = os.path.join("..", "PyPoll", "Analysis", "election_results.txt")
    with open(election_results, "w") as ed:
        ed.write(results)