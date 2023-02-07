import socket
import pandas as pd
import redis
import json


h10sample = pd.read_csv('H3ID_types_xyz.csv', sep=',')
r = redis.Redis(host='localhost', port=6379, db=0)


# Crear un socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Dirección y puerto destino
destination_address_0 = ('127.0.0.1', 3000)
destination_address_1 = ('127.0.0.1', 3001)

m_address = ('192.168.2.131', 3001)


H3IDlist = h10sample['index']
number_of_lines = str(len(H3IDlist.index))
# number_of_lines = str(0)


udp_socket.sendto(number_of_lines.encode(), destination_address_0)



# Obtener la lista de todos los nombres de los hashes en Redis
hash_names = r.keys()
# print(hash_names)

msg = []

for hash_name in hash_names:
    hash_ = r.hgetall(hash_name)
    # print(hash_name.decode())s
    for value in hash_:
        print('H3ID: ', hash_name.decode(), 'DATA: ', str(hash_.items()))
        msg = 'DATA: ', str(hash_.items())
        udp_socket.sendto(bytes(str(msg), encoding='utf-8') , destination_address_1)
        break

