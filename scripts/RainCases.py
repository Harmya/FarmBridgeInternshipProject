import pandas as pd
import csv
import operator
# this script calculates the number of extreme rainfall cases in Celsius 
# three categories: <25mm, >50mm and >75mm

def extreme_rainfall(year, lat, lon, variable):
    
    days = []
    monthly_25 =[]
    monthly_50 =[]
    monthly_75 = []
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
        
    check = 0
    c = 0
    is_25, is_50, is_75 = 0, 0, 0
    is_25_d, is_50_d, is_75_d = 0, 0, 0
    for x in range(0, days_loop):
        data = next(csv_reader)
        data_x = float(data[1])
        if check == int(days[c]):
            monthly_25.append(is_25)
            monthly_50.append(is_50)
            monthly_75.append(is_75)
            c += 1
            is_25, is_50, is_75 = 0, 0, 0
            check = 0
        check += 1
        if float(data_x) > 25:
            is_25 += 1
        if float(data_x) > 50:
            is_50 += 1
        if float(data_x) > 75:
            is_75 += 1
        if c > 10:
            if float(data_x) > 25:
                is_25_d += 1
            if float(data_x) > 50:
                is_50_d += 1
            if float(data_x) > 75:
                is_75_d += 1
    monthly_25.append(is_25_d)
    monthly_50.append(is_50_d)
    monthly_75.append(is_75_d)
    annual_25 = sum(monthly_25)
    w_25 = (monthly_25[0] + monthly_25[1])
    s_25 = (monthly_25[2] + monthly_25[3] + monthly_25[4])
    s_w_m_25 = (monthly_25[5] + monthly_25[6] + monthly_25[7] + monthly_25[8])
    n_e_m_25 = (monthly_25[9] + monthly_25[10] + monthly_25[11])
    annual_50 = sum(monthly_50)
    w_50 = (monthly_50[0] + monthly_50[1])
    s_50 = (monthly_50[2] + monthly_50[3] + monthly_50[4])
    s_w_m_50 = (monthly_50[5] + monthly_50[6] + monthly_50[7] + monthly_50[8])
    n_e_m_50 = (monthly_50[9] + monthly_50[10] + monthly_50[11])
    annual_75 = sum(monthly_75)
    w_75 = (monthly_75[0] + monthly_75[1])
    s_75 = (monthly_75[2] + monthly_75[3] + monthly_75[4])
    s_w_m_75 = (monthly_75[5] + monthly_75[6] + monthly_75[7] + monthly_75[8])
    n_e_m_75 = (monthly_75[9] + monthly_75[10] + monthly_75[11])
    final_25 = [str(annual_25), str(w_25), str(s_25), str(s_w_m_25), str(n_e_m_25)]
    final_50 = [str(annual_50), str(w_50), str(s_50), str(s_w_m_50), str(n_e_m_50)]
    final_75 = [str(annual_75), str(w_75), str(s_75), str(s_w_m_75), str(n_e_m_75)]
    blank = ['']
    final_list = blank + final_25 + blank + final_50 + blank + final_75 
    print(final_list)
    df_new = pd.read_csv('D:/IMDdata/SortedData/rainCasesExtreme.csv')
    df_new[str(year)] = final_list
    df_new.to_csv('D:/IMDdata/SortedData/rainCasesExtreme.csv', index=False)

#input here
# PLEASE CHECK INPUT BEFORE RUNNING THE SCRIPT 

lat = '00'
lon = '00'
start_year = 2018 # input
end_year = 2020 #input

for x in range(start_year, end_year + 1):
    extreme_rainfall(x, lat,lon, 'rain')
    print('year done is ' + str(x))
