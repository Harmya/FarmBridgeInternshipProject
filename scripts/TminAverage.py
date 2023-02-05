import pandas as pd
import csv
import statistics
# this script calculates the MEAN minimum temperature for each specified month in Celsius


def min_average_val(year, lat, lon, variable):
    


    csv_file = open('D:/IMDdata/tmin/' + str(year) + '_' + str(variable) + '_' + str(lat) + '_' + str(lon) + '.csv' , 'r')
    csv_reader = csv.reader(csv_file)
    # each file of tmin will be opened
    next(csv_reader)
    

    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if year % 4 == 0:
        days[1] = 29
        days_loop = 366
        
    else:
        days[1] = 28
        days_loop = 365
        

    
    monthly_mean = []
    temp_dec = []
    check = 0
    c = 0
    temp_arr = []
    for x in range(0, days_loop):
        data = next(csv_reader)
        if check == int(days[c]):
            c += 1
            mean_arr = statistics.mean(temp_arr)
            monthly_mean.append(str(mean_arr))
            temp_arr.clear()
            check = 0
        check += 1
        data_x = float(data[1])
        if data_x > 0:
           temp_arr.append(data_x)
        if c > 10:
            temp_dec.append(data_x)
    max_dec = statistics.mean(temp_dec)
    monthly_mean.append(max_dec)
    monthly_mean = list(map(float, monthly_mean))
    annual = statistics.mean(monthly_mean)
    w = statistics.mean([monthly_mean[0], monthly_mean[1]])
    s = statistics.mean([monthly_mean[2], monthly_mean[3], monthly_mean[4]])
    s_w_m = statistics.mean([monthly_mean[5], monthly_mean[6], monthly_mean[7], monthly_mean[8]])
    n_e_m = statistics.mean([monthly_mean[9], monthly_mean[10], monthly_mean[11]])
    temp_a = [str(annual), str(w), str(s), str(s_w_m), str(n_e_m)]
    final_max = temp_a + monthly_mean
    df_new = pd.read_csv('D:/IMDdata/SortedData/tminAverage.csv')
    df_new[str(year)] = final_max
    df_new.to_csv('D:/IMDdata/SortedData/tminAverage.csv', index=False)



    