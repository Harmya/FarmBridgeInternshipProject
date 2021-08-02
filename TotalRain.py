import pandas as pd
import csv
import operator


def rain_val(year, lat, lon, variable):
    


    csv_file = open('D:/IMDdata/rain/' + str(year) + '_' + str(variable) + '_' + str(lat) + '_' + str(lon) + '.csv' , 'r')
    csv_reader = csv.reader(csv_file)
    # each file of rain will be opened
    next(csv_reader)
    

    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if year % 4 == 0:
        days[1] = 29
        days_loop = 366
        
    else:
        days[1] = 28
        days_loop = 365
        

    
    monthly_rain = []
    rain_dec = 0
    check = 0
    c = 0
    temp = 0

    for x in range(0, days_loop):
        data = next(csv_reader)
        if check == int(days[c]):
            c += 1
            monthly_rain.append(str(temp))
            temp = 0
            check = 0
        check += 1
        data_x = float(data[1])
        if data_x > 0:
           temp += data_x
        if c > 10:
            rain_dec += data_x
             
    monthly_rain.append(rain_dec)
    monthly_rain = list(map(float, monthly_rain))
    annual = sum(monthly_rain)
    w = monthly_rain[0] + monthly_rain[1]
    s = monthly_rain[2] +  monthly_rain[3] + monthly_rain[4]
    s_w_m = monthly_rain[5] + monthly_rain[6] + monthly_rain[7] + monthly_rain[8]
    n_e_m = monthly_rain[9] + monthly_rain[10] + monthly_rain[11]
    temp_a = [str(annual), str(w), str(s), str(s_w_m), str(n_e_m)]
    monthly_rain = list(map(str, monthly_rain))
    final_sum = temp_a + monthly_rain
    df_new = pd.read_csv('D:/IMDdata/SortedData/rain.csv')
    df_new[str(year)] = final_sum
    df_new.to_csv('D:/IMDdata/SortedData/rain.csv', index=False)

    

    

