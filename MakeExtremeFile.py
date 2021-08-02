import csv
csv_file = open('D:/IMDdata/SortedData/rainCasesExtreme.csv' , 'w', newline='')
csv_writer = csv.writer(csv_file)
extreme_months = ['Rainy Days > 25mm', 'Annual', 'Winter', 'Summer', 'SWM', 'NEM', 'Rainy days > 50mm', 'Annual', 'Winter', 'Summer', 'SWM', 'NEM', 'Rainy days > 75 mm', 'Annual', 'Winter', 'Summer', 'SWM', 'NEM']  
years = ['rainExtreme']
for x in range(1990, 2021):
    years.append(str(x))
csv_writer.writerow(years)
l = len(extreme_months)
for x in range(0, l):
    temp = [extreme_months[x]]
    csv_writer.writerow(temp)