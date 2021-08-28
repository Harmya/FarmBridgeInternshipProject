# this script downloads historical data of a particular variable(tmax, tmin or rain)
# in a specified year range

import imdlib as imd
import os



def downloadFiles(start_year, end_year, lat, lon, variable):
 # other options are ('tmin'/ 'tmax')
    file_dir = "D:/IMDdata/" 

    for year in range(start_year, end_year + 1):

        temp_start = start_year
        temp_end = end_year
        temp_end = temp_start 
        data = imd.get_data(variable, temp_start, temp_end, fn_format='yearwise', file_dir=file_dir)
        out_dir='D:/IMDdata/' + str(variable) . # change this path to get files in a particular dir 
        file_name =  str(temp_start) + "_" + str(variable)
        data.to_csv(file_name, lat, lon, out_dir)
        print('csv conversion complete')
        os.remove("D:/IMDdata/" + str(variable) + "/" + str(temp_start) + ".grd") # change the dir here too
        start_year += 1





