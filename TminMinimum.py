import pandas as pd
import csv
import operator



def min_val(year, lat, lon, variable):
    


    csv_file = open('D:/IMDdata/tmin/' + str(year) + '_' + str(variable) + '_' + str(lat) + '_' + str(lon) + '.csv' , 'r')
    csv_reader = csv.reader(csv_file)
    # each file of tmin/tmin/rain will be opened
    next(csv_reader)
    

    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if year % 4 == 0:
        days[1] = 29
        days_loop = 366
        
    else:
        days[1] = 28
        days_loop = 365
        

    
    monthly_min = []
    temp_dec = []
    check = 0
    c = 0
    temp_arr = []
    for x in range(0, days_loop):
        data = next(csv_reader)
        if check == int(days[c]):
            c += 1
            min_arr = min(temp_arr)
            monthly_min.append(str(min_arr))
            temp_arr.clear()
            check = 0
        check += 1
        data_x = float(data[1])
        if data_x > 0:
           temp_arr.append(data_x)
        if c > 10:
            temp_dec.append(data_x)
    min_dec = min(temp_dec)
    monthly_min.append(min_dec)
    monthly_min = list(map(float, monthly_min))
    annual = min(monthly_min)
    w = min(monthly_min[0], monthly_min[1])
    s = min(monthly_min[2], monthly_min[3], monthly_min[4])
    s_w_m = min(monthly_min[5], monthly_min[6], monthly_min[7], monthly_min[8])
    n_e_m = min(monthly_min[9], monthly_min[10], monthly_min[11])
    temp_a = [str(annual), str(w), str(s), str(s_w_m), str(n_e_m)]
    monthly_min = list(map(str, monthly_min))
    final_min = temp_a + monthly_min
    df_new = pd.read_csv('D:/IMDdata/SortedData/tmin.csv')
    df_new[str(year)] = final_min
    df_new.to_csv('D:/IMDdata/SortedData/tmin.csv', index=False)



    