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
import os, csv

election_data_csv = os.path.join(".","Resources","election_data.csv")
analysis_txt = os.path.join(".","analysis","election_results.txt")

total_votes = 0 
candidates = []
votes = []


with open(election_data_csv, 'r') as source:
	csvreader = csv.reader(source,delimiter=',')
	
	header = next(csvreader)
	
	
	for row in csvreader:
		#add to the total votes
		total_votes += 1
	
		if row[2] in candidates:
			index = candidates.index(row[2])
			votes[index] += 1
		else:
			#if this is the first time we are seeing this
			#candidate, create a index
			index = len(candidates)
			candidates.append(row[2])
			votes.append(1)

#find who the winner is
winner_index = votes.index(max(votes))

#return the results to comand line
print('Election Results')
print('--------------------')
print(f'Total Votes: {total_votes}')
print('--------------------')
for x in range(0,len(candidates)):
	print(f'{candidates[x]}: {round(votes[x] / total_votes * 100,2)}% ({votes[x]})')
print('--------------------')	
print(f'Winner: {candidates[winner_index]}')
print('--------------------')		
		

#write to file
with open(analysis_txt, 'w', newline='') as output:
	output.write('Election Results\n')
	output.write('--------------------\n')
	output.write(f'Total Votes: {total_votes}\n')
	output.write('--------------------\n')
	for x in range(0,len(candidates)):
		output.write(f'{candidates[x]}: {round(votes[x] / total_votes * 100,2)}% ({votes[x]})\n')
	output.write('--------------------\n')
	output.write(f'Winner: {candidates[winner_index]}\n')
	output.write('--------------------\n')	
































