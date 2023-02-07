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
    # print(hash_name.decode())
    for value in hash_:
        print('H3ID: ', hash_name.decode(), 'DATA: ', str(hash_.types()))
        msg = 'H3ID: ', hash_name.decode(), 'DATA: ', str(hash_.types())
        udp_socket.sendto(bytes(str(msg), encoding='utf-8') , destination_address_1)
        break

# hashs = r.hgetall(hash_name)

# for _ in range(int(number_of_lines)):
#     for hash_name in hash_names:
#         hashs = r.hgetall(hash_name)
#         print(f'Hash: {hash_name}')
#         msg.append('a')
#         for key, value in hashs.items():
#             print(f'{key}: {value}')
#             msg.append('b')

        
#     # udp_socket.sendto(bytes(str(msg)) , destination_address_1)
# udp_socket.sendto(bytes(str(msg), encoding='utf-8') , destination_address_1)













# Iterar a través de todos los hashes y mostrar cada clave con sus valores
# for _ in range(int(number_of_lines)):



# for hash_name in hash_names:
#     hash = r.hgetall(hash_name)
#     print(f'Hash: {hash_name}')
#     msg.append(str(f'Hash: {hash_name}'))
#     for key, value in hash.items():
#         print(f'{key}: {value}')
#         msg.append(str(f'{key}: {value}'))
#         # udp_socket.sendto(msg.encode(), destination_address_1)
# udp_socket.sendto(bytes(str(msg), encoding='utf-8') , destination_address_1)



# print(str(msg))
    # udp_socket.sendto(msg.encode(), destination_address_1)
# bytes(str(numbers), encoding='utf-8')






# # values = r.hget('8a39242600c7fff', 'types')

# hashs = r.hgetall('8a39242600c7fff')

# for i in H3IDlist:
#     # print(i)
#     value = r.hgetall(i)
#     for key, value in hashs.items():
#         print(f'{key}: {value}')





# Imprimir los valores del hash
# for key, value in hashs.items():
#     print(f'{key}: {value}')

# print(values)
# print(hashs)


# for value in values:
#     if value:
#         # procesar el valor aquí
#         print(value)
#     else:
#         print("La clave no existe en la base de datos")

# for _ in H3IDlist:
#     value = r.mget(_)
#     print(value)




# udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
