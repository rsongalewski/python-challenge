# import modules
import os
import csv

# define variables

# net total in "Profit/Losses" over the entire period
total = 0

# total number of months included in the dataset
total_months = 0

# date in dataset (column one)
date = ""

# amount in dataset (column two)
amt = 0

# previous amount (for keeping track of change)
prev_amt = 0

# change between one amount and the next
change = 0

# change between one amount and the next
total_change = 0

# average of the changes in "Profit/Losses" over the entire period
avg_change = 0.0

# greatest increase in profits (date and amount) over the entire period
greatest_incr_date = ""
greatest_incr = 0

# greatest decrease in losses (date and amount) over the entire period
greatest_decr_date = ""
greatest_decr = 0

# read input file

input_path = os.path.join('Resources','budget_data.csv')

with open(input_path,newline='') as input_file:

	input_reader = csv.reader(input_file,delimiter=',')

	# skip header
	next(input_reader)

	# read each row and store columns
	for row in input_reader:
		date = row[0]
		amt = row[1]

		# store previous amount
		if prev_amt == 0:
			prev_amt = amt
			
		# compute change from previous month
		change = int(amt) - int(prev_amt)

		# change greatest increase if change is biggest
		if change > greatest_incr:
			greatest_incr = change
			greatest_incr_date = date

		# change greatest decrease if change is lowest
		if change < greatest_decr:
			greatest_decr = change
			greatest_decr_date = date

		# keep track of total change for average change
		total_change += change

		# increment total net change
		total += int(amt)

		# set current amount to next iteration's previous amount
		prev_amt = amt

		# increment number of total_months
		total_months += 1

# compute average change
avg_change = total_change / (total_months - 1)

# construct output as list

output=[]
output.append("Financial Analysis")
output.append("----------------------------")
output.append("Total Months: " + str(total_months))
output.append("Total: $" + str(total))
output.append("Average Change: $" + str(round(avg_change,2)))
output.append("Greatest Increase in Profits: " + greatest_incr_date + " ($" + str(greatest_incr) + ")")
output.append("Greatest Decrease in Profits: " + greatest_decr_date + " ($" + str(greatest_decr) + ")")

# print to terminal
for line in output:
	print(line)

# open file for writing
out_path  = "PyBank.txt"

# print to file
with open(out_path, 'w') as out_file:
	for line in output:
		out_file.write("%s\n" % line)