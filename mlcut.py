import numpy as np
from astropy.io import fits
from astropy.table import Table

directory = "C:/Users/honor/Downloads/compact_cluster_catalogs"

### gets the specific catalogs from the larger file
file = directory + "/ngc4571_phangs-hst_v1p1_ml_class12.fits"
file2 = directory + "/ngc4571_phangs-hst_v1p1_human_class12.fits"

### gets data from the catalog files
data = fits.getdata(file)
data2 = fits.getdata(file2)

### converting to a table
data = Table(data)
data2 = Table(data2)

### gets the column names of the data and organizes data accordingly
names = data.colnames
names2 = data2.colnames

### converts them into a list as well as the x and y coordinates 
id = list(data[names[0]])
id2 = list(data2[names2[0]])
x_coord = data[names[1]]
y_coord = data[names[2]]

### gets magnitude values of different filter bands
B_band = data[names[12]]
B_band2 = data2[names2[12]]
V_band = data[names[14]]
V_band2 = data2[names2[14]]
I_band = data[names[16]]
I_band2 = data2[names2[16]]

### makes B-V and V-I tables of the data
B_V = B_band-V_band
B_V2 = B_band2-V_band2
V_I = V_band-I_band
V_I2 = V_band2-I_band2

### makes new lists based on color cuts
id_list = []
id_list2 = []
x_list = []
y_list = []
output_list = []

### adds ML clusters with color cut
for i in range(0, len(B_V)):
  if B_V[i]>=0.5 and V_I[i]>=0.73:
    id_list.append(id[i])

### adds Human clusters with color cut
for i in range(0, len(B_V2)):
  if B_V2[i]>=0.5 and V_I2[i]>=0.73:
    id_list2.append(id2[i])

### sorts the clusters in the ML catalog not found in the Human catalog
for i in range(0, len(id_list)):
  if np.any(id_list[i] == id_list2):
    pass
  else:
    output_list.append(id_list[i])

### creates x and y coordinate lists of sorted ML clusters 
for i in range(0, len(output_list)):
  order = id.index(output_list[i])
  x_list.append(x_coord[order])
  y_list.append(y_coord[order])

### converts int lists to string lists
string_output_list = [str(x) for x in output_list]
string_x_list = [str(x) for x in x_list]
string_y_list = [str(x) for x in y_list]

### combines all 3 lists into a big list
final_output_list = ["ID: " + ID + ", (" + x + ", " + y + ")" for ID, x, y in zip(string_output_list, string_x_list, string_y_list)]

### writes all info to a txt file
textfile = open("C:/Users/honor/Downloads/compact_cluster_catalogs/data.txt", "w")
textfile.write("Galaxy: NGC 1566\n")
for element in final_output_list:
    textfile.write(element + "\n")
textfile.close()

#print(id_list)
#print(id_list2)
#print ("", len(x_list))
#print ("", len(y_list))
#print(final_output_list)
#print(len(output_list))