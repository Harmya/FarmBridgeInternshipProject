
import csv




def create_file():
    var = ['rain', 'tmax', 'tmin', 'rainyDays', 'tmaxAverage', 'tminAverage'] #options are tmax, tmin, rain and rainy days
    for variable in var:
         csv_file = open('D:/IMDdata/SortedData/' + str(variable) + ".csv" , 'w', newline='')
         csv_writer = csv.writer(csv_file)
         months = ['Annual', 'Winter', 'Summer', 'SWM', 'NEM', 'January', 'February', 'March', 'April', 'May',
              'June',
              'July', 'August', 'September', 'October', 'November', 'December']
                   

         years = [variable]
         for x in range(1990, 2021):
              years.append(str(x))
         csv_writer.writerow(years)
         l = len(months)
         for x in range(0, l):
             temp = [months[x]]
             csv_writer.writerow(temp)
     


   

create_file()