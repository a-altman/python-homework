from pathlib import Path
import csv

# Set path to budget data csv file
csvpath = Path('./budget_data.csv')

# Initialize variables for pnl analysis
total_months = 0
pnl_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999999]
net_total_pnl = 0
sum_pnl_changes = 0

# Set up csv reader object to read csv file and read header row
# Extract header and set up objects to hold data as we move through list of months and pnl data
with open(csvpath, 'r') as pybank_pnl_csv:
    csvreader = csv.reader(pybank_pnl_csv, delimiter=',')
    header = next(csvreader)
    first_row = next(csvreader)
    total_months = total_months + 1
    net_total_pnl = net_total_pnl + int(first_row[1])
    prev_pnl = int(first_row[1])
   
    # Iterate through data to calculate total months and net total pnl
    for row in csvreader:

        total_months = total_months + 1
        net_total_pnl = net_total_pnl + int(row[1])
    
    # Create objects to calculate and hold onto pnl change for each month as we iterate over data
        net_change = int(row[1]) - prev_pnl
        prev_pnl = int(row[1])
        pnl_change_list = pnl_change_list + [net_change] 
    
    # Create conditionals that will find the greatest increase and greatest decrease in pnl    
        if net_change > greatest_increase[1]:
            greatest_increase[1] = net_change
            greatest_increase[0] = row[0]
        if net_change < greatest_decrease[1]:
            greatest_decrease[1] = net_change
            greatest_decrease[0] = row[0] 
 
    #  Iterate through the pnl change list to calculate net total pnl change and use this to calculate average pnl change
    for change in pnl_change_list:
       sum_pnl_changes += change
    
    num_pnl_changes = len(pnl_change_list)
    average_pnl_change = sum_pnl_changes/num_pnl_changes
    
    # Print the results of the analysis   
    print("PyBank Financial Analysis")
    print("------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_total_pnl:.2f}")
    print(f"Average Change: ${average_pnl_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase[0]}, ${greatest_increase[1]:.2f}")
    print(f"Greatest Decrease in Profits: {greatest_decrease[0]}, ${greatest_decrease[1]:.2f}")