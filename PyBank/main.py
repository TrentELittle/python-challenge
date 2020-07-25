import os 
import csv

# Create a file path for data
bank_csv = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

# Open and read the data path
with open(bank_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    # Read the header row
    csv_header = next(csvreader)
    date = csv_header[0]
    prof_loss = csv_header[1]

    # Count the Number of Months and add the Net Profit/Loss included in the data set
    total_months = []
    net_profits = []
    for row in csvreader:
        total_months.append(row[0])
        net_profits.append(int(row[1]))

    # Find the average of the changes in "Profit/Losses" over the entire period
    change_profits = []
    a = 0
    b = 0
    while b < len(net_profits):
        change = net_profits[b] - net_profits[a]
        change_profits.append(change)
        a = b
        b = b + 1

    average_change = sum(change_profits) / len(change_profits)

    # Greatest increase and greatest decrease in profits for both date and amount
    max_incr = max(change_profits)
    max_decr = min(change_profits)
    max_incr_date = total_months[(change_profits.index(max_incr))]
    max_decr_date = total_months[(change_profits.index(max_decr))]



    # Format the final numbers to include commas or decimals for separation and readability
    formatted_profit = "{:,}".format(sum(net_profits))
    formatted_average_change = "{:.2f}".format(average_change)
    form_max_incr = "{:,}".format(max_incr)
    form_max_decr = "{:,}".format(max_decr)
    
# Print out Financial Analysis and export to text file "finacial_analysis.txt" with results
output = ("Financial Analysis"
    "\n----------------------------"
    f"\nTotal Months: {len(total_months)}"
    f"\nNet Total Profit/Loss: ${formatted_profit}"
    f"\nAverage Change: ${formatted_average_change}"
    f"\nGreatest Increase in Profits: {max_incr_date} (${form_max_incr})"
    f"\nGreatest Decrease in Profits: {max_decr_date} (${form_max_decr})"
    )
print(output)

financial_analysis = os.path.join("..", "PyBank", "Analysis", "financial_analysis.txt")
with open(financial_analysis, "w") as fa:
    fa.write(output)




