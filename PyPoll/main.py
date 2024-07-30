"""
This script analyzes a dataset of poll data from 'election_data.csv' to calculate key metrics related to the election results:

1. The total number of votes cast.
2. A complete list of candidates who received votes.
3. The percentage of votes each candidate won.
4. The total number of votes each candidate won.
5. The winner of the election based on popular vote.

The script processes the dataset to extract and compute these values, providing a comprehensive summary of the election results.
"""

#Import Modules
import csv
from pathlib import Path


#path variables
election_data_csv = Path('./Resources/election_data.csv')
analysis_txt = Path('./analysis/election_results.txt')

#2 lists for tracking candidates and their vote count
#each candidate will be assigned their own index. 
candidates = []
votes = []


with open(election_data_csv, 'r') as source:
	csvreader = csv.reader(source,delimiter=',')
	
	header = next(csvreader)
	
	
	for row in csvreader:
	
		if row[2] in candidates:
			#if we've already collected the candidate, increment their vote count up 1
			index = candidates.index(row[2])
			votes[index] += 1
		else:
			#if this is the first time we are seeing this
			#candidate, create an index
			index = len(candidates)
			candidates.append(row[2])
			votes.append(1)

#Find who the winner is
winner_index = votes.index(max(votes))



#------------------
#Return the results to command line
print(
	'Election Results\n'
	'--------------------\n'
	f'Total Votes: {sum(votes)}\n'
	'--------------------\n'
)

#This will dynamically output each candidate and their votes. 
#This should also work if you provide more than 3 candidates in the same format
#csv file
for x in range(0,len(candidates)):
	print(f'{candidates[x]}: {round(votes[x] / sum(votes) * 100,3)}% ({votes[x]})')

print(
	'\n--------------------\n'	
	f'Winner: {candidates[winner_index]}\n'
	'--------------------'
)		
		

#-------------------
#Return results to file
with open(analysis_txt, 'w', newline='') as output:
	output.write(
		'Election Results\n'
		'--------------------\n'
		f'Total Votes: {sum(votes)}\n'
		'--------------------\n'
	)
	for x in range(0,len(candidates)):
		output.write(f'{candidates[x]}: {round(votes[x] / sum(votes) * 100,2)}% ({votes[x]})\n')
	output.write(
		'--------------------\n'
		f'Winner: {candidates[winner_index]}\n'
		'--------------------\n'
	)	
































