import os
import csv

# Path to collect data from the csv file
budget_data_csv = os.path.join('..', 'Data', 'budget_data.csv')

# Create financial variables for output
totalmonths = 0
totalrevenue = 0
greatestincrease = 0
greatestdecrease = 0
increasedate = "unknown"
decreasedate = "unknown"
totalchange = 0
currentmonthrev = 0
previousmonthrev = 0
change = 0

# Open csv and loop through data to fill in variables
with open(budget_data_csv, 'r') as budget_data:
    reader = csv.DictReader(budget_data)
        
    for row in reader:
            
        # Keep a running tab of months and revenue
        previousmonthrev = currentmonthrev 
        if previousmonthrev == 0:
            exclude = int(row["Profit/Losses"])
        totalrevenue = totalrevenue + int(row["Profit/Losses"])
        totalmonths = totalmonths + 1
        
        # Calculate change in current month revenue and keep total change     
        currentmonthrev = int(row["Profit/Losses"])
        change = currentmonthrev - previousmonthrev
        totalchange = totalchange + change

        # Find greatest increase and decrease
        if change > greatestincrease:
            greatestincrease = change
            increasedate = row["Date"]
        elif change < greatestdecrease:
            greatestdecrease = change
            decreasedate = row["Date"]

# Calculate the average change over period
totalchange = totalchange - exclude
averagechange = totalchange / (totalmonths - 1)

# Output summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------\n"
    f"Total Months: {totalmonths}\n"
    f"Total: ${totalrevenue}\n"
    f"Average Change: ${averagechange}\n"
    f"Greatest Increase in Profits: {increasedate} (${greatestincrease})\n"
    f"Greatest Decrease in Profits: {decreasedate} (${greatestdecrease})\n")
print (output)

# Print output summary in terminal and export text file
with open("budget_analysis.txt", "w") as txt_file:
    txt_file.write(output)