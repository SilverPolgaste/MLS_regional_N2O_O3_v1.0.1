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
loc_pressure = "32"
pressurename = "_32.csv"
location = geo_loc(loc_name, loc_lat-loc_halfsize, loc_lat+loc_halfsize, loc_lon-loc_halfsize, loc_lon+loc_halfsize)

directory = 'path_to_data_dir'

data_arr=np.array([[],[],[],[],[],[]])

for file in os.listdir(directory):	
    hdffile = os.fsdecode(file)
    if hdffile.endswith(".he5"):
        print(hdffile)
        f = h5py.File(hdffile, mode='r')
        subset=18
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
        fullindex=[int(year[0]+dateindex[0])]
        #print(dateindex)
        # add data to list
        data = np.array([f[name][:,subset][box_index]*10**6, latitude[box_index], longitude[box_index], (fullindex)*len(latitude[box_index]), quality[box_index], convergence[box_index]], dtype=np.float32)
        #print(data)
        data_arr=np.hstack((data_arr, data))
        continue
    else:
        continue
		
		
data_list=[[],[],[],[],[],[]]

for i in range(len(data_arr[0])):
    for j in range(6):
        if data_arr[4][i]>=1 and data_arr[5][1]<=1.03:
            data_list[j].append(data_arr[j][i])
        else:
            continue

# endarr = np.array([data_list[4],data_list[0]])

# unique_str = np.unique(endarr[0])

# indices = [np.where(endarr[0] == s)[0] for s in unique_str]

# sums = [np.add.reduceat(endarr[1], idx) for idx in indices]

# means = [s / idx.size for s, idx in zip(sums, indices)]
# print(len(unique_str), len(means))
# averages = [unique_str, means]
d = {}

for i, s in enumerate(data_list[3]):
    if s not in d:
        d[s] = [data_list[0][i]]
    else:
        d[s].append(data_list[0][i])

for key in d:
    d[key] = sum(d[key])/len(d[key])
    
averages = np.column_stack([list(d.keys()), list(d.values())])

print(len(data_list[0]))
print(len(averages))


os.chdir('path_to_data_dir')

np.savetxt("n2oavg_"+loc_name+pressurename, averages, fmt='%s')


