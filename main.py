import DownloadCsv
import MakeMonthlyFiles
import TmaxAverage
import TmaxMaximum
import TminAverage
import TminMinimum
import TotalRain
import RainyDays
import MakeExtremeFile


start_year = 2018
end_year = 2020
latitude = 23.50
longitude = 78.22
lat = '23.50'
lon ='78.22'
variable_one = 'tmax'
variable_two = 'tmin'
variable_three = 'rain'
'''
DownloadCsv.downloadFiles(start_year, end_year, latitude, longitude, variable_one )
DownloadCsv.downloadFiles(start_year, end_year, latitude, longitude, variable_two )
'''
DownloadCsv.downloadFiles(start_year, end_year, latitude, longitude, variable_three)

MakeMonthlyFiles.create_file()
MakeExtremeFile

for x in range(start_year, end_year + 1):
    '''
    TmaxAverage.max_average_val(x, lat, lon, variable_one)
    TmaxMaximum.max_val(x, lat, lon, variable_one)
    TminAverage.min_average_val(x, lat, lon, variable_two)
    TminMinimum.min_val(x, lat, lon, variable_two)
    '''
    RainyDays.rain_day_val(x, lat, lon, variable_three)
    TotalRain.rain_val(x, lat, lon, variable_three)
    print('year done is ' + str(x))
