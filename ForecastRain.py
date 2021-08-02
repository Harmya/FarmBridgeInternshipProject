
import FinalYearRain
import pandas as pd
import csv


def forecast():
    file_to_read = 'D:/IMDdata/Precipitation.csv'
    output_file = 'D:/IMDdata/ForecastRain.csv'
    df = pd.read_csv(file_to_read)
    df_new = pd.read_csv(output_file)
    months = ['Annual', 'Winter', 'Summer', 'SWM', 'NEM', 'January', 'February', 'March', 'April', 'May',
              'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    df_new[str(df.iloc[0,0])] = months
                   
    c = 1
    year = 2021
    sum_temp = []

    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if year % 4 == 0:
        days[1] = 29
    else:
        days[1] = 28

    for x in range(180, 1128):

        val = str(df.iloc[x, 1])
        temp = (float(val))
        if c == 13:
            annual = sum(sum_temp)
            w = sum_temp[0] + sum_temp[1]
            s = sum_temp[2] + sum_temp[3] + sum_temp[4]
            s_w_m = sum_temp[5] + sum_temp[6] + sum_temp[7] + sum_temp[8]
            n_e_m = sum_temp[9] + sum_temp[10] + sum_temp[11]
            temp_year = [annual, w, s, s_w_m, n_e_m]
            temp_year = temp_year + sum_temp
            df_new[str(year)] = temp_year
            df_new.to_csv( output_file,
                          index=False)
            print(year)
            year += 1
            sum_temp.clear()
            temp_year.clear()
            c = 1

        temp = temp * 86400 * days[c - 1]
        sum_temp.append(temp)
        c += 1
    FinalYearRain.get_it(file_to_read, output_file)


forecast()
