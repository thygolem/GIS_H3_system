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
