from scripts import TmaxAverage, TminMinimum, DownloadCsv, RainyDays, MakeMonthlyFiles, TotalRain, MakeExtremeFile, \
    TmaxMaximum, TminAverage

# RUN THIS SCRIPT FOR ORGANIZING DATA
# This is the main script 
# input data down here
# default inputs are 1990, 2020 for start and end year
# latitude is 00 and longitude is 00
# input latitude and longitude twice because we need a string to search files in the directory
start_year = 1990 #input
end_year = 2020 #input
latitude = 00 #input
longitude = 00 #input
lat = '00' #input
lon ='00'  #input
variable_one = 'tmax'
variable_two = 'tmin'
variable_three = 'rain'
#Step One: Downloads all the files in grid format and converts them to csv
DownloadCsv.downloadFiles(start_year, end_year, latitude, longitude, variable_one)
DownloadCsv.downloadFiles(start_year, end_year, latitude, longitude, variable_two)
DownloadCsv.downloadFiles(start_year, end_year, latitude, longitude, variable_three)
#Step Two: Makes empty orgnized files to fill in data from the downloaded files
MakeMonthlyFiles.create_file()
MakeExtremeFile
#Step Three: runs all the functions from various scirpts in the project to organize all the data
# specific to india's seasons
for x in range(start_year, end_year + 1):
    TmaxAverage.max_average_val(x, lat, lon, variable_one)
    TmaxMaximum.max_val(x, lat, lon, variable_one)
    TminAverage.min_average_val(x, lat, lon, variable_two)
    TminMinimum.min_val(x, lat, lon, variable_two)
    RainyDays.rain_day_val(x, lat, lon, variable_three)
    TotalRain.rain_val(x, lat, lon, variable_three)
    print('year done is ' + str(x))
