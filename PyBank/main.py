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
months = 0
changes = []
grand_total = 0
high_month = ["",0]
low_month = ["",0]


#Open the source data file as read
with open(budget_data_csv, 'r') as source:
	csvreader = csv.reader(source,delimiter=',')
	header = next(csvreader)

	#variables to be used in loop
	previous_value = 0
	low_change = 0
	high_change = 0

	for row in csvreader:
		#set the current value variable
		current_value = int(row[1])
		#month counter
		months += 1
		#add to the grand total
		grand_total += current_value
		
		if previous_value != 0:
			#change equal to the current value minus the previous value
			change = current_value - previous_value
			#add the change to the changes list (used for average)
			changes.append(change)

			#if change > largest change we've recorded, record the new one
			if change > high_change:
				high_change = change
				high_month[0] = row[0]
				high_month[1] = change
			#if change < lowest change we've recorded, record the new one
			elif change < low_change:
				low_change = change
				low_month[0] = row[0]
				low_month[1] = change
			

		#set previous value = to current value for next run
		previous_value = current_value


	#calculate the average change
	average_change = sum(changes) / len(changes)




#results to command line
print('Financial Analysis\n'
					'-------------------------------\n'
 					f'Total Months: {months}\n'
 					f'Total: ${grand_total}\n'
 					f'Average Change: ${round(average_change,2)}\n'
 					f'Greatest Increase in Profits: {high_month[0]} (${high_month[1]})\n'
 					f'Greatest Decrease is Profits: {low_month[0]} (${low_month[1]})\n'
)


#open the file with write permissions
with open(analysis_txt, 'w', newline='') as output:
	
 	#write results
 	output.write('Financial Analysis\n'
 					'-------------------------------\n'
 					f'Total Months: {months}\n'
 					f'Total: ${grand_total}\n'
 					f'Average Change: ${round(average_change,2)}\n'
 					f'Greatest Increase in Profits: {high_month[0]} (${high_month[1]})\n'
 					f'Greatest Decrease is Profits: {low_month[0]} (${low_month[1]})\n')
















