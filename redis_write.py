import redis
import pandas as pd


# Connect to Redis server
r = redis.Redis(host='localhost', port=6379, db=0)


h10sample = pd.read_csv('H3ID_types_xyz.csv', sep=',')

for index, row in h10sample.iterrows():
    key = row['index']
    value = {
        'types': row['types'],
        'x': row['x'],
        'y': row['y'],
        'z': row['z']
    }

    # Store the data as a hash in Redis
    r.hmset(key, value)









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
