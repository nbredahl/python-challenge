import os
import csv

# Path to collect data from the csv file
election_data_csv = os.path.join('..', 'Data', 'election_data.csv')

# Open file into cvs reader
with open(election_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# Create dictionary to hold vote count
    candidates = {}

# Skip the header and loop through data to count votes for each candidate (values for the candidate key)
    next(csvreader)
    for row in csvreader:
        if row[2] not in candidates.keys():
            candidates[row[2]] = 0
        candidates[row[2]] = candidates[row[2]] + 1
        
    # Create total votes variable to count votes for candidates in dictionary    
    totalvotes=0

    for votes in candidates.values():
        totalvotes = totalvotes + votes

# Create text file and print total votes
text_file = open("election_analysis.txt", "w")
print(" ")
text_file.write(" \n")
print("Election Results")
text_file.write("Election Results\n")
print("------------------------")
text_file.write("------------------------\n")
print("Total Votes: " + str(totalvotes))
text_file.write("Total Votes: " + str(totalvotes) + "\n")
print("------------------------")
text_file.write("------------------------\n")

# Calculate each candidate's percentage of total votes, determine winner, and print
for each, votes in candidates.items():
    percentage = votes / totalvotes
    print(each + ": " + '{:.1%}'.format(votes/totalvotes) + " (" + str(votes) + ")")
    text_file.write(each + ": " + '{:.1%}'.format(votes/totalvotes) + " (" + str(votes) + ")\n")
print("------------------------")
text_file.write("------------------------\n")
    
mostvotes = 0
for name in candidates.keys():
    if candidates[name] > mostvotes:
        winner = name
        mostvotes= candidates[name]
print("Winner: " +winner)
text_file.write("Winner: " + winner + "\n") 
print("------------------------")
text_file.write("------------------------\n")
text_file.close()