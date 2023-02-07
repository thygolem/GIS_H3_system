import pandas as pd
import numpy as np



h10sample = pd.read_csv('10sample.csv', sep=';')


def get_cartesian(lat=None,lon=None): # convert lat/long to cartesian
    lat, lon = np.deg2rad(lat), np.deg2rad(lon) # convert to radians
    R = 100 # radius of the earth
    x = R * np.cos(lat) * np.cos(lon)  # convert to cartesian
    y = R * np.cos(lat) * np.sin(lon)   # convert to cartesian
    z = R *np.sin(lat)  # convert to cartesian
    return x, y, z   # return cartesian coordinates

x = []
y = []
z = []

for index, row in h10sample.iterrows():
    xCart, yCart, zCart = get_cartesian(row['Lat'], row['Long'])
    x.append(xCart)   
    y.append(yCart)
    z.append(zCart)

    # xyDF['x'] = x
    # xyDF.append(row['lat'])

h10sample['x'] = x
h10sample['y'] = y
h10sample['z'] = z


types = []


NoTrees = '0'
Eucalyptus = '1'
MixedWood = '2'
Pine = '3'
Oak = '4'
Birch = '5' 
Chestnut = '6'
FloweringPlants = '7'
Fire = '8'
# - El tipo de arbol: 'No trees', 'Eucalyptus', 'Mixed wood', 'Pine', 'Oak', 'Birch', 'Chestnut', 'Flowering plants'
for index, row in h10sample.iterrows():
  if row['NewTreeClas'] == 'No tree':
    # print('yeah', row['index'])
    types.append(NoTrees)
  elif row['NewTreeClas'] == 'Eucalyptus':
    # print('yeah', row['index'])
    types.append(Oak)
  elif row['NewTreeClas'] == 'Mixed wood':
    # print('yeah', row['index'])
    types.append(MixedWood)
  elif row['NewTreeClas'] == 'Pine':
    # print('yeah', row['index'])
    types.append(Pine)
  elif row['NewTreeClas'] == 'Oak':
    # print('yeah', row['index'])
    types.append(Oak)
  elif row['NewTreeClas'] == 'Birch':
    # print('yeah', row['index'])
    types.append(Birch)
  elif row['NewTreeClas'] == 'Chestnut':
    # print('yeah', row['index'])
    types.append(Chestnut)
  elif row['NewTreeClas'] == 'Flowering plants':
    # print('yeah', row['index'])
    types.append(FloweringPlants)


h10sample['types'] = types

h3ID_type_xyz = h10sample[['index', 'types', 'x', 'y', 'z']]
h3ID_type_xyz

h3ID_type_xyz.to_csv('H3ID_types_xyz.csv', index=False)

# print(h10sample[['index', 'types', 'x', 'y', 'z']])



# gisJson = {}

# for index, row in h10sample.iterrows():
#     gisJson = {'key': h10sample['index'],
#              'value':  [str(h10sample['types'])]
#              }
    # r.set(str(gisJson['key']), str(gisJson['value']))


# print(gisJson['key'])
# print(gisJson['value'])
# r.set(str(gisJson['key']), str(gisJson['value']))



# value = r.get(gisJson['key']).decode("utf-8")
# value = r.get(gisJson['key'])
# print(value)  # Output: value
