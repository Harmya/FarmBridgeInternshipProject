import statistics
import pandas as pd
import csv
import FinalYearTmax

def monthly_fore():
    file_to_read = 'D:/IMDdata/Tmax.csv'
    output_file = 'D:/IMDdata/TMaxCCCma.csv'

    df = pd.read_csv(file_to_read)
    df_new = pd.read_csv(output_file)
    c = 1
    year = 2021
    sum_temp = []
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
            print(year)
            year += 1
            sum_temp.clear()
            temp_year.clear()

        sum_temp.append(temp)
        c += 1
    FinalYearTmax.get_it(file_to_read, output_file)


monthly_fore()

