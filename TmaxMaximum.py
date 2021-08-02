import pandas as pd
import csv
import operator


def max_val(year, lat,lon,variable):
    


    csv_file = open('D:/IMDdata/tmax/' + str(year) + '_' + str(variable) + '_' + str(lat) + '_' + str(lon) + '.csv' , 'r')
    csv_reader = csv.reader(csv_file)
    # each file of tmax/tmax/rain will be opened
    next(csv_reader)
    

    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if year % 4 == 0:
        days[1] = 29
        days_loop = 366
        
    else:
        days[1] = 28
        days_loop = 365
        

    
    monthly_max = []
    temp_dec = []
    check = 0
    c = 0
    temp_arr = []
    for x in range(0, days_loop):
        data = next(csv_reader)
        if check == int(days[c]):
            c += 1
            max_arr = max(temp_arr)
            monthly_max.append(str(max_arr))
            temp_arr.clear()
            check = 0
        check += 1
        data_x = float(data[1])
        if data_x > 0:
           temp_arr.append(data_x)
        if c > 10:
            temp_dec.append(data_x)
    max_dec = max(temp_dec)
    monthly_max.append(max_dec)
    monthly_max = list(map(float, monthly_max))
    annual = max(monthly_max)
    w = max(monthly_max[0], monthly_max[1])
    s = max(monthly_max[2], monthly_max[3], monthly_max[4])
    s_w_m = max(monthly_max[5], monthly_max[6], monthly_max[7], monthly_max[8])
    n_e_m = max(monthly_max[9], monthly_max[10], monthly_max[11])
    temp_a = [str(annual), str(w), str(s), str(s_w_m), str(n_e_m)]
    monthly_max = list(map(str, monthly_max))
    final_max = temp_a + monthly_max
    df_new = pd.read_csv('D:/IMDdata/SortedData/tmax.csv')
    df_new[str(year)] = final_max
    df_new.to_csv('D:/IMDdata/SortedData/tmax.csv', index=False)



    