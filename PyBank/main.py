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
grand_total = 0
average_change = 0
total_change = 0
change = 0
month = []
returns = []

#Open the budget_data_csv file as source
with open(budget_data_csv, 'r') as source:
	csvreader = csv.reader(source,delimiter=',')
	header = next(csvreader)

	#Loop through each row in the CSV File
	for row in csvreader:
		#Add the profit/loss to the grand total
		grand_total += int(row[1])

		#Add each month and value to their own list, this is for calculating the min and max
		month.append(row[0])
		returns.append(int(row[1]))



#Find the index of the highest and lowest profit
high_index = returns.index(max(returns))
low_index = returns.index(min(returns))
		


#Calculate the average change in profit/loss
cur_val = 0
prev_val = 0
for row in returns:
	cur_val = row

	#the change is current value - previous value)
	change = cur_val - prev_val
	prev_val = row

	total_change += average_change + change

#average change is the 'The changes in Profit/Losses over the entire period, 
#and then the average of those changes'
average_change = total_change / len(month)

#results to command line
print('Financial Analysis\n'
					'-------------------------------\n'
					f'Total Months: {len(month)}\n'
					f'Total: ${grand_total}\n'
					f'Average Change: ${round(average_change,2)}\n'
					f'Greatest Increase in Profits: {month[high_index]} (${returns[high_index]})\n'
					f'Greatest Decrease is Profits: {month[low_index]} (${returns[low_index]})\n'
		)




#Write results to the file
with open(analysis_txt, 'w', newline='') as output:
	
	#write results
	output.write('Financial Analysis\n'
					'-------------------------------\n'
					f'Total Months: {len(month)}\n'
					f'Total: ${grand_total}\n'
					f'Average Change: ${round(average_change,2)}\n'
					f'Greatest Increase in Profits: {month[high_index]} (${returns[high_index]})\n'
					f'Greatest Decrease is Profits: {month[low_index]} (${returns[low_index]})\n'
		)
















