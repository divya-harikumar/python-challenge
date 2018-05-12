# # Option 1: PyBank

print('Financial Analysis')
print('----------------------------')

# read the csv
fn = 'budget_data_2.csv'
f = open(fn)
all_data = f.read()
f.close()

list_of_lines = all_data.split('\n')
# remove headers
headers = list_of_lines.pop(0)

# The total number of months included in the dataset
# remove blanks lines
for row_number, line in enumerate(list_of_lines):
    if line == '':
        del(list_of_lines[row_number])

num_months = len(list_of_lines)
print('Total Months:', num_months)


# The total amount of revenue gained over the entire period
# get the revenues from each line
total_revenue = 0
dates = []
revenues = []
for line in list_of_lines:
    # line is 'date,revenue'
    items_list = line.split(',')
    date = items_list[0]  # 1st col is date
    dates.append(date)
    revenue_string = items_list[1]  # 2nd column
    revenue = int(revenue_string)
    revenues.append(revenue)   # add to list
    total_revenue += revenue
    
print('Total Revenue: $%d' % revenue)

# The average change in revenue between months over the entire period
revenue_changes = []
for row_number, revenue in enumerate(revenues):
    if row_number == 0:
        continue
    change = revenue - revenues[row_number - 1]
    #print('44 change', change, '  rev:', revenue, '  prev rev', revenues[row_number-1])
    revenue_changes.append(change)
    
# calc average change in revenue
avg_change = sum(revenue_changes) / len(revenue_changes)
#print('sum of changes', sum(revenue_changes))
print('Average Revenue Changes: $%6.2f' % avg_change)

# The greatest increase in revenue (date and amount) over the entire period
largest_change = 0
largest_change_row_number = None
for row_number, change in enumerate(revenue_changes):
    if change > largest_change:
        largest_change = change
        largest_change_row_number = row_number

date_of_largest_change = dates[largest_change_row_number]

print('Greatest Increase in Revenue: %s $(%0.2f)' % (date_of_largest_change, largest_change) )

# The greatest decrease in revenue (date and amount) over the entire period
largest_decrease = 0
largest_decr_row_number = None
for row_number, change in enumerate(revenue_changes):
    if change < largest_decrease:
        largest_decrease = change
        largest_decr_row_number = row_number

date_of_largest_decrease = dates[largest_decr_row_number]

print('Greatest Increase in Revenue: %s $(%0.2f)' % (date_of_largest_decrease, largest_decrease) )