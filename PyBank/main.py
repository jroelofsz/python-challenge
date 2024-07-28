"""
This script analyzes a dataset of financial records to calculate key metrics:

1. The total number of months included in the dataset.
2. The net total amount of "Profit/Losses" over the entire period.
3. The changes in "Profit/Losses" over the entire period, and then the average of those changes.
4. The greatest increase in profits (date and amount) over the entire period.
5. The greatest decrease in profits (date and amount) over the entire period.

The script processes the dataset to extract and compute these values, providing a comprehensive summary of the financial performance over time.
"""

#Import OS and CSV Module
import os
import csv 

#Set path variables for CSV and Output text file
budget_data_csv = os.path.join(".","Resources","budget_data.csv")
analysis_txt = os.path.join(".","analysis","budget_analysis.txt")


#Declare Variables to be used throughout the script
month = []
changes = []
grand_total = 0
previous_value = 0
low_change = 0
high_change = 0
high_month = ["",0]
low_month = ["",0]


#Open the budget_data_csv file as source
with open(budget_data_csv, 'r') as source:
	csvreader = csv.reader(source,delimiter=',')
	header = next(csvreader)

	for row in csvreader:
		current_value = int(row[1])
		month.append(row[0])
		grand_total += current_value
		
		if previous_value != 0:
			change = current_value - previous_value
			changes.append(change)

			if change > high_change:
				high_change = change
				high_month[0] = row[0]
				high_month[1] = change
			elif change < low_change:
				low_change = change
				low_month[0] = row[0]
				low_month[1] = change
			

		previous_value = current_value


	average_change = sum(changes) / len(changes)




#results to command line
print('Financial Analysis\n'
					'-------------------------------\n'
 					f'Total Months: {len(month)}\n'
 					f'Total: ${grand_total}\n'
 					f'Average Change: ${round(average_change,2)}\n'
 					f'Greatest Increase in Profits: {high_month[0]} (${high_month[1]})\n'
 					f'Greatest Decrease is Profits: {low_month[0]} (${low_month[1]})\n'
)


#Write results to the file
with open(analysis_txt, 'w', newline='') as output:
	
 	#write results
 	output.write('Financial Analysis\n'
 					'-------------------------------\n'
 					f'Total Months: {len(month)}\n'
 					f'Total: ${grand_total}\n'
 					f'Average Change: ${round(average_change,2)}\n'
 					f'Greatest Increase in Profits: {high_month[0]} (${high_month[1]})\n'
 					f'Greatest Decrease is Profits: {low_month[0]} (${low_month[1]})\n')
















