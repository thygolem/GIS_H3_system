import pymongo
import pandas as pd


client = pymongo.MongoClient("mongodb://localhost:27017/")

# Choose a database and a collection
db = client["gis_yeah"]
collection = db["h3id_types_xyz"]


h10sample = pd.read_csv('H3ID_types_xyz.csv', sep=',')

my_json = {
    "H3ID": "John Doe",
    "age": 35,
    "city": "New York"
}


for index, row in h10sample.iterrows():
    h3id = row['index']
    types = row['types']
    x = row['x']
    y = row['y']
    z = row['z']

    my_gis_json = {
        "H3ID": h3id,
        "types": types,
        "x": x,
        "y": y,
        "z": z
    }
    collection.insert_one(my_gis_json)

print(my_gis_json)


    # key = row['index']
    # value = {
    #     'types': row['types'],
    #     'x': row['x'],
    #     'y': row['y'],
    #     'z': row['z']
    # }

    # # Store the data as a hash in Redis
    # r.hmset(key, value)









# r.set("key", "value")

# # Get value from Redis cache
# value = r.get("key").decode("utf-8")
# print(value)  # Output: value









# for hash_name in hash_names:
#     hash_ = r.hgetall(hash_name)
#     # print(hash_name.decode())s
#     for value in hash_:
#         # print('H3ID: ', hash_name.decode(), 'DATA: ', str(hash_.items()))
#         print('H3ID: ', hash_name.decode(), 
#                 'DATA: ', str(r.hmget(hash_name, ['types'])))
#         msg = 'DATA: ', str(hash_.items())
#         udp_socket.sendto(bytes(str(msg), encoding='utf-8') , destination_address_1)
#         break
