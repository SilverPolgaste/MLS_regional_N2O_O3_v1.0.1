import h5py
import numpy as np
import os
import csv
os.chdir('path_to_data_dir')

# define a box

class geo_loc:

    def __init__(self, name, box_lat1, box_lat2, box_lon1, box_lon2):
        self.name=name
        self.box_lat1 = box_lat1
        self.box_lat2 = box_lat2
        self.box_lon1 = box_lon1
        self.box_lon2 = box_lon2

#class datapoint:
#    def __init__(self, n2o, location, year, month)

loc_lat = 58.4
loc_lon = 26.5
loc_halfsize = 1.5
loc_name = 'estonia'
loc_pressure = "46"
location = geo_loc(loc_name, loc_lat-loc_halfsize, loc_lat+loc_halfsize, loc_lon-loc_halfsize, loc_lon+loc_halfsize)

directory = 'path_to_data_dir'

data_arr=np.array([[],[],[],[],[],[],[]])

for datafile in os.listdir(directory):	
    hdffile = os.fsdecode(datafile)
    if hdffile.endswith(".he5"):
        print(hdffile)
        f = h5py.File(hdffile, mode='r')
        subset=16
        # full path within the HDF file
        name = '/HDFEOS/SWATHS/O3/Data Fields/L2gpValue'
        month = '/HDFEOS/ADDITIONAL/FILE_ATTRIBUTES[GranuleMonth]'
        # get the geolocation data
        latitude = f['/HDFEOS/SWATHS/O3/Geolocation Fields/Latitude'][:]
        longitude = f['/HDFEOS/SWATHS/O3/Geolocation Fields/Longitude'][:]
        # get quality flags
        quality = f['/HDFEOS/SWATHS/O3/Data Fields/Quality'][:] 
        convergence = f['/HDFEOS/SWATHS/O3/Data Fields/Convergence'][:]
        # define box
        lat_index = np.logical_and(latitude > location.box_lat1, latitude < location.box_lat2)
        lon_index = np.logical_and(longitude > location.box_lon1, longitude < location.box_lon2)
        box_index = np.logical_and(lat_index, lon_index)
        year = [str(hdffile[-12:-8])]
        dateindex = [str(hdffile[-7:-4]).lstrip('0')]
        #print(dateindex)
        # add data to list
        data = np.array([f[name][:,subset][box_index]*10**6, latitude[box_index], longitude[box_index], dateindex*len(latitude[box_index]), quality[box_index], convergence[box_index], year*len(latitude[box_index])], dtype=np.float32)
        #print(data)
        data_arr=np.hstack((data_arr, data))
        continue
    else:
        continue
		
		
data_list=[[],[],[],[],[],[],[]]

for i in range(len(data_arr[0])):
    for j in range(7):
        if data_arr[0][i]>0 and data_arr[5][i]<=1.03 and data_arr[4][i]>=1:
            data_list[j].append(data_arr[j][i])
        else:
            continue


jan2005=[]
feb2005=[]
mar2005=[]
apr2005=[]
may2005=[]
jun2005=[]
jul2005=[]
aug2005=[]
sep2005=[]
oct2005=[]
nov2005=[]
dec2005=[]

jan2006=[]
feb2006=[]
mar2006=[]
apr2006=[]
may2006=[]
jun2006=[]
jul2006=[]
aug2006=[]
sep2006=[]
oct2006=[]
nov2006=[]
dec2006=[]

jan2007=[]
feb2007=[]
mar2007=[]
apr2007=[]
may2007=[]
jun2007=[]
jul2007=[]
aug2007=[]
sep2007=[]
oct2007=[]
nov2007=[]
dec2007=[]

jan2008=[]
feb2008=[]
mar2008=[]
apr2008=[]
may2008=[]
jun2008=[]
jul2008=[]
aug2008=[]
sep2008=[]
oct2008=[]
nov2008=[]
dec2008=[]

jan2009=[]
feb2009=[]
mar2009=[]
apr2009=[]
may2009=[]
jun2009=[]
jul2009=[]
aug2009=[]
sep2009=[]
oct2009=[]
nov2009=[]
dec2009=[]

jan2010=[]
feb2010=[]
mar2010=[]
apr2010=[]
may2010=[]
jun2010=[]
jul2010=[]
aug2010=[]
sep2010=[]
oct2010=[]
nov2010=[]
dec2010=[]

jan2011=[]
feb2011=[]
mar2011=[]
apr2011=[]
may2011=[]
jun2011=[]
jul2011=[]
aug2011=[]
sep2011=[]
oct2011=[]
nov2011=[]
dec2011=[]

jan2012=[]
feb2012=[]
mar2012=[]
apr2012=[]
may2012=[]
jun2012=[]
jul2012=[]
aug2012=[]
sep2012=[]
oct2012=[]
nov2012=[]
dec2012=[]

jan2013=[]
feb2013=[]
mar2013=[]
apr2013=[]
may2013=[]
jun2013=[]
jul2013=[]
aug2013=[]
sep2013=[]
oct2013=[]
nov2013=[]
dec2013=[]

jan2014=[]
feb2014=[]
mar2014=[]
apr2014=[]
may2014=[]
jun2014=[]
jul2014=[]
aug2014=[]
sep2014=[]
oct2014=[]
nov2014=[]
dec2014=[]

jan2015=[]
feb2015=[]
mar2015=[]
apr2015=[]
may2015=[]
jun2015=[]
jul2015=[]
aug2015=[]
sep2015=[]
oct2015=[]
nov2015=[]
dec2015=[]
    
jan2016=[]
feb2016=[]
mar2016=[]
apr2016=[]
may2016=[]
jun2016=[]
jul2016=[]
aug2016=[]
sep2016=[]
oct2016=[]
nov2016=[]
dec2016=[]

jan2017=[]
feb2017=[]
mar2017=[]
apr2017=[]
may2017=[]
jun2017=[]
jul2017=[]
aug2017=[]
sep2017=[]
oct2017=[]
nov2017=[]
dec2017=[]

jan2018=[]
feb2018=[]
mar2018=[]
apr2018=[]
may2018=[]
jun2018=[]
jul2018=[]
aug2018=[]
sep2018=[]
oct2018=[]
nov2018=[]
dec2018=[]

jan2019=[]
feb2019=[]
mar2019=[]
apr2019=[]
may2019=[]
jun2019=[]
jul2019=[]
aug2019=[]
sep2019=[]
oct2019=[]
nov2019=[]
dec2019=[]

jan2020=[]
feb2020=[]
mar2020=[]
apr2020=[]
may2020=[]
jun2020=[]
jul2020=[]
aug2020=[]
sep2020=[]
oct2020=[]
nov2020=[]
dec2020=[]

jan2021=[]
feb2021=[]
mar2021=[]
apr2021=[]
may2021=[]
jun2021=[]
jul2021=[]
aug2021=[]
sep2021=[]
oct2021=[]
nov2021=[]
dec2021=[]


def yearly(setyear):
    for j in range(len(data_list[0])):
        if data_list[6][j]==setyear:
            if data_list[3][j] <= 31:
                eval("jan"+str(setyear)).append(data_list[0][j])
            elif 31 < data_list[3][j] <= 59:
                eval("feb"+str(setyear)).append(data_list[0][j])
            elif 59 < data_list[3][j] <= 90:
                eval("mar"+str(setyear)).append(data_list[0][j])
            elif 90 < data_list[3][j] <= 120:
                eval("apr"+str(setyear)).append(data_list[0][j])
            elif 120 < data_list[3][j]<= 151:
                eval("may"+str(setyear)).append(data_list[0][j])
            elif 151 < data_list[3][j] <= 181:
                eval("jun"+str(setyear)).append(data_list[0][j])        
            elif 181 < data_list[3][j] <= 212:
                eval("jul"+str(setyear)).append(data_list[0][j]) 
            elif 212 < data_list[3][j] <= 243:
                eval("aug"+str(setyear)).append(data_list[0][j]) 
            elif 243 < data_list[3][j] <= 273:
                eval("sep"+str(setyear)).append(data_list[0][j])         
            elif 273 < data_list[3][j] <= 304:
                eval("oct"+str(setyear)).append(data_list[0][j])
            elif 304 < data_list[3][j] <= 334:
                eval("nov"+str(setyear)).append(data_list[0][j])        
            elif 304 < data_list[3][j]:
                eval("dec"+str(setyear)).append(data_list[0][j]) 


yearly(2021)
yearly(2020)
yearly(2019)
yearly(2018)
yearly(2017)
yearly(2016)
yearly(2015)
yearly(2014)
yearly(2013)
yearly(2012)
yearly(2011)
yearly(2010)
yearly(2009)
yearly(2008)
yearly(2007)
yearly(2006)
yearly(2005)



#with open('test_est_5y.csv', 'w') as file:
#    writer = csv.writer(file)
#    for k in range(5):
#        writer.writerow(data_list[k])


months_2021=np.array((str(jan2021).replace("[","").replace("]",""), str(feb2021).replace("[","").replace("]",""), str(mar2021).replace("[","").replace("]",""), str(apr2021).replace("[","").replace("]",""), str(may2021).replace("[","").replace("]",""), str(jun2021).replace("[","").replace("]",""), str(jul2021).replace("[","").replace("]",""), str(aug2021).replace("[","").replace("]",""), str(sep2021).replace("[","").replace("]",""), str(oct2021).replace("[","").replace("]",""), str(nov2021).replace("[","").replace("]",""), str(dec2021).replace("[","").replace("]","")), dtype=object)
months_2020=np.array((str(jan2020).replace("[","").replace("]",""), str(feb2020).replace("[","").replace("]",""), str(mar2020).replace("[","").replace("]",""), str(apr2020).replace("[","").replace("]",""), str(may2020).replace("[","").replace("]",""), str(jun2020).replace("[","").replace("]",""), str(jul2020).replace("[","").replace("]",""), str(aug2020).replace("[","").replace("]",""), str(sep2020).replace("[","").replace("]",""), str(oct2020).replace("[","").replace("]",""), str(nov2020).replace("[","").replace("]",""), str(dec2020).replace("[","").replace("]","")), dtype=object)
months_2019=np.array((str(jan2019).replace("[","").replace("]",""), str(feb2019).replace("[","").replace("]",""), str(mar2019).replace("[","").replace("]",""), str(apr2019).replace("[","").replace("]",""), str(may2019).replace("[","").replace("]",""), str(jun2019).replace("[","").replace("]",""), str(jul2019).replace("[","").replace("]",""), str(aug2019).replace("[","").replace("]",""), str(sep2019).replace("[","").replace("]",""), str(oct2019).replace("[","").replace("]",""), str(nov2019).replace("[","").replace("]",""), str(dec2019).replace("[","").replace("]","")), dtype=object)
months_2018=np.array((str(jan2018).replace("[","").replace("]",""), str(feb2018).replace("[","").replace("]",""), str(mar2018).replace("[","").replace("]",""), str(apr2018).replace("[","").replace("]",""), str(may2018).replace("[","").replace("]",""), str(jun2018).replace("[","").replace("]",""), str(jul2018).replace("[","").replace("]",""), str(aug2018).replace("[","").replace("]",""), str(sep2018).replace("[","").replace("]",""), str(oct2018).replace("[","").replace("]",""), str(nov2018).replace("[","").replace("]",""), str(dec2018).replace("[","").replace("]","")), dtype=object)
months_2017=np.array((str(jan2017).replace("[","").replace("]",""), str(feb2017).replace("[","").replace("]",""), str(mar2017).replace("[","").replace("]",""), str(apr2017).replace("[","").replace("]",""), str(may2017).replace("[","").replace("]",""), str(jun2017).replace("[","").replace("]",""), str(jul2017).replace("[","").replace("]",""), str(aug2017).replace("[","").replace("]",""), str(sep2017).replace("[","").replace("]",""), str(oct2017).replace("[","").replace("]",""), str(nov2017).replace("[","").replace("]",""), str(dec2017).replace("[","").replace("]","")), dtype=object)
months_2016=np.array((str(jan2016).replace("[","").replace("]",""), str(feb2016).replace("[","").replace("]",""), str(mar2016).replace("[","").replace("]",""), str(apr2016).replace("[","").replace("]",""), str(may2016).replace("[","").replace("]",""), str(jun2016).replace("[","").replace("]",""), str(jul2016).replace("[","").replace("]",""), str(aug2016).replace("[","").replace("]",""), str(sep2016).replace("[","").replace("]",""), str(oct2016).replace("[","").replace("]",""), str(nov2016).replace("[","").replace("]",""), str(dec2016).replace("[","").replace("]","")), dtype=object)
months_2015=np.array((str(jan2015).replace("[","").replace("]",""), str(feb2015).replace("[","").replace("]",""), str(mar2015).replace("[","").replace("]",""), str(apr2015).replace("[","").replace("]",""), str(may2015).replace("[","").replace("]",""), str(jun2015).replace("[","").replace("]",""), str(jul2015).replace("[","").replace("]",""), str(aug2015).replace("[","").replace("]",""), str(sep2015).replace("[","").replace("]",""), str(oct2015).replace("[","").replace("]",""), str(nov2015).replace("[","").replace("]",""), str(dec2015).replace("[","").replace("]","")), dtype=object)
months_2014=np.array((str(jan2014).replace("[","").replace("]",""), str(feb2014).replace("[","").replace("]",""), str(mar2014).replace("[","").replace("]",""), str(apr2014).replace("[","").replace("]",""), str(may2014).replace("[","").replace("]",""), str(jun2014).replace("[","").replace("]",""), str(jul2014).replace("[","").replace("]",""), str(aug2014).replace("[","").replace("]",""), str(sep2014).replace("[","").replace("]",""), str(oct2014).replace("[","").replace("]",""), str(nov2014).replace("[","").replace("]",""), str(dec2014).replace("[","").replace("]","")), dtype=object)
months_2013=np.array((str(jan2013).replace("[","").replace("]",""), str(feb2013).replace("[","").replace("]",""), str(mar2013).replace("[","").replace("]",""), str(apr2013).replace("[","").replace("]",""), str(may2013).replace("[","").replace("]",""), str(jun2013).replace("[","").replace("]",""), str(jul2013).replace("[","").replace("]",""), str(aug2013).replace("[","").replace("]",""), str(sep2013).replace("[","").replace("]",""), str(oct2013).replace("[","").replace("]",""), str(nov2013).replace("[","").replace("]",""), str(dec2013).replace("[","").replace("]","")), dtype=object)
months_2012=np.array((str(jan2012).replace("[","").replace("]",""), str(feb2012).replace("[","").replace("]",""), str(mar2012).replace("[","").replace("]",""), str(apr2012).replace("[","").replace("]",""), str(may2012).replace("[","").replace("]",""), str(jun2012).replace("[","").replace("]",""), str(jul2012).replace("[","").replace("]",""), str(aug2012).replace("[","").replace("]",""), str(sep2012).replace("[","").replace("]",""), str(oct2012).replace("[","").replace("]",""), str(nov2012).replace("[","").replace("]",""), str(dec2012).replace("[","").replace("]","")), dtype=object)
months_2011=np.array((str(jan2011).replace("[","").replace("]",""), str(feb2011).replace("[","").replace("]",""), str(mar2011).replace("[","").replace("]",""), str(apr2011).replace("[","").replace("]",""), str(may2011).replace("[","").replace("]",""), str(jun2011).replace("[","").replace("]",""), str(jul2011).replace("[","").replace("]",""), str(aug2011).replace("[","").replace("]",""), str(sep2011).replace("[","").replace("]",""), str(oct2011).replace("[","").replace("]",""), str(nov2011).replace("[","").replace("]",""), str(dec2011).replace("[","").replace("]","")), dtype=object)
months_2010=np.array((str(jan2010).replace("[","").replace("]",""), str(feb2010).replace("[","").replace("]",""), str(mar2010).replace("[","").replace("]",""), str(apr2010).replace("[","").replace("]",""), str(may2010).replace("[","").replace("]",""), str(jun2010).replace("[","").replace("]",""), str(jul2010).replace("[","").replace("]",""), str(aug2010).replace("[","").replace("]",""), str(sep2010).replace("[","").replace("]",""), str(oct2010).replace("[","").replace("]",""), str(nov2010).replace("[","").replace("]",""), str(dec2010).replace("[","").replace("]","")), dtype=object)
months_2009=np.array((str(jan2009).replace("[","").replace("]",""), str(feb2009).replace("[","").replace("]",""), str(mar2009).replace("[","").replace("]",""), str(apr2009).replace("[","").replace("]",""), str(may2009).replace("[","").replace("]",""), str(jun2009).replace("[","").replace("]",""), str(jul2009).replace("[","").replace("]",""), str(aug2009).replace("[","").replace("]",""), str(sep2009).replace("[","").replace("]",""), str(oct2009).replace("[","").replace("]",""), str(nov2009).replace("[","").replace("]",""), str(dec2009).replace("[","").replace("]","")), dtype=object)
months_2008=np.array((str(jan2008).replace("[","").replace("]",""), str(feb2008).replace("[","").replace("]",""), str(mar2008).replace("[","").replace("]",""), str(apr2008).replace("[","").replace("]",""), str(may2008).replace("[","").replace("]",""), str(jun2008).replace("[","").replace("]",""), str(jul2008).replace("[","").replace("]",""), str(aug2008).replace("[","").replace("]",""), str(sep2008).replace("[","").replace("]",""), str(oct2008).replace("[","").replace("]",""), str(nov2008).replace("[","").replace("]",""), str(dec2008).replace("[","").replace("]","")), dtype=object)
months_2007=np.array((str(jan2007).replace("[","").replace("]",""), str(feb2007).replace("[","").replace("]",""), str(mar2007).replace("[","").replace("]",""), str(apr2007).replace("[","").replace("]",""), str(may2007).replace("[","").replace("]",""), str(jun2007).replace("[","").replace("]",""), str(jul2007).replace("[","").replace("]",""), str(aug2007).replace("[","").replace("]",""), str(sep2007).replace("[","").replace("]",""), str(oct2007).replace("[","").replace("]",""), str(nov2007).replace("[","").replace("]",""), str(dec2007).replace("[","").replace("]","")), dtype=object)
months_2006=np.array((str(jan2006).replace("[","").replace("]",""), str(feb2006).replace("[","").replace("]",""), str(mar2006).replace("[","").replace("]",""), str(apr2006).replace("[","").replace("]",""), str(may2006).replace("[","").replace("]",""), str(jun2006).replace("[","").replace("]",""), str(jul2006).replace("[","").replace("]",""), str(aug2006).replace("[","").replace("]",""), str(sep2006).replace("[","").replace("]",""), str(oct2006).replace("[","").replace("]",""), str(nov2006).replace("[","").replace("]",""), str(dec2006).replace("[","").replace("]","")), dtype=object)
months_2005=np.array((str(jan2005).replace("[","").replace("]",""), str(feb2005).replace("[","").replace("]",""), str(mar2005).replace("[","").replace("]",""), str(apr2005).replace("[","").replace("]",""), str(may2005).replace("[","").replace("]",""), str(jun2005).replace("[","").replace("]",""), str(jul2005).replace("[","").replace("]",""), str(aug2005).replace("[","").replace("]",""), str(sep2005).replace("[","").replace("]",""), str(oct2005).replace("[","").replace("]",""), str(nov2005).replace("[","").replace("]",""), str(dec2005).replace("[","").replace("]","")), dtype=object)

#allmonths=np.array([month_avg2021, month_avg2020, month_avg2019, month_avg2018, month_avg2017, month_avg2016, month_avg2015, month_avg2014, month_avg2013, month_avg2012, month_avg2011, month_avg2010, month_avg2009, month_avg2008, month_avg2007, month_avg2006, month_avg2005, month_avg2004,])


os.chdir('path_to_save_dir'+loc_pressure)

np.savetxt("monthly_"+loc_name+"_2021"+loc_pressure+".csv", months_2021, delimiter=",", fmt='%s')
np.savetxt("monthly_"+loc_name+"_2020"+loc_pressure+".csv", months_2020, delimiter=",", fmt='%s')
np.savetxt("monthly_"+loc_name+"_2019"+loc_pressure+".csv", months_2019, delimiter=",", fmt='%s')
np.savetxt("monthly_"+loc_name+"_2018"+loc_pressure+".csv", months_2018, delimiter=",", fmt='%s')
np.savetxt("monthly_"+loc_name+"_2017"+loc_pressure+".csv", months_2017, delimiter=",", fmt='%s')
np.savetxt("monthly_"+loc_name+"_2016"+loc_pressure+".csv", months_2016, delimiter=",", fmt='%s')
np.savetxt("monthly_"+loc_name+"_2015"+loc_pressure+".csv", months_2015, delimiter=",", fmt='%s')
np.savetxt("monthly_"+loc_name+"_2014"+loc_pressure+".csv", months_2014, delimiter=",", fmt='%s')
np.savetxt("monthly_"+loc_name+"_2013"+loc_pressure+".csv", months_2013, delimiter=",", fmt='%s')
np.savetxt("monthly_"+loc_name+"_2012"+loc_pressure+".csv", months_2012, delimiter=",", fmt='%s')
np.savetxt("monthly_"+loc_name+"_2011"+loc_pressure+".csv", months_2011, delimiter=",", fmt='%s')
np.savetxt("monthly_"+loc_name+"_2010"+loc_pressure+".csv", months_2010, delimiter=",", fmt='%s')
np.savetxt("monthly_"+loc_name+"_2009"+loc_pressure+".csv", months_2009, delimiter=",", fmt='%s')
np.savetxt("monthly_"+loc_name+"_2008"+loc_pressure+".csv", months_2008, delimiter=",", fmt='%s')
np.savetxt("monthly_"+loc_name+"_2007"+loc_pressure+".csv", months_2007, delimiter=",", fmt='%s')
np.savetxt("monthly_"+loc_name+"_2006"+loc_pressure+".csv", months_2006, delimiter=",", fmt='%s')
np.savetxt("monthly_"+loc_name+"_2005"+loc_pressure+".csv", months_2005, delimiter=",", fmt='%s')
