import statistics
import pandas as pd
import csv


def get_it(file_to_read, output_file):
    df = pd.read_csv(file_to_read)
    df_new = pd.read_csv(output_file)
    c = 1
    year = 2021
    sum_temp = []

    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if year % 4 == 0:
        days[1] = 29
    else:
        days[1] = 28

    for x in range(1116, 1128):

        val = str(df.iloc[x, 1])
        temp = (float(val))
        temp = temp * 86400 * days[c - 1]
        sum_temp.append(temp)
        c += 1
        if c == 13:
            annual = statistics.mean(sum_temp)
            w = max(sum_temp[0], sum_temp[1])
            s = max(sum_temp[2], sum_temp[3], sum_temp[4])
            s_w_m = max(sum_temp[5], sum_temp[6], sum_temp[7], sum_temp[8])
            n_e_m = max(sum_temp[9], sum_temp[10], sum_temp[11])
            temp_year = [annual, w, s, s_w_m, n_e_m]
            temp_year = temp_year + sum_temp
            df_new['2099'] = temp_year
            df_new.to_csv(output_file, index=False)
            year += 1
            c = 1