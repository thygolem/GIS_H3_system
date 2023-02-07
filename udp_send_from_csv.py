import socket
import pandas as pd


# h10sample = pd.read_csv('../data/joaquin/PruebaIvan2.csv', sep=';')
h10sample = pd.read_csv('H3ID_types_xyz.csv', sep=',')


# Crear un socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# Dirección y puerto destino
destination_address_0 = ('127.0.0.1', 3000)
destination_address_1 = ('127.0.0.1', 3001)



# Mensaje a enviar
number_of_lines = str(len(h10sample.index))

# number_of_lines = str(0)
print(number_of_lines, 'lineas')
# MESSAGE = str(17)


# # Enviar el mensaje a la dirección destino
udp_socket.sendto(number_of_lines.encode(), destination_address_0)


for _ in range(len(h10sample.index)):
    print(h10sample.iloc[_])
    # msg = str(h10sample.iloc[_])
    # msg = '0'
    msg = str(h10sample.iloc[_])
    udp_socket.sendto(msg.encode(), destination_address_1)
    







# for i in range(number_of_lines):
#     count = count+7

#     MESSAGE = str(count)
#     print("UDP target IP:", UDP_IP)
#     print("UDP target port:", UDP_PORT)
#     print("message:", MESSAGE)

#     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))
#     sock.close()



# Cerrar el socket
udp_socket.close()
