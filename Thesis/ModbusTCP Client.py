# # Import Required Functions from Library
from pymodbus.constants import Endian
from pymodbus.client.sync import ModbusTcpClient
from pymodbus.payload import BinaryPayloadBuilder
import socket
import time

# # Get System IP address and Define Default PORT-502 for Connection
hostname = socket.gethostname()    
server_ip_address = socket.gethostbyname(hostname)
server_port = 502
print("[+]Info : IP Address : " + str(server_ip_address))

# # Connect with Server as a Client
client = ModbusTcpClient(server_ip_address,server_port)

# # Check if Client is Connected to Server or not ?
print("[+]Info : Connection : " + str(client.connect()))

# # Write Holding Regsiter Value on Server
for i in range(0,10):
    print(f"[+]Info : Writing Value : {i*i} On Register : {i} ")
    client.write_registers(i,i*i)

# # Read Holding Register Values from Server
value = client.read_holding_registers(0,10)
value.registers


