# this script organizes the forecast data for tmax into specific seasons for india
import statistics
import pandas as pd
import FinalYearTmax

def monthly_fore():
    file_to_read = 'D:/IMDdata/Tmax.csv' 
    # change the path to the directory where you have stored the tmax file 
    output_file = 'D:/IMDdata/TMaxCCCma.csv'
    # change the path to the directory where you have stored the forecast models for the tmax file
    # here, CCCma is a type of forecast model licensed to the company by an instituition
    # for intellectual property reasons, I cannot display the code we used to operate on the forecast
    # hence this is a snippet to show how we organized the files into specific seasons
    # SWM: South West Monsoon
    # NEM: North East Monsooon
    df = pd.read_csv(file_to_read)
    df_new = pd.read_csv(output_file)
    df = pd.read_csv(file_to_read)
    df_new = pd.read_csv(output_file)
    months = ['Annual', 'Winter', 'Summer', 'SWM', 'NEM', 'January', 'February', 'March', 'April', 'May',
              'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    c = 1
    year = 2021
    sum_temp = []
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if year % 4 == 0:
        days[1] = 29
    else:
        days[1] = 28
    for x in range(180, 1128):

        val = df.iloc[x, 1]
        temp = float(val) - 273

        if c == 13:
            annual = statistics.mean(sum_temp)
            w = max(sum_temp[0], sum_temp[1])
            s = max(sum_temp[2], sum_temp[3], sum_temp[4])
            s_w_m = max(sum_temp[5], sum_temp[6], sum_temp[7], sum_temp[8])
            n_e_m = max(sum_temp[9], sum_temp[10], sum_temp[11])
            temp_year = [annual, w, s, s_w_m, n_e_m]
            temp_year = temp_year + sum_temp
            df_new[str(year)] = temp_year
            df_new.to_csv(output_file, index=False)
            c = 1
            year += 1
            sum_temp.clear()
            temp_year.clear()

        sum_temp.append(temp)
        c += 1
    FinalYearTmax.get_it(file_to_read, output_file)


monthly_fore()

